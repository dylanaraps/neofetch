#!/usr/bin/env bash
# Fetch info about your system
#
# Dependencies:
#   Displaying Images: w3m
#   Image Cropping: ImageMagick
#   Wallpaper Display: feh
#   Window Manager Detection: wmctrl
#   Current Song: mpc
#
# Created by Dylan Araps
# https://github.com/dylanaraps/dotfiles


# Info Prefixes {{{
# The titles that come before the info (Ram:, Cpu:, Uptime:)
# TODO: Add an easy way to specify these at launch.


title_os="OS"
title_kernel="Kernel"
title_uptime="Uptime"
title_packages="Packages"
title_shell="Shell"
title_windowmanager="Window Manager"
title_cpu="CPU"
title_memory="Memory"
title_song="Song"


# }}}


# Text Formatting {{{


# Set to "" or comment this line to disable bold text
bold="\033[1m"

# This is a simple function to make the vars below easier to edit.
color () {
    echo "\033[38;5;${1}m"
}

# Default colors
# Colors can be defined at launch with:
# "--titlecol 1, --subtitlecol 2, --coloncol 3, --infocol 4"
# Or the shorthand "-c/--color 1 2 3 4"
# Or by editing them below.
title_color=$(color 7)
subtitle_color=$(color 1)
colon_color=$(color 7) # Also changes underline color
info_color=$(color 7)

# Reset formatting
# Removing this line will fuck up the text formatting
clear="\033[0m"


# }}}


# Custom Image {{{

# Enable or disable the use of images (Disable images at launch with "--noimg")
enableimages=1

# If 1, fetch will use a cropped version of your wallpaper as the image
# (Disable this at launch with "--nowall")
# NOTE: This is only compatible with feh, I can add support for more
#       wallpaper setters but you'll need to show me a way to get the current
#       wallpaper from the commandline.
usewall=1

# The image to use if usewall=0. There's also the launch flags "-i" + "--image"
# to set a custom image at launch.
img="$HOME/Pictures/avatars/gon.png"

# Image size/offset
# (Customizable at launch with these flags: --size 128 --xoffset 0 --yoffset 0")
imgsize=128
yoffset=0
xoffset=0

# Default crop offset (Customizable at launch with --cropoffset)
# Possible values:
# northwest, north, northeast, west, center, east, southwest, south, southeast
crop_offset="center"

# Padding to align text to the right
# TODO: Find a reliable way to set this dynamically. I can get
#       this to work based on font width but there's no reliable way
#       of getting fontwidth for every terminal.
pad="                             "

# Directory to store cropped images
imgtempdir="$HOME/.fetchimages"


# }}}


# Get Info {{{
# Commands to use when gathering info


# Title (Configurable with "-t" and "--title" at launch)
# To use the usual "user@hostname" change the line below to:
title="$(whoami)@$(hostname)"

# Operating System (Configurable with "-O" and "--distro" at launch)
# You can manually set this if the command below doesn't work for you.
os=$(awk '/^NAME=/' /etc/*ease | sed -n 's/^NAME=//p' | tr -d '"')

# Linux kernel name/version (Configurable with "-K" and "--kernel" at launch)
kernel=$(uname -r)

# System Uptime (Configurable with "-U" and "--uptime" at launch)
uptime=$(uptime -p)

# Total number of packages (Configurable with "-P" and "--packages" at launch)
# If your package manager can't be found open an issue on my github repo.
# (Link is at the top)
getpackages () {
    case $os in
        'Arch Linux'|'Parabola GNU/Linux-libre'|'Manjaro'|'Antergos') \
            packages=$(pacman -Q | wc -l) ;;
        'Ubuntu'|'Mint'|'Debian'|'Kali Linux') \
            packages=$(dpkg --get-selections | grep -v deinstall$ | wc -l) ;;
        'Slackware') \
            packages=$(ls -1 /var/log/packages | wc -l) ;;
        'Gentoo'|'Funtoo') \
            packages=$(ls -d /var/db/pkg/*/* | wc -l) ;;
        'Fedora'|'openSUSE'|'Red Hat Enterprise Linux'|'CentOS') \
            packages=$(rpm -qa | wc -l) ;;
        'CRUX') \
            packages=$(pkginfo -i | wc -l) ;;
        *) packages="unknown" ;;
    esac
}


# Shell (Configurable with "-s" and "--shell" at launch)
shell="$SHELL"

# Window manager (Configurable with "-W" and "--windowmanager" at launch)
# (depends on wmctrl)
# This can be detected without wmctrl by using an array of window manager
# process names and pgrep but it's really slow.
# (Doubles script startup time in some cases).
# If you don't want to install wmctrl you can either edit the var below,
# export the "windowmanager" variable in your shell's configuration file,
# or run the script with: --windowmanager wmname
# windowmanager="openbox"
if [ -z $windowmanager ]; then
    if type -p wmctrl >/dev/null 2>&1; then
        windowmanager=$(wmctrl -m | awk '/Name:/ {printf $2}')
    elif [ -e ~/.xinitrc ]; then
        windowmanager=$(grep -v "^#" "${HOME}/.xinitrc" | tail -n 1 | cut -d " " -f2)
    else
        windowmanager="Unknown"
    fi
fi

# Processor (Configurable with "-C", "-S" and "--cpu", "--speed" at launch)
cpu="$(awk 'BEGIN{FS=":"} /model name/ {print $2; exit}' /proc/cpuinfo |\
    awk 'BEGIN{FS="@"; OFS="\n"} { print $1; exit }' |\
    sed -e 's/\((tm)\|(TM)\)//' -e 's/\((R)\|(r)\)//' -e 's/^\ //')"

# Get current/min/max cpu speed
speed_type="max"
cpuspeed () {
    case $speed_type in
        current) speed="$(lscpu | awk '/CPU MHz:/ {printf "scale=1; " $3 " / 1000 \n"}' | bc -l)" ;;
        min) speed="$(lscpu | awk '/CPU min MHz:/ {printf "scale=1; " $4 " / 1000 \n"}' | bc -l)" ;;
        max) speed="$(lscpu | awk '/CPU max MHz:/ {printf "scale=1; " $4 " / 1000 \n"}' | bc -l)" ;;
    esac
}

# Memory (Configurable with "-M" and "--memory" at launch)
# Print the total amount of ram and amount of ram in use
memory=$(free -m | awk '/Mem:/ {printf $3 "MB / " $2 "MB"}')

# Currently playing song/artist (Configurable with "-m" and "--song" at launch)
song=$(mpc current)

# Print terminal colors in a line
# (Configurable with "--printcols start end" at launch)
# Start/End are vars for the range of colors to print
# The default values below print 8 colors in total.
start=0
end=7

# Print the color blocks by default.
printcols=1

printcols () {
    echo
    echo

    while [ "$start" -le "$end" ]; do
        echo -n "\033[48;5;${start}m      "
        start=$((start + 1))

        # Split the blocks at 8 colors
        [ $end -ge 9 ] && [ $start -eq 8 ] && echo -e "\033[0m"
    done

    # Vertically center colors if they're one row tall
    [ $end -le 8 ] && echo

    # Clear formatting
    echo -n "$clear"
}


# }}}


# Usage {{{


usage () {
    echo
    echo "usage: ${0##*/} [--colors 1 2 4 5] [--kernel \"\$(uname -rs)\"]"
    echo
    echo "   Info:"
    echo "   --title string         Change the title at the top"
    echo "   --distro string/cmd    Manually set the distro"
    echo "   --kernel string/cmd    Manually set the kernel"
    echo "   --uptime string/cmd    Manually set the uptime"
    echo "   --packages string/cmd  Manually set the package count"
    echo "   --shell string/cmd     Manually set the shell"
    echo "   --winman string/cmd Manually set the window manager"
    echo "   --cpu string/cmd       Manually set the cpu name"
    echo "   --memory string/cmd    Manually set the memory"
    echo "   --speed string/cmd     Manually set the cpu speed"
    echo "   --speed_type           Change the type of cpu speed to get"
    echo "                          Possible values: current, min, max"
    echo "   --song string/cmd      Manually set the current song"
    echo
    echo "   Text Colors:"
    echo "   --colors 1 2 3 4       Change the color of text"
    echo "                          (title, subtitle, colon, info)"
    echo "   --titlecol num         Change the color of the title"
    echo "   --subtitlecol num      Change the color of the subtitle"
    echo "   --coloncol num         Change the color of the colons"
    echo "   --infocol num          Change the color of the info"
    echo
    echo "   Color Blocks:"
    echo "   --printcols start end  Range of colors to print as blocks"
    echo "   --nopal                Disable the color blocks"
    echo
    echo "   Image:"
    echo "   --image                Image to display with the script"
    echo "                          The image gets priority over other"
    echo "                          images: (wallpaper, \$img)"
    echo "   --size px              Change the size of the image"
    echo "   --cropoffset value     Change the crop offset. Possible values:"
    echo "                          northwest, north, northeast, west, center"
    echo "                          east, southwest, south, southeast"
    echo
    echo "   --padding              How many spaces to pad the text"
    echo "                          to the right"
    echo "   --xoffset px           How close the image will be "
    echo "                          to the left edge of the window"
    echo "   --yoffset px           How close the image will be "
    echo "                          to the top edge of the window"
    echo "   --noimg                Disable all images"
    echo "   --nowall               Disable the wallpaper function"
    echo "                          and fallback to \$img"
    echo "   --clean                Remove all cropped images"
    echo
    echo "   Other:"
    echo "   --help                 Print this text and exit"
    echo
    exit 1
}

# }}}


# Args {{{


# Loop index
index=0

# Args
args=$@

for argument in $args; do
    index=$((index + 1))

    case $1 in
        # Info
        --title) title="$2" ;;
        --distro) os="$2" ;;
        --kernel) kernel="$2" ;;
        --uptime) uptime="$2" ;;
        --packages) packages="$2" ;;
        --shell) shell="$2" ;;
        --winman) windowmanager="$2" ;;
        --cpu) cpu="$2" ;;
        --speed) speed="$2" ;;
        --speed_type) speed_type="$2" ;;
        --memory) memory="$2" ;;
        --song) song="$2" ;;

        # Text Colors
        --colors) title_color="\033[38;5;${2}m"; \
            [ ! -z $3 ] && subtitle_color="\033[38;5;${3}m"; \
            [ ! -z $4 ] && colon_color="\033[38;5;${4}m"; \
            [ ! -z $5 ] && info_color="\033[38;5;${5}m" ;;
        --titlecol) title_color="\033[38;5;${2}m" ;;
        --subtitlecol) subtitle_color="\033[38;5;${2}m" ;;
        --coloncol) colon_color="\033[38;5;${2}m" ;;
        --infocol) info_color="\033[38;5;${2}m" ;;

        # Color Blocks
        --printcols) start=$2; end=$3 ;;
        --nopal) printcols=0 ;;

        # Image
        --image) usewall=0; img="$2" ;;
        --size) imgsize="$2" ;;
        --cropoffset) crop_offset="$2" ;;
        --padding) pad="$2" ;;
        --xoffset) xoffset="$2" ;;
        --yoffset) yoffset="$2" ;;
        --noimg) enableimages=0 ;;
        --nowall) usewall=0 ;;
        --clean) rm -rf "$imgtempdir" || exit ;;

        # Other
        --help) usage ;;
    esac

    # The check here fixes shift in sh/mksh
    [ ! -z "$1" ] && shift
done


# }}}


# Image Crop {{{


# If the script was called with --noimg, disable images and padding
if [ $enableimages -eq 1 ]; then
    # If usewall=1, Get image to display from current wallpaper.
    # (only works with feh)
    [ $usewall -eq 1 ] && \
        img=$(awk '/feh/ {printf $3}' "$HOME/.fehbg" | sed -e "s/'//g")

    # Get name of image and prefix it with it's crop offset
    imgname="$crop_offset-${img##*/}"

    # This check allows you to resize the image at launch
    if [ -f "$imgtempdir/$imgname" ]; then
        imgheight=$(identify -format "%h" "$imgtempdir/$imgname")
        [ $imgheight != $imgsize ] && rm "$imgtempdir/$imgname"
    fi

    # Check to see if the tempfile exists before we do any cropping.
    if [ ! -f "$imgtempdir/$imgname" ]; then
        # Check if the directory exists and create it if it doesn't
        [ ! -d "$imgtempdir" ] && (mkdir "$imgtempdir" || exit)

        # Get wallpaper size so that we can do a better crop
        size=($(identify -format "%w %h" $img))

        # This checks to see if height is geater than width
        # so we can do a better crop of portrait images.
        if [ ${size[1]} -gt ${size[0]} ]; then
            size=${size[0]}
        else
            size=${size[1]}
        fi

        # Crop the image and save it to  the $imgtempdir
        # By default we crop a square in the center of the image which is
        # "image height x image height".
        # We then resize it to the image size specified above.
        # (default 128x128 px, uses var $height)
        # This way we get a full image crop with the speed benefit
        # of a tiny image.
        convert \
            -crop "$size"x"$size"+0+0 \
            -gravity $crop_offset "$img" \
            -resize "$imgsize"x"$imgsize" "$imgtempdir/$imgname"
    fi

    # The final image
    img="$imgtempdir/$imgname"
else
    img=""
    pad=""
fi


# }}}


# Print Info {{{

# Get cpu speed
cpuspeed

# Get packages
[ -z $packages ] && getpackages

# Get window manager
[ -z $windowmanager ] && getwindowmanager

clear

# Underline title with length of title
underline=$(printf %"${#title}"s |tr " " "-")

# Hide the terminal cursor while we print the info
echo -n -e "\033[?25l"

# Print the title and underline
echo -e "$pad$bold$title_color$title$clear"
echo -e "$pad$colon_color$underline$clear"

# Custom echo function to make it easier to edit the info lines.
echoinfo () {
    echo -n -e "$pad$bold$subtitle_color$1$clear"
    echo -n -e "$colon_color:$clear "
    echo -e "$info_color$2$clear"
}

echoinfo "$title_os" "$os"
echoinfo "$title_kernel" "$kernel"
echoinfo "$title_uptime" "$uptime"
echoinfo "$title_packages" "$packages"
echoinfo "$title_shell" "$shell"
echoinfo "$title_windowmanager" "$windowmanager"
echoinfo "$title_cpu" "$cpu @ ${speed}GHz"
echoinfo "$title_memory" "$memory"
echoinfo "$title_song" "$song"

# Display the color blocks
[ $printcols -eq 1 ] && echo -e "$(printcols)"

# Display the image
echo -e "0;1;$xoffset;$yoffset;$imgsize;$imgsize;;;;;$img\n4;\n3;" |\
    /usr/lib/w3m/w3mimgdisplay
# Show the cursor again
echo -n -e "\033[?25h"


# }}}

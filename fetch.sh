#!/usr/bin/env bash
# Fetch info about your system
#
# Optional Dependencies: (You'll lose these features without them)
#   Displaying Images: w3m
#   Image Cropping: ImageMagick
#   Wallpaper Display: feh Window Manager Detection: wmctrl
#   Current Song: mpc
#   Text formatting, dynamic image size and padding: tput
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


# Line wrap
# Set this to 0 or use the flag "--wrap on/off" to disable
# line wrapping. Really useful for small terminal windows
# and long lines.
linewrap="on"

# Set to "", comment this line or use the flag "--bold on/off"
# to disable all bold text.
bold="on"

# Whether or not to underline the title.
# Configurable at launch with "--underline on/off"
underline="on"

# Character to underline title with
# Configurable at launch with "--underline_char char"
underline_char="-"

# Default colors
# Colors can be defined at launch with:
# "--titlecol 1, --subtitlecol 2, --coloncol 3, --infocol 4"
# Or the shorthand "-c/--color 1 2 3 4"
# Or by editing them below.
title_color=$(tput setaf 7)
subtitle_color=$(tput setaf 1)
colon_color=$(tput setaf 7) # Also changes underline color
info_color=$(tput setaf 7)

# Reset formatting
# Removing this line will fuck up the text formatting
clear=$(tput sgr0)

# Amount of left padding to use when images are disabled.
# The variable takes a count of spaces. So a value of 10
# will pad the text to the right 10 spaces.
padding=0


# }}}


# Custom Image {{{


# Enable or disable the use of images (Disable images at launch with "--images on/off")
images="on"

# If "on", fetch will use a cropped version of your wallpaper as the image
# (Disable this at launch with "--wall off")
# NOTE: This is only compatible with feh, I can add support for more
#       wallpaper setters but you'll need to show me a way to get the current
#       wallpaper from the commandline.
wall="on"

# The image to use if wall="off". There's also the launch flag "--image"
# to set a custom image at launch.
img="$HOME/Pictures/avatars/gon.png"

# Image size is based on terminal size
# Using the flag "--size" sets this to off.
img_auto="on"

# This is experimental and needs testing. ( Off by default )
# Smart crop images with plain color backgrounds.
# What this means is that your solid bg waifu wallpaper will be cropped around
# your waifu no matter where she is in the image.
smart_crop="off"

# Smart crop has two modes, fit and fill.
# Fit: Fit the whole character into the crop.
# Fill: Fit a portrait of the character into the crop.
# Fit gives the best results when the character isn't cut off at the sides.
smart_crop_mode="fit"

# Image size to use if img_auto="off"
# Also configureable at launch with "--size"
size=128

# Font width is needed to properly calulate the image size
# If there's a gap on the right try increasing the value by 1
# If there's an overlap try decreasing the value by 1
fontwidth=5

# Gap is the amount of space between the image and the text on the right
gap=4

# Image size/offset
# (Customizable at launch with these flags: --xoffset 0 --yoffset 0")
yoffset=0
xoffset=0

# Default crop offset (Customizable at launch with --cropoffset)
# Possible values:
# northwest, north, northeast, west, center, east, southwest, south, southeast
crop_offset="center"

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
if type -p crux >/dev/null 2>&1; then
    os="CRUX"
else
    os=$(awk '/^NAME=/' /etc/*ease | sed -n 's/^NAME=//p' | tr -d '"')
fi

# Linux kernel name/version (Configurable with "-K" and "--kernel" at launch)
kernel=$(uname -r)

# System Uptime (Configurable with "-U" and "--uptime" at launch)
uptime=$(uptime -p)

# Total number of packages (Configurable with "-P" and "--packages" at launch)
# If your package manager can't be found open an issue on my github repo.
# (Link is at the top)
getpackages () {
    case $os in
	'void') \
	    packages=$(xbps-query -l | wc -l) ;;
        'Arch Linux'|'Parabola GNU/Linux-libre'|'Manjaro'|'Antergos') \
            packages=$(pacman -Q | wc -l) ;;
        'Ubuntu'|'Mint'|'Debian'|'Kali Linux'|'Deepin Linux') \
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
getwindowmanager () {
    if type -p wmctrl >/dev/null 2>&1; then
        windowmanager=$(wmctrl -m | awk '/Name:/ {printf $2}')
    elif [ -e ~/.xinitrc ]; then
        windowmanager=$(grep -v "^#" "${HOME}/.xinitrc" | tail -n 1 | cut -d " " -f2)
    else
        windowmanager="Unknown"
    fi
}

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

# Memory (Configurable with "--memory" at launch)
# Print used ram / total ram
# This function checks the "free" command's version as
# version 3.3.0 changed the layout of columns.
getmemory () {
    freeversion=$(free --version | awk '{printf $4}')

    if [ ${freeversion//.} -gt 330 ] || [${freeversion//.} -gt 3300 ]; then
        memory=$(free -m | awk '/Mem:/ {printf $3 "MB / " $2 "MB"}')
    else
        usedmem=$(free -m | awk '/cache:/ {print $3}')
        totalmem=$(free -m | awk '/Mem:/ {print $2}')
        memory="${usedmem}MB / ${totalmem}MB"
    fi
}

# Currently playing song/artist (Configurable with "-m" and "--song" at launch)
if type -p mpc >/dev/null 2>&1; then
    song=$(mpc current)
else
    song="Unknown"
fi

# Print terminal colors in a line
# (Configurable with "--printcols start end" at launch)
# Start/End are vars for the range of colors to print
# The default values below print 8 colors in total.
start=0
end=7

# Print the color blocks by default.
color_blocks="on"

# Widh of the color blocks
blockwidth=3

printcols () {
    while [ "$start" -le "$end" ]; do
        printf "%s%${blockwidth}s" "$(tput setab $start)"
        start=$((start + 1))

        # Split the blocks at 8 colors
        [ $end -ge 9 ] && [ $start -eq 8 ] && printf "\n%${pad}s" "$clear$pad"
    done

    # Clear formatting
    printf %s "$clear"
}


# }}}


# Usage {{{


usage () {
    printf '%s\n'
    printf '%s\n' "usage: ${0##*/} [--colors 1 2 4 5] [--kernel \"\$(uname -rs)\"]"
    printf '%s\n'
    printf '%s\n' "   Info:"
    printf '%s\n' "   --title string         Change the title at the top"
    printf '%s\n' "   --distro string/cmd    Manually set the distro"
    printf '%s\n' "   --kernel string/cmd    Manually set the kernel"
    printf '%s\n' "   --uptime string/cmd    Manually set the uptime"
    printf '%s\n' "   --packages string/cmd  Manually set the package count"
    printf '%s\n' "   --shell string/cmd     Manually set the shell"
    printf '%s\n' "   --winman string/cmd    Manually set the window manager"
    printf '%s\n' "   --cpu string/cmd       Manually set the cpu name"
    printf '%s\n' "   --memory string/cmd    Manually set the memory"
    printf '%s\n' "   --speed string/cmd     Manually set the cpu speed"
    printf '%s\n' "   --speed_type           Change the type of cpu speed to get"
    printf '%s\n' "                          Possible values: current, min, max"
    printf '%s\n' "   --song string/cmd      Manually set the current song"
    printf '%s\n'
    printf '%s\n' "   Text Colors:"
    printf '%s\n' "   --colors 1 2 3 4       Change the color of text"
    printf '%s\n' "                          (title, subtitle, colon, info)"
    printf '%s\n' "   --titlecol num         Change the color of the title"
    printf '%s\n' "   --subtitlecol num      Change the color of the subtitle"
    printf '%s\n' "   --coloncol num         Change the color of the colons"
    printf '%s\n' "   --infocol num          Change the color of the info"
    printf '%s\n'
    printf '%s\n' "   Text Formatting:"
    printf '%s\n' "   --underline on/off     Enable/Disable title underline"
    printf '%s\n' "   --underline_char char  Character to use when underlineing title"
    printf '%s\n' "   --linewrap on/off      Enable/Disable line wrapping"
    printf '%s\n' "   --bold on/off          Enable/Disable bold text"
    printf '%s\n'
    printf '%s\n' "   Color Blocks:"
    printf '%s\n' "   --printcols start end  Range of colors to print as blocks"
    printf '%s\n' "   --blockwidth num       Width of color blocks"
    printf '%s\n' "   --color_blocks on/off  Enable/Disable the color blocks"
    printf '%s\n'
    printf '%s\n' "   Image:"
    printf '%s\n' "   --image                Image to display with the script"
    printf '%s\n' "                          The image gets priority over other"
    printf '%s\n' "                          images: (wallpaper, \$img)"
    printf '%s\n' "   --fontwidth px         Used to automatically size the image"
    printf '%s\n' "   --size px              Change the size of the image"
    printf '%s\n' "   --smart_crop on/off    Smart crop images with plain color backgrounds"
    printf '%s\n' "   --smart_crop_mode      Which mode to use with smart crop"
    printf '%s\n' "                          Takes the values: fit, fill"
    printf '%s\n' "   --img_auto on/off      Enable/Disable automatic i mage sizing"
    printf '%s\n' "   --cropoffset value     Change the crop offset. Possible values:"
    printf '%s\n' "                          northwest, north, northeast, west, center"
    printf '%s\n' "                          east, southwest, south, southeast"
    printf '%s\n'
    printf '%s\n' "   --padding num          How many spaces to pad the text"
    printf '%s\n' "                          to the right"
    printf '%s\n' "   --xoffset px           How close the image will be "
    printf '%s\n' "                          to the left edge of the window"
    printf '%s\n' "   --yoffset px           How close the image will be "
    printf '%s\n' "   --gap num              Gap between image and text right side"
    printf '%s\n' "                          to the top edge of the window"
    printf '%s\n' "   --images on/off        Enable/Disable all images"
    printf '%s\n' "   --wall on/off          Enable/Disable the wallpaper function"
    printf '%s\n' "                          and fallback to \$img"
    printf '%s\n' "   --clean                Remove all cropped images"
    printf '%s\n'
    printf '%s\n' "   Other:"
    printf '%s\n' "   --help                 Print this text and exit"
    printf '%s\n'
    exit 1
}


# }}}


# Args {{{


for argument in "$@"; do
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
        --colors) title_color="$(tput setaf $2)"; \
            [ ! -z $3 ] && subtitle_color="$(tput setaf $3)"; \
            [ ! -z $4 ] && colon_color="$(tput setaf $4)"; \
            [ ! -z $5 ] && info_color="$(tput setaf $5)" ;;
        --titlecol) title_color="$(tput setaf $2)" ;;
        --subtitlecol) subtitle_color="$(tput setaf $2)" ;;
        --coloncol) colon_color="$(tput setaf $2)" ;;
        --infocol) info_color="$(tput setaf $2)" ;;

        # Text Formatting
        --underline) underline="$2" ;;
        --underline_char) underline_char="$2" ;;
        --linewrap) linewrap="$2" ;;
        --bold) bold="$2" ;;

        # Color Blocks
        --printcols) start=$2; end=$3 ;;
        --color_blocks) color_blocks="$2" ;;

        # Image
        --image) wall="off"; img="$2" ;;
        --fontwidth) fontwidth="$2" ;;
        --size) img_auto="off" imgsize="$2" ;;
        --smart_crop) smart_crop="$2" ;;
        --smart_crop_mode) smart_crop_mode="$2" ;;
        --img_auto) img_auto="off" ;;
        --cropoffset) crop_offset="$2" ;;
        --padding) padding="$2" ;;
        --xoffset) xoffset="$2" ;;
        --yoffset) yoffset="$2" ;;
        --gap) gap="$2" ;;
        --images) images="$2" ;;
        --wall) wall="$2" ;;
        --clean) rm -rf "$imgtempdir" || exit ;;

        # Other
        --help) usage ;;
    esac

    # The check here fixes shift in sh/mksh
    [ ! -z "$1" ] && shift
done


# }}}


# Image  {{{


# If the script was called with --noimg, disable images and padding
if [ $images == "on" ]; then
    # Check to see if auto=1
    if [ $img_auto == "on" ]; then
        # Image size is half of the terminal
        imgsize=$(($(tput cols) * fontwidth / 2))

        # Padding is half the terminal width + gap
        padding=$(($(tput cols) / 2 + gap))
    fi

    # If wall=on, Get image to display from current wallpaper.
    # (only works with feh)
    [ $wall == "on" ] && \
        img=$(awk '/feh/ {printf $3}' "$HOME/.fehbg" | sed -e "s/'//g")

    # Get name of image and prefix it with it's crop offset or smart_crop mode
    if [ $smart_crop == "on" ]; then
        imgname="$smart_crop_mode-${img##*/}"
    else
        imgname="$crop_offset-${img##*/}"
    fi

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

        # Crop the image, resize it and save it to $imgtempdir.
        if [ $smart_crop == "on" ]; then
            # Fixes transparent images having a white bg after -extent
            c=$(convert "$img" -colorspace srgb -format "%[pixel:p{0,0}]" info:)

            if [ $smart_crop_mode == "fit" ]; then
                convert \
                    -trim +repage "$img"  \
                    -gravity south \
                    -background "$c" \
                    -extent "$size"x"$size" \
                    -resize "$imgsize"x"$imgsize" \
                    "$imgtempdir/$imgname"
            else
                convert \
                    -trim +repage "$img"  \
                    -resize "$imgsize"x"$imgsize"^ \
                    -background "$c" \
                    -extent "$imgsize"x"$imgsize" \
                    "$imgtempdir/$imgname"
            fi
        else
            convert \
                -crop "$size"x"$size"+0+0 \
                -gravity $crop_offset "$img" \
                -resize "$imgsize"x"$imgsize" \
                "$imgtempdir/$imgname"
        fi
    fi

    # The final image
    img="$imgtempdir/$imgname"
else
    img=""
fi


# }}}


# Print Info {{{


# Get cpu speed
[ -z $speed ] && cpuspeed

# Get packages
[ -z $packages ] && getpackages

# Get window manager
[ -z $windowmanager ] && getwindowmanager

# Get memory
[ -z $memory ] && getmemory

# Check for whether or not we bold text
[ $bold == "on" ] && b=$(tput bold)

# Padding
pad=$(printf "%${padding}s")

# Hide the terminal cursor while we print the info
tput civis

# Clear terminal before printing anything
clear

# Underline title with length of title
[ $underline == "on" ] && uline=$(printf %"${#title}"s |tr " " "$underline_char")

# Disable line wrap
[ $linewrap == "off" ] && printf '\e[?7l'

# Print the title and underline
printf "%s\n" "$pad$b$title_color$title$clear"
[ $underline == "on" ] && printf "%s\n" "$pad$colon_color$uline$clear"

# Custom printf function to make it easier to edit the info lines.
printinfo () {
    printf "$pad$b$subtitle_color$1$clear"
    printf "$colon_color:$clear "
    printf "%s\n" "$info_color$2$clear"
}

printinfo "$title_os" "$os"
printinfo "$title_kernel" "$kernel"
printinfo "$title_uptime" "$uptime"
printinfo "$title_packages" "$packages"
printinfo "$title_shell" "$shell"
printinfo "$title_windowmanager" "$windowmanager"
printinfo "$title_cpu" "$cpu @ ${speed}GHz"
printinfo "$title_memory" "$memory"
printinfo "$title_song" "$song"

# Display the color blocks
printf "\n"
[ $color_blocks == "on" ] && printf "$pad$(printcols)"

# Enable line wrap again
[ $linewrap == "off" ] && printf '\e[?7h'

# If w3mimgviewer is found Display the image
sleep .02
if type -p /usr/lib/w3m/w3mimgdisplay >/dev/null 2>&1; then
    printf "0;1;$xoffset;$yoffset;$imgsize;$imgsize;;;;;$img\n4;\n3;" |\
        /usr/lib/w3m/w3mimgdisplay
fi

# Show the cursor again
tput cnorm

# Move the cursor to the bottom of the terminal
tput cup $(tput lines)


# }}}

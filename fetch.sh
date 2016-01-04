#!/usr/bin/env bash
# Fetch info about your system
#
# Optional Dependencies: (You'll lose these features without them)
#   Displaying Images: w3m
#   Image Cropping: ImageMagick
#   Wallpaper Display: feh
#   Current Song: mpc
#   Text formatting, dynamic image size and padding: tput
#   Resolution detection: xorg-xdpyinfo
#
# Created by Dylan Araps
# https://github.com/dylanaraps/dotfiles

# Speed up script by not using unicode
export LC_ALL=C


# Config Options {{{


# Info Options {{{

# Info
# What to display and in what order.
#
# Format is: "Subtitle: function name"
# Additional lines you can use include:
# "underline" "linebreak" "echo: msg here" "title: title here"
#
# You can also include your own custom lines by using:
# "echo: subtitlehere: $(custom cmd here)"
# "echo: Custom string to print"
#
# Optional info lines that are disabled by default are:
# "getresolution" "getsong"
info=(
    "gettitle"
    "underline"
    "OS: getdistro"
    "Kernel: getkernel"
    "Uptime: getuptime"
    "Packages: getpackages"
    "Shell: getshell"
    "Window Manager: getwindowmanager"
    "CPU: getcpu"
    "Memory: getmemory"
    "linebreak"
    "getcols"
)

# CPU

# CPU speed type
# --speed_type current/min/max
speed_type="max"


# Uptime

# Shorten the output of the uptime function
uptime_shorthand="off"


# Color Blocks

# Color block range
# --block_range start end
start=0
end=7

# Toggle color blocks
# --color_blocks on/off
color_blocks="on"

# Color block width
# --color_block_width num
block_width=3


# }}}


# Text Colors {{{
# --colors 1 2 3 4 5


# --title_color num
title_color=4

# --subtitle_color num
subtitle_color=1

# --colon_color num
colon_color=8

# --underline_color num
underline_color=8

# --info_color num
info_color=6


# }}}


# Text Options {{{


# Toggle line wrapping
# --line_wrap on/off
line_wrap="on"

# Toggle bold text
# --bold on/off
bold="on"

# Toggle title underline
# --underline on/off
underline="on"

# Underline character
# --underline_char char
underline_char="-"


# }}}


# Image Options {{{


# Toggle all images
# --images on/off
images="on"

# Thumbnail directory
imgtempdir="$HOME/.fetchimages"

# Split Size
# Sizing for the img and text splits
# The larger the value the less space fetch will take up.
# The default value of 2 splits the image and text at
# half terminal width each.
# A value of 3 splits them at a third width each and etc.
# --split_size num
split_size=2

# Image position
# --image_position left/right
image_position="left"

# Use current wallpaper as the image
# --wall on/off
wall="on"

# Default image to use if wallpaper use is disabled
# --image img
img="$HOME/Pictures/avatars/gon.png"

# Crop mode
# --crop_mode normal/fit/fill
crop_mode="normal"

# Crop offset
# Only affects normal mode.
# --crop_offset northwest/north/northeast/west/center
#               east/southwest/south/southeast
crop_offset="center"

# Font width
# Used when calculating dynamic image size
font_width=5

# Right gap between image and text
# --gap num
gap=4

# Image offsets
# --xoffset px
# --yoffset px
yoffset=0
xoffset=0


# }}}


# }}}


# Gather Info {{{


# Get Operating System Type
case "$(uname)" in
    "Linux")
        os="Linux"
    ;;

    "Darwin")
        os="Mac OS X"
    ;;

    "OpenBSD")
        os="OpenBSD"
    ;;
esac

# Get Distro
getdistro () {
    case "$os" in
        "Linux" )
            if type -p crux >/dev/null 2>&1; then
                distro="CRUX"
            else
                distro="$(awk -F'=' '/^NAME=/ {printf $2; exit}' /etc/*ease)"
                distro=${distro#\"*}
                distro=${distro%*\"}
            fi
        ;;

        "Mac OS X")
            distro="Mac OS X $(sw_vers -productVersion)"
        ;;

        "OpenBSD")
            distro="OpenBSD"
        ;;

        *)
            distro="Unknown"
        ;;
    esac
}

# Get Title
gettitle () {
    title="${USER}@$(hostname)"
}

# Get kernel version
getkernel() {
    kernel="$(uname -r)"
}

# Get uptime
getuptime () {
    case "$os" in
        "Linux")
            uptime="$(uptime -p)"
        ;;

        "Mac OS X")
            # TODO: Fix uptime for OS X
            uptime="Unknown"
        ;;

        "OpenBSD")
            uptime=$(uptime | awk -F',' '{ print $1 }')
            uptime=${uptime# }
        ;;

        *)
            uptime="Unknown"
        ;;

    esac

    if [ "$uptime_shorthand" == "on" ]; then
        uptime=${uptime/up/}
        uptime=${uptime/minutes/mins}
        uptime=${uptime# }
    fi
}

# Get package count
getpackages () {
    case "$distro" in
        "Arch Linux"|"Parabola GNU/Linux-libre"|"Manjaro"|"Antergos")
            packages="$(pacman -Q | wc -l)"
        ;;

        "void")
            packages="$(xbps-query -l | wc -l)"
        ;;

        "Ubuntu"|"Mint"|"Debian"|"Kali Linux"|"Deepin Linux")
            packages="$(dpkg --get-selections | grep -v deinstall$ | wc -l)"
        ;;

        "Slackware")
            packages="$(ls -1 /var/log/packages | wc -l)"
        ;;

        "Gentoo"|"Funtoo")
            packages="$(ls -d /var/db/pkg/*/* | wc -l)"
        ;;

        "Fedora"|"openSUSE"|"Red Hat Enterprise Linux"|"CentOS")
            packages="$(rpm -qa | wc -l)"
        ;;

        "CRUX")
            packages="$(pkginfo -i | wc -l)"
        ;;

        "Mac OS X"*)
            packages="$(pkgutil --pkgs | wc -l)"
            packages=${packages//[[:blank:]]/}
        ;;

        "OpenBSD")
            packages=$(pkg_info | wc -l)
        ;;

        *)
            packages="Unknown"
        ;;
    esac
}

# Get shell
getshell () {
    shell="$SHELL"
}

# Get window manager
getwindowmanager () {
    if [ ! -z "${XDG_CURRENT_DESKTOP}" ]; then
        windowmanager="${XDG_CURRENT_DESKTOP}"
    elif [ -e "$HOME/.xinitrc" ]; then
        xinitrc=$(awk '/^[^#]*exec/ {print $2}' "${HOME}/.xinitrc")
        windowmanager="${xinitrc/-session/}"
    else
        case "$os" in
            "Mac OS X")
                windowmanager="Quartz Compositor"
            ;;

            *)
                windowmanager="Unknown"
            ;;

        esac
    fi
}

# Get cpu
getcpu () {
    case "$os" in
        "Linux")
            cpu="$(awk -F ': ' '/model name/ {printf $2; exit}' /proc/cpuinfo)"

            # We're using lscpu because /proc/cpuinfo doesn't have min/max speed.
            case $speed_type in
                current) speed="$(lscpu | awk '/CPU MHz:/ {printf $3}')" ;;
                min) speed="$(lscpu | awk '/CPU min MHz:/ {printf $4}')" ;;
                max) speed="$(lscpu | awk '/CPU max MHz:/ {printf $4}')" ;;
            esac

            # Convert mhz to ghz without bc
            speed=$((${speed/.*/} / 100))
            speed=${speed:0:1}.${speed:1}
            cpu="$cpu @ ${speed}GHz"
        ;;

        "Mac OS X")
            cpu="$(sysctl -n machdep.cpu.brand_string)"
        ;;

        "OpenBSD")
            cpu="$(sysctl -n hw.model)"
        ;;

        *)
            cpu="Unknown"
        ;;
    esac

    # Remove uneeded patterns from cpu output
    # This is faster than sed/gsub
    cpu=${cpu//(tm)/}
    cpu=${cpu//(TM)/}
    cpu=${cpu//(r)/}
    cpu=${cpu//(R)/}
    cpu=${cpu// CPU/}
    cpu=${cpu// Processor/}
    cpu=${cpu// Six-Core/}
}

# Get memory
getmemory () {
    case "$os" in
        "Linux")
            mem="$(awk 'NR < 4 {printf $2 " "}' /proc/meminfo)"

            # Split the string above into 3 vars
            # This is faster than using an array.
            set $mem

            memtotal=$1
            memfree=$2
            memavail=$3
            memused="$((memtotal - memavail))"
            memory="$(( ${memused%% *} / 1024))MB / $(( ${memtotal%% *} / 1024))MB"
        ;;

        "Mac OS X")
            memtotal=$(printf "%s\n" "$(sysctl -n hw.memsize)"/1024^2 | bc)
            memwired=$(vm_stat | awk '/wired/ { print $4 }')
            memactive=$(vm_stat | awk '/active / { print $3 }')
            memcompressed=$(vm_stat | awk '/occupied/ { print $5 }')
            memused=$(((${memwired//.} + ${memactive//.} + ${memcompressed//.}) * 4 / 1024))
            memory="${memused}MB / ${memtotal}MB"
        ;;

        "OpenBSD")
            memtotal=$(dmesg | awk '/real mem/ {printf $5}')
            memused=$(top -1 1 | awk '/Real:/ {print $3}')
            memtotal=${memtotal/()MB/}
            memused=${memused/M/}
            memory="${memused}MB / ${memtotal}MB"
        ;;

        *)
            memory="Unknown"
        ;;
    esac
}

# Get song
getsong () {
    song=$(mpc current 2>/dev/null || printf "%s" "Unknown")
}

# Get Resolution
getresolution () {
    case "$os" in
        "Linux"|"OpenBSD")
            resolution=$(xdpyinfo | awk '/dimensions:/ {printf $2}')
        ;;

        "Mac OS X")
            resolution=$(system_profiler SPDisplaysDataType | awk '/Resolution:/ {print $2"x"$4" "}')
        ;;

        *)
            resolution="Unknown"
        ;;
    esac

}

getcols () {
    if [ "$color_blocks" == "on" ]; then
        printf "%s" "${padding}"
        while [ $start -le $end ]; do
            printf "%s%${block_width}s" "$(tput setab $start)"
            start=$((start + 1))

            # Split the blocks at 8 colors
            [ $end -ge 9 ] && [ $start -eq 8 ] && \
                printf "\n%s" "${clear}${padding}"
        done

        # Clear formatting
        printf "%s" "$clear"
    fi
}


# }}}


# Images {{{


getimage () {
    # Check if the directory exists
    [ ! -d "$imgtempdir" ] && (mkdir "$imgtempdir" || exit)

    # Get columns
    columns=$(tput cols)

    # Image size is half of the terminal
    imgsize=$((columns * font_width / split_size))

    # Where to draw the image
    case "$image_position" in
        "left")
            # Padding is half the terminal width + gap
            padding="$(tput cuf $((columns / split_size + gap)))"
        ;;

        "right")
            padding=$(tput cuf 0)
            xoffset=$((columns * font_width / split_size - gap))
        ;;
    esac

    # If wall=on, Get image to display from current wallpaper.
    if [ "$wall" == "on" ]; then
        img=$(awk '/feh/ {printf $3}' "$HOME/.fehbg")
        img=${img#\'*}
        img=${img%*\'}
    fi

    # Get name of image and prefix it with it's crop mode and offset
    imgname="$crop_mode-$crop_offset-${img##*/}"

    # This check allows you to resize the image at launch
    if [ -f "$imgtempdir/$imgname" ]; then
        imgheight=$(identify -format "%h" "$imgtempdir/$imgname")
        [ $imgheight != $imgsize ] && rm "$imgtempdir/$imgname"
    fi

    # Check to see if the thumbnail exists before we do any cropping.
    if [ ! -f "$imgtempdir/$imgname" ]; then
        # Get image size so that we can do a better crop
        size=$(identify -format "%w %h" $img)
        width=${size%% *}
        height=${size##* }

        # This checks to see if height is geater than width
        # so we can do a better crop of portrait images.
        if [ $height -gt $width ]; then
            size=$width
        else
            size=$height
        fi

        case "$crop_mode" in
            fit)
                c=$(convert "$img" -colorspace srgb -format "%[pixel:p{0,0}]" info:)
                convert \
                    "$img" \
                    -trim +repage \
                    -gravity south \
                    -background "$c" \
                    -extent "$size"x"$size" \
                    -scale "$imgsize"x"$imgsize" \
                    "$imgtempdir/$imgname"
            ;;

            fill)
                c=$(convert "$img" -colorspace srgb -format "%[pixel:p{0,0}]" info:)
                convert \
                    "$img" \
                    -trim +repage \
                    -scale "$imgsize"x"$imgsize"^ \
                    -background "$c" \
                    -extent "$imgsize"x"$imgsize" \
                    "$imgtempdir/$imgname"
            ;;

            *)
                convert \
                    "$img" \
                    -gravity $crop_offset \
                    -crop "$size"x"$size"+0+0 \
                    -scale "$imgsize"x"$imgsize" \
                    "$imgtempdir/$imgname"
            ;;

        esac
    fi

    # The final image
    img="$imgtempdir/$imgname"
}


# }}}


# Text Formatting {{{


underline () {
    uline=$(printf %"$length"s)
    uline=${uline// /$underline_char}
}

colors () {
    title_color="$(tput setaf $title_color)"
    subtitle_color="$(tput setaf $subtitle_color)"
    colon_color="$(tput setaf $colon_color)"
    underline_color="$(tput setaf $underline_color)"
    info_color="$(tput setaf $info_color)"
}

bold () {
    if [ "$bold" == "on" ]; then
        bold="$(tput bold)"
    else
        bold=""
    fi
}

clear="$(tput sgr0)"


# }}}


# Usage {{{


usage () {
    printf "%s\n"
    printf "%s\n" "usage: ${0##*/} [--colors 1 2 4 5] [--kernel \"\$(uname -rs)\"]"
    printf "%s\n"
    printf "%s\n" "   Info:"
    printf "%s\n" "   --title string         Change the title at the top"
    printf "%s\n" "   --distro string/cmd    Manually set the distro"
    printf "%s\n" "   --kernel string/cmd    Manually set the kernel"
    printf "%s\n" "   --uptime string/cmd    Manually set the uptime"
    printf "%s\n" "   --uptime_shorthand on/off --v"
    printf "%s\n" "                          Shorten the output of uptime"
    printf "%s\n" "   --packages string/cmd  Manually set the package count"
    printf "%s\n" "   --shell string/cmd     Manually set the shell"
    printf "%s\n" "   --winman string/cmd    Manually set the window manager"
    printf "%s\n" "   --cpu string/cmd       Manually set the cpu name"
    printf "%s\n" "   --memory string/cmd    Manually set the memory"
    printf "%s\n" "   --speed_type           Change the type of cpu speed to get"
    printf "%s\n" "                          Possible values: current, min, max"
    printf "%s\n" "   --song string/cmd      Manually set the current song"
    printf "%s\n"
    printf "%s\n" "   Text Colors:"
    printf "%s\n" "   --colors 1 2 3 4 5     Change the color of text"
    printf "%s\n" "                          (title, subtitle, colon, underline, info)"
    printf "%s\n" "   --title_color num      Change the color of the title"
    printf "%s\n" "   --subtitle_color num   Change the color of the subtitle"
    printf "%s\n" "   --colon_color num      Change the color of the colons"
    printf "%s\n" "   --underline_color num  Change the color of the underlines"
    printf "%s\n" "   --info_color num       Change the color of the info"
    printf "%s\n"
    printf "%s\n" "   Text Formatting:"
    printf "%s\n" "   --underline on/off     Enable/Disable title underline"
    printf "%s\n" "   --underline_char char  Character to use when underlineing title"
    printf "%s\n" "   --line_wrap on/off      Enable/Disable line wrapping"
    printf "%s\n" "   --bold on/off          Enable/Disable bold text"
    printf "%s\n"
    printf "%s\n" "   Color Blocks:"
    printf "%s\n" "   --color_blocks on/off  Enable/Disable the color blocks"
    printf "%s\n" "   --block_width num      Width of color blocks"
    printf "%s\n" "   --block_range start end --v  "
    printf "%s\n" "                          Range of colors to print as blocks"
    printf "%s\n"
    printf "%s\n" "   Image:"
    printf "%s\n" "   --image                Image to display with the script"
    printf "%s\n" "                          The image gets priority over other"
    printf "%s\n" "                          images: (wallpaper, \$img)"
    printf "%s\n" "   --font_width px        Used to automatically size the image"
    printf "&s\n" "   --image_position       Where to display the image: (Left/Right)"
    printf "%s\n" "   --split_size num       Width of img/text splits"
    printf "%s\n" "                          A value of 2 makes each split half the terminal"
    printf "%s\n" "                          width and etc"
    printf "%s\n" "   --crop_mode            Which crop mode to use"
    printf "%s\n" "                          Takes the values: normal, fit, fill"
    printf "%s\n" "   --crop_offset value    Change the crop offset for normal mode."
    printf "%s\n" "                          Possible values: northwest, north, northeast,"
    printf "%s\n" "                          west, center, east, southwest, south, southeast"
    printf "%s\n"
    printf "%s\n" "   --xoffset px           How close the image will be "
    printf "%s\n" "                          to the left edge of the window"
    printf "%s\n" "   --yoffset px           How close the image will be "
    printf "%s\n" "                          to the top edge of the window"
    printf "%s\n" "   --gap num              Gap between image and text right side"
    printf "%s\n" "                          to the top edge of the window"
    printf "%s\n" "   --images on/off        Enable/Disable all images"
    printf "%s\n" "   --wall on/off          Enable/Disable the wallpaper function"
    printf "%s\n" "                          and fallback to \$img"
    printf "%s\n" "   --clean                Remove all cropped images"
    printf "%s\n"
    printf "%s\n" "   Other:"
    printf "%s\n" "   --help                 Print this text and exit"
    printf "%s\n"
    exit 1
}


# }}}


# Args {{{


while [ ! -z "$1" ]; do
    case $1 in
        # Info
        --title) title="$2" ;;
        --os) os="$2" ;;
        --kernel) kernel="$2" ;;
        --uptime) uptime="$2" ;;
        --uptime_shorthand) uptime_shorthand="$2" ;;
        --packages) packages="$2" ;;
        --shell) shell="$2" ;;
        --winman) windowmanager="$2" ;;
        --cpu) cpu="$2" ;;
        --speed_type) speed_type="$2" ;;
        --memory) memory="$2" ;;
        --song) song="$2" ;;

        # Text Colors
        --colors) title_color=$2; \
            [ ! -z $3 ] && subtitle_color=$3; \
            [ ! -z $4 ] && colon_color=$4; \
            [ ! -z $4 ] && underline_color=$5; \
            [ ! -z $5 ] && info_color=$6 ;;
        --title_color) title_color=$2 ;;
        --subtitle_color) subtitle_color=$2 ;;
        --colon_color) colon_color=$2 ;;
        --underline_color) underline_color=$2 ;;
        --info_color) info_color=$2 ;;

        # Text Formatting
        --underline) underline="$2" ;;
        --underline_char) underline_char="$2" ;;
        --line_wrap) line_wrap="$2" ;;
        --bold) bold="$2" ;;

        # Color Blocks
        --color_blocks) color_blocks="$2" ;;
        --block_range) start=$2; end=$3 ;;
        --block_width) block_width="$2" ;;

        # Image
        --image) wall="off"; img="$2" ;;
        --font_width) font_width="$2" ;;
        --image_position) image_position="$2" ;;
        --split_size) split_size="$2" ;;
        --crop_mode) crop_mode="$2" ;;
        --crop_offset) crop_offset="$2" ;;
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


# Print Info {{{


printinfo () {
    for info in "${info[@]}"; do
        function=${info#*: }
        subtitle=${info%:*}

        case "$info" in
            echo:*:*)
                info=${function#*: }
                subtitle=${function/:*/}
                string="${bold}${subtitle_color}${subtitle}${clear}${colon_color}: ${info_color}${info}"
                length=${#function}
            ;;

            echo:*)
                string="${info_color}${function}"
                length=${#function}
            ;;

            title:*)
                string="${bold}${title_color}${function}"
                length=${#function}
            ;;

            linebreak)
                string=""
            ;;

            underline)
                if [ "$underline" == "on" ]; then
                    underline
                    string="${underline_color}${uline}"
                fi
            ;;

            *:*|*)
                # Update the var
                var=${function/get/}
                typeset -n output=$var

                # Call the function
                [ -z "$output" ] && $function
            ;;&

            gettitle)
                string="${bold}${title_color}${output}"
                length=${#output}
            ;;

            *:*)
                string="${bold}${subtitle_color}${subtitle}${clear}${colon_color}: ${info_color}${output}"
                length=$((${#subtitle} +  ${#output} + 2))
            ;;

            *)
                string="$output"
                length=${#output}
            ;;

        esac

        printf "%s\n" "${padding}${string}${clear}"
    done
}


# }}}


# Call Functions and Finish Up {{{


# Get image
[ "$images" == "on" ] && getimage

# Hide the terminal cursor
tput civis

# Clear the terminal
clear

# Disable line wrap
[ $line_wrap == "off" ] && printf '\e[?7l'

# Call functions and display info
colors
bold
printinfo

# Display the image
[ "$images" == "on" ] && printf "0;1;$xoffset;$yoffset;$imgsize;$imgsize;;;;;$img\n4;\n3;" |\
    /usr/lib/w3m/w3mimgdisplay

# Enable line wrap again
[ $line_wrap == "off" ] && printf '\e[?7h'

# Move cursor to bottom and redisplay it.
printf "cup $(tput lines) \n cuu1 \n cnorm" | tput -S


# }}}



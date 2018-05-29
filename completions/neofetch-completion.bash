#!/usr/bin/env bash
#
# Shell completion for neofetch.

_neofetch_completions() {
    local flags cur prev usage config

    usage="$(neofetch --help)"
    config="$(neofetch --print_config)"

    # User input.
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Generate a list of flags.
    IFS=$'\n' read -d "" -ra flags < <(awk '/^    --/{print $1}' <<< "$usage")

    # Complete partial matches.
    IFS=$'\n' read -d "" -ra COMPREPLY < <(compgen -W "${flags[*]}" -- "$cur")

    case "$prev" in
        "--disable")
            conf="${HOME}/.config/neofetch/config.conf"

            [[ -f "$conf" ]] &&
                IFS=$'\n' read -d "" -ra COMPREPLY \
                    < <(awk '/  info /&&!a[$0]++{print $NF}' "$conf")
        ;;

        "--backend")
            IFS=$'\n' read -d "" -ra COMPREPLY \
                < <(awk -F\' '/ Shortcut/ {print $2}' <<< "$usage")
        ;;

        "--os_arch"|\
        "--speed_shorthand"|\
        "--cpu_brand"|\
        "--cpu_speed"|\
        "--distro_shorthand"|\
        "--kernel_shorthand"|\
        "--uptime_shorthand"|\
        "--refresh_rate"|\
        "--gpu_brand"|\
        "--gtk_shorthand"|\
        "--gtk2"|\
        "--gtk3"|\
        "--shell_path"|\
        "--shell_version"|\
        "--song_shorthand"|\
        "--install_time"|\
        "--underline"|\
        "--bold"|\
        "--color_blocks"|\
        "--bar_border"|\
        "--ascii_bold")
            COMPREPLY=(
                "on"
                "off"
            )
        ;;

        "--speed_type")
            COMPREPLY=(
                "current"
                "min"
                "max"
                "bios"
                "scaling_current"
                "scaling_min"
                "scaling_max"
            )
        ;;

        "--cpu_cores")
            COMPREPLY=(
                "logical"
                "physical"
                "off"
            )
        ;;

        "--cpu_temp")
            COMPREPLY=(
                "C"
                "F"
                "off"
            )
        ;;

        "--gpu_type")
            COMPREPLY=(
                "all"
                "dedicated"
                "integrated"
            )
        ;;

        "--disk_show")
            COMPREPLY=(
                "/dev/sd"*
                "/"
            )
        ;;

        "--disk_subtitle")
            COMPREPLY=(
                "name"
                "mount"
                "dir"
            )
        ;;

        "--ip_host")
            COMPREPLY=(
                "http://ident.me"
            )
        ;;

        "--song_format")
            COMPREPLY=(
                "\"%artist% - %album% - %title%\""
                "\"%artist - %title\""
            )
        ;;

        "--music_player")
            COMPREPLY=(
                "amarok"
                "audacious"
                "banshee"
                "bluemindo"
                "clementine"
                "cmus"
                "deadbeef"
                "deepin-music"
                "elisa"
                "exaile"
                "gnome-music"
                "Google Play"
                "guayadeque"
                "iTunes"
                "juk"
                "lollypop"
                "mocp"
                "mopidy"
                "mpd"
                "pogo"
                "pragha"
                "qmmp"
                "quodlibet"
                "rhythmbox"
                "sayonara"
                "spotify"
                "Spotify"
                "tomahawk"
                "vlc"
                "xmms2d"
                "yarock"
            )
        ;;

        "--install_time_format")
            COMPREPLY=(
                "12h"
                "24h"
            )
        ;;

        "--underline_char")
            COMPREPLY=(
                "_"
                "-"
                "."
                "⎯"
                "―"
            )
        ;;

        "--block_width"|\
        "--block_height"|\
        "--bar_length")
            COMPREPLY=(
                {1..9}
            )
        ;;
    esac
}

complete -F _neofetch_completions neofetch

#!/usr/bin/env bash
#
# Shell completion for neofetch.
shopt -s nullglob

_neofetch_completions() {
    local cur prev

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    IFS=$'\n' read -d "" -ra COMPREPLY \
        < <(compgen -W "$(neofetch -h | awk '/  --/{printf $1" "}')" -- "$cur")

    case "$prev" in
        "--disable")
            conf="${HOME}/.config/neofetch/config.conf"

            [[ -f "$conf" ]] &&
                IFS=$'\n' read -d "" -ra COMPREPLY \
                    < <(awk '/  info /&&!a[$0]++{print $NF}' "$conf")
        ;;

        "--backend")
            COMPREPLY=(
                "ascii"
                "caca"
                "iterm2"
                "jp2a"
                "kitty"
                "pixterm"
                "sixel"
                "termpix"
                "tycat"
                "w3m"
                "off"
            )
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

        "--cpu_display"|\
        "--memory_display"|\
        "--battery_display"|\
        "--disk_display")
            COMPREPLY=(
                "bar"
                "infobar"
                "barinfo"
                "off"
            )
        ;;

        "--source"|\
        "--ascii"|\
        "--caca"|\
        "--iterm2"|\
        "--jp2a"|\
        "--kitty"|\
        "--pixterm"|\
        "--sixel"|\
        "--termpix"|\
        "--tycat"|\
        "--w3m")
            COMPREPLY=(
                "auto"
                "ascii"
                "wallpaper"
                "/path/to/img.jpg"
                "/path/to/images"
                "/path/to/ascii_file"
            )

        ;;

        "--ascii_distro")
            COMPREPLY=(
                "aix"
                "alpine"
                "alpine_small"
                "amazon"
                "anarchy"
                "android"
                "antergos"
                "antix"
                "aosc"
                "apricity"
                "arch"
                "arch_old"
                "arch_small"
                "archbox"
                "archlabs"
                "archmerge"
                "arcolinux"
                "artix"
                "arya"
                "bitrig"
                "blag"
                "blankon"
                "bsd"
                "bunsenlabs"
                "calculate"
                "centos"
                "chakra"
                "chaletos"
                "chapeau"
                "chrom"
                "clover"
                "crux"
                "crux_small"
                "darwin"
                "debian"
                "debian_small"
                "deepin"
                "desaos"
                "devuan"
                "dracos"
                "dragonfly"
                "dragonfly_old"
                "dragonfly_small"
                "elementary"
                "endless"
                "exherbo"
                "fedora"
                "freebsd"
                "freebsd_small"
                "freemint"
                "frugalware"
                "funtoo"
                "galliumos"
                "gentoo"
                "gentoo_small"
                "gnewsense"
                "gnu"
                "gobolinux"
                "grombyang"
                "guixsd"
                "haiku"
                "hyperbola"
                "irix"
                "kali"
                "kaos"
                "kde"
                "kogaion"
                "korora"
                "kslinux"
                "kubuntu"
                "lede"
                "linux"
                "linux mint"
                "lmde"
                "lubuntu"
                "lunar"
                "mac"
                "mageia"
                "magpieos"
                "manjaro"
                "maui"
                "mer"
                "minix"
                "mx"
                "netbsd"
                "netrunner"
                "nitrux"
                "nixos"
                "nixos_small"
                "nurunner"
                "nutyx"
                "obrevenge"
                "open source media center"
                "openbsd"
                "openbsd_small"
                "openindiana"
                "openmandriva"
                "opensuse"
                "openwrt"
                "oracle"
                "pacbsd"
                "parabola"
                "pardus"
                "parrot"
                "parsix"
                "pcbsd"
                "pclinuxos"
                "peppermint"
                "porteus"
                "postmarketos"
                "puppy"
                "qubes"
                "raspbian"
                "red star"
                "redcore"
                "redhat"
                "rosa"
                "sabayon"
                "sabotage"
                "sailfishos"
                "salentos"
                "scientific"
                "siduction"
                "slackware"
                "slitaz"
                "smartos"
                "solus"
                "sparky"
                "steamos"
                "sunos"
                "swagarch"
                "tails"
                "trisquel"
                "ubuntu"
                "ubuntu_old"
                "void"
                "void_small"
                "windows"
                "windows 10"
                "xferience"
                "xubuntu"
                "zorin"
            )
        ;;

        "--size")
            COMPREPLY=(
               "00px"
               "00%"
               "auto"
               "none"
            )
        ;;

        "--crop_mode")
            COMPREPLY=(
               "normal"
               "fit"
               "fill"
            )
        ;;

        "--crop_offset")
            COMPREPLY=(
                "northwest"
                "north"
                "northeast"
                "west"
                "center"
                "east"
                "southwest"
                "south"
                "southeast"
            )
        ;;

        "--config")
            COMPREPLY=(
               "none"
               "/path/to/config"
            )
        ;;
    esac
}

complete -F _neofetch_completions neofetch

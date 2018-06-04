#!/usr/bin/env bash
#
# Shell completion for neofetch.
shopt -s nullglob

_neofetch_completions() {
    local cur prev usage

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    if [[ "$cur" == -* ]]; then
        usage="$(neofetch -h | awk '/^    --/{printf $1" "}')"

        IFS=$'\n' read -d "" -ra COMPREPLY \
            < <(compgen -W "$usage" -- "$cur")

    else
        case "$prev" in
            "--disable")
                conf="${HOME}/.config/neofetch/config.conf"

                [[ -f "$conf" ]] &&
                    IFS=$'\n' read -d "" -ra values \
                        < <(awk '/  info /&&!a[$0]++{print $NF}' "$conf")
            ;;

            "--backend")
                values=(
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
            "--kernel_shorthand"|\
            "--refresh_rate"|\
            "--gpu_brand"|\
            "--gtk_shorthand"|\
            "--gtk2"|\
            "--gtk3"|\
            "--shell_path"|\
            "--shell_version"|\
            "--song_shorthand"|\
            "--underline"|\
            "--bold"|\
            "--color_blocks"|\
            "--bar_border"|\
            "--ascii_bold")
                values=(
                    "on"
                    "off"
                )
            ;;

            "--uptime_shorthand"|\
            "--package_managers"|\
            "--distro_shorthand")
                values=(
                    "on"
                    "tiny"
                    "off"
                )
            ;;

            "--speed_type")
                values=(
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
                values=(
                    "logical"
                    "physical"
                    "off"
                )
            ;;

            "--cpu_temp")
                values=(
                    "C"
                    "F"
                    "off"
                )
            ;;

            "--gpu_type")
                values=(
                    "all"
                    "dedicated"
                    "integrated"
                )
            ;;

            "--disk_show")
                values=(
                    "/dev/sd"*
                    "/"
                )
            ;;

            "--disk_subtitle")
                values=(
                    "name"
                    "mount"
                    "dir"
                )
            ;;

            "--ip_host")
                values=(
                    "http://ident.me"
                )
            ;;

            "--song_format")
                values=(
                    "\"%artist% - %album% - %title%\""
                    "\"%artist - %title\""
                )
            ;;

            "--music_player")
                values=(
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
                    "gmusicbrowser"
                    "gnome-music"
                    "gmusicbrowser"
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
                values=(
                    "12h"
                    "24h"
                )
            ;;

            "--underline_char")
                values=(
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
                values=(
                    {1..9}
                )
            ;;

            "--cpu_display"|\
            "--memory_display"|\
            "--battery_display"|\
            "--disk_display")
                values=(
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
                values=(
                    "auto"
                    "ascii"
                    "wallpaper"
                    "/path/to/img.jpg"
                    "/path/to/images"
                    "/path/to/ascii_file"
                )

            ;;

            "--ascii_distro")
                values=(
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
                    "condres"
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
                    "kibojoe"
                    "kogaion"
                    "korora"
                    "kslinux"
                    "kubuntu"
                    "lede"
                    "linux lite"
                    "linux mint"
                    "linux"
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
                    "pureos"
                    "qubes"
                    "raspbian"
                    "red star"
                    "redcore"
                    "redcore"
                    "redhat"
                    "regata"
                    "rosa"
                    "sabayon"
                    "sabotage"
                    "sailfishos"
                    "salentos"
                    "scientific"
                    "sharklinux"
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
                    "windows 10"
                    "windows"
                    "xferience"
                    "xubuntu"
                    "zorin"
                )
            ;;

            "--size")
                values=(
                   "00px"
                   "00%"
                   "auto"
                   "none"
                )
            ;;

            "--crop_mode")
                values=(
                   "normal"
                   "fit"
                   "fill"
                )
            ;;

            "--crop_offset")
                values=(
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
                values=(
                   "none"
                   "/path/to/config"
                )
            ;;
        esac

        IFS=$'\n' read -d "" -ra COMPREPLY \
            < <(compgen -W "${values[*]}" -- "$cur")
    fi
}

complete -F _neofetch_completions neofetch

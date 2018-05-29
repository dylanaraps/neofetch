#!/usr/bin/env bash
#
# Shell completion for neofetch.

_neofetch_completions() {
    local flags cur prev usage

    usage="$(neofetch --help)"

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
            COMPREPLY=("on" "off")
        ;;
    esac
}

complete -F _neofetch_completions neofetch

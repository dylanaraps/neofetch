#!/usr/bin/env bash
#
# Shell completion for neofetch.

_neofetch_completions() {
    local flags cur prev

    # User input.
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Generate a list of flags.
    IFS=$'\n' read -d "" -ra flags \
        < <(neofetch --help | awk '/^    --/{print $1}')

    # Complete partial matches.
    IFS=$'\n' read -d "" -ra COMPREPLY \
        < <(compgen -W "${flags[*]}" -- "$cur")


    case "$prev" in
        "--disable")
            conf="${HOME}/.config/neofetch/config.conf"

            [[ -f "$conf" ]] &&
                IFS=$'\n' read -d "" -ra COMPREPLY \
                    < <(awk '/  info /&&!a[$0]++{print $NF}' "$conf")
        ;;

        "--backend")
            IFS=$'\n' read -d "" -ra COMPREPLY \
                < <(neofetch --help | awk -F\' '/ Shortcut/ {print $2}')
        ;;
    esac
}

complete -F _neofetch_completions neofetch

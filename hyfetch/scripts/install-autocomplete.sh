#!/usr/bin/env bash

# Usage: ./install-autocomplete.sh [Uninstall]
if [[ "$1" == "uninstall" ]]; then
    uninstall=true
    echo -n "Uninstalling "
else
    echo -n "Installing "
fi
echo "autocomplete scripts for HyFetch..."

# Stop on error
set -e

# Obtain path of the current bash script
script_path="$(dirname "$(realpath "$0")")"

# Installing for a specific shell in a specific directory if it exists
install-for()
{
    shell=$1
    dir=$2

    case $shell in
        bash)
            filename="hyfetch"
            ;;
        zsh)
            filename="_hyfetch"
            ;;
        csh)
            filename="hyfetch.completion.csh"
            ;;
        *)
            echo "Unknown shell: $shell"
            exit 1
            ;;
    esac

    if [[ -d "$dir" ]]; then
        if [[ "$uninstall" ]]; then
            rm -f "$dir/$filename"
            echo "⭐ Uninstalled for $shell in $dir"
        else
            cp "$script_path/autocomplete.$shell" "$dir/$filename"
            echo "⭐ Installed for $shell in $dir"
        fi
    fi
}

# Copy files
install-for bash /etc/bash_completion.d
install-for bash /usr/share/bash-completion/completions

install-for zsh /usr/share/zsh/functions/Completion/Unix
install-for zsh /usr/share/zsh/site-functions
install-for zsh /usr/share/zsh-completions
install-for zsh /usr/local/share/zsh/site-functions

install-for csh /etc/profile.d

echo "Done!"

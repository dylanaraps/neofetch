## Contributors


## IRC

Neofetch now has an irc channel at `##neofetch` on Freenode. If you have any questions, issues or ideas feel free to join the irc channel and I'll be happy to assist you. I know that we've already got the gitter chat but hopefully this makes things easier for those without a github account. :)

**NOTE:** I've applied for `#neofetch` so we'll be using `##neofetch` in the meantime.

## General

- Travis now runs [shellcheck](https://github.com/koalaman/shellcheck) on every commit and pull request.
    - We've had to exclude around 10 lint errors, see this wiki page for why we did this:
    - https://github.com/dylanaraps/neofetch/wiki/Shellcheck-Exclusions
- Optimize usage of get_de(), get_wm() and get_term().
    - We were calling these multiple times, we now check to see if they were run previously.


## Images

- [iTerm2] Fixed blank images.

## Ascii

- Fixed bug causing macOS ascii art to be used on other Operating Systems.

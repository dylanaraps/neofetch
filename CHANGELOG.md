## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**


## IRC

Neofetch now has an irc channel at `#neofetch` on Freenode. If you have any questions, issues or ideas feel free to join the irc channel and I'll be happy to assist you. I know that we've already got the gitter chat but hopefully this makes things easier for those without a github account. :)

[![Freenode](https://img.shields.io/badge/%23neofetch-%20on%20Freenode-brightgreen.svg)](http://irc.lc/freenode/neofetch)


## General

- Travis now runs [shellcheck](https://github.com/koalaman/shellcheck) on every commit and pull request.
    - We've had to exclude around 10 lint errors, see this wiki page for why we did this:
    - https://github.com/dylanaraps/neofetch/wiki/Shellcheck-Exclusions
- Optimize usage of get_de(), get_wm() and get_term().
    - We were calling these multiple times, we now check to see if they were run previously.
- Optimize info caching, only check for cache files in scripts that use caching.
- Cleanup `main()`.
- Renamed `old_flags()` --> `old_options()`.
- The manpage is now generated using `help2man`. `help2man` parses the output of `--help` and `--version` to create a manpage. This ensures that our manpage stays 1:1 with the script documentation. We actually found a lot of outdated info in the old manpage thanks to this.
    - A new flag was added called `--gen-man` which generates a neofetch manpage in your current directory.
- Delete most of `info()` and instead call `prin()`.
    - This removes a lot of duplicate code between `info()` and `prin()`.


## Info

**Shell**<br \>

- [Fish] Fixed memory leak caused by Fish.
- Added support for `xonsh`.
- Fixed version output on `ksh`.
- Rewrote the function to remove duplicate code. All shells now use `$SHELL --version` to get the version info, with the exception of `mksh` which doesn't have a `--version` flag.

**Uptime**<br \>

- Moved duplicate code to a function.
- Changed `$uptime_shorthand` to `on` by default.

**Desktop Environment**<br \>

- Fixed issues where MATE wouldn't be detected properly.
- Added fallback to `$DESKTOP_SESSION`, `$MATE_DESKTOP_SESSION_ID` and `$GNOME_DESKTOP_SESSION_ID`.

**CPU**<br \>

- [Linux] Don't simplify `cpufreq` speed option names for no reason.
- [Linux] Fixed issues with CPU name detection for architectures other than x86/amd64/ARM.
- [NetBSD] Remove case statement in favor of 1 line test.
- Remove case sensitive substitutions.
    - We match everything case insensitively so they were pointless.
- Simplify check for low CPU speeds.

**CPU Usage**<br \>

- Added Haiku cores command.
- Updated Linux and macOS commands to the match the commands in the `get_cpu()` function.

**Disk**<br \>

- Warn the user if `df` isn't installed.
- Fixed broken output if `df` wasn't installed but the function was enabled.

**Song**<br \>

- Simplify state detection.
- [cmus] Simplify block and fix `artistsort` bug

**Battery**<br \>

- [MacOS] Fixed issue where battery always appears as charging. **[@jorgegonzalez](https://github.com/jorgegonzalez)**

**Color Blocks**<br \>

- Use start++ instead of adding it manually after case. **[@konimex](https://github.com/konimex)**


## Images

- [iTerm2] Fixed blank images.


## Ascii

- Added Ubuntu-Studio. **[@konimex](https://github.com/konimex)**
- Fixed bug causing macOS ascii art to be used on other Operating Systems.
- Display warning about 'ascii' being the new default mode.


## Screenshot

- Use arrays for `$scrot_program`

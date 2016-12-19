## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- **[@z33ky](https://github.com/z33ky)**

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
- Remove `printf` subshells and instead use `printf -v` to declare the variables.
- Set fixed `$PATH` in the beginning of the script.
- Fixed artifacts when using line-breaks in TTYs.
- Removed executable permission from config files. BASH can source them even if they're un-executable.

## Info

**OS** <br \>
- Added support for GNU/kFreeBSD.
- Merged all GNU Hurd instances to Linux since they work exactly the same way.

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

**~~Birthday~~ Install Date**<br \>

- Renamed `get_birthday()` -- > `get_install_date()`
- Removed all `date` usage from `get_install_date()`.
- Added a new function called `convert_time()` which takes the time stamped `ls` output and converts it to a pretty format. The function only uses bash so its much faster than calling `date`. This makes things simple and keeps the output consistent across all Operating Systems. Example: `2016-12-06 16:58:58.000000000` --> `Tue 06 Dec 2016 4:58 PM`

**Disk**<br \>

- Rewrote function from scratch.
    - The function is `40` lines smaller than before and works on all \[1\] versions of `df` we tested on \[2\].
- We only show the `root (/)` partition now.
    - Showing a total of all disks only worked on GNU `df` and we had to hardcode different commands for Distros and Operating Systems that used a different `df`.
- We're using the same `df` flags across all Operating Systems now.
    - No more ugly case statements or per distro hardcoding of `df` flags.
- Removed all percentage calculation since `df` already provides us with the percentage.
- Warn the user if `df` isn't installed.
- Fixed broken output if `df` wasn't installed but the function was enabled.

\[1\] The function doesn't work on Haiku since their `df` is wildly non-standard. (The output format and flags are 100% different from all of the other `df` versions floating around.)

\[2\] Tested on `GNU`, `Busybox`, `BSD`, `Solaris` and `macOS` `df` versions.

**Song**<br \>

- [cmus] Simplify block and fix `artistsort` bug.
- Removed `state` detection.
- Removed duplicate `dbus-send` commands.
- Added support for xmms2. **[@z33ky](https://github.com/z33ky)**

**Battery**<br \>

- [MacOS] Fixed issue where battery always appears as charging. **[@jorgegonzalez](https://github.com/jorgegonzalez)**

**Local IP**<br \>

- [BSD and Solaris] Merged the detection to Linux.
- [Windows] Support multiple interfaces.

**Color Blocks**<br \>

- Use start++ instead of adding it manually after case. **[@konimex](https://github.com/konimex)**
- Fixed bug where color blocks wouldn't respect width in TTYs.
- Cursor positioning now takes `$block_height` into account.


## Images

- [iTerm2] Fixed blank images.
- Fixed bug where image mode would attempt to run in a TTY.


## Ascii

- Added Ubuntu-Studio. **[@konimex](https://github.com/konimex)**
- Fixed bug causing macOS ascii art to be used on other Operating Systems.
- Display warning about 'ascii' being the new default mode.
- Removed `ascii_logo_size` in favor of `ascii_distro='{arch,crux,gentoo}_small`.


## Screenshot

- Use arrays for `$scrot_program`


## Args

- Fixed bug where `neofetch --config` sourced the user config twice.
- Cleaned up config arg handling.

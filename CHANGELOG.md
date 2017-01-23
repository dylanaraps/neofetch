This is another large release containing over `550` commits from 7 contributors. Due to the size and large amount of changes made this release expect at least one minor release to fix any bugs that come up. 

The version number has been bumped to `3.0` due to the large amount of breaking changes introduced this update. I've added backwards compatibility for all of the new changes but there may still be some breakage. I highly recommend starting with a new config to avoid any issues that may arise. 

Neofetch now supports displaying images using `catimg`, `libcaca` and `jp2a`. See this wiki page for screenshots. https://github.com/dylanaraps/neofetch/wiki/Image-Backends

Thanks to everyone who contributed this release, there were a lot of new faces this time around. :)


## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- **[@z33ky](https://github.com/z33ky)**
- **[@mstraube](https://github.com/mstraube)**
- **[@gavinhungry](https://github.com/gavinhungry)**


## IRC

Neofetch now has an IRC channel at `#neofetch` on Freenode. If you have any questions, issues or ideas feel free to join the IRC channel and I'll be happy to assist you. I know that we've already got the Gitter chat but hopefully this makes things easier for those without a GitHub account. :)

[![Freenode](https://img.shields.io/badge/%23neofetch-%20on%20Freenode-brightgreen.svg)](http://irc.lc/freenode/neofetch)


## Collaborators 

I have given collaborator access to both **[@konimex](https://github.com/konimex)** and **[@iandrewt](https://github.com/iandrewt)**. In short this allows them to push directly to the master branch of the repo, manage the issue tracker and also merge pull requests. They've been a huge help the past year so this made sense to me.


## OS

- Added support for AIX.
- Added support for AntiX.
- Added support for GNU/kFreeBSD.
- Added support for Gentoo FreeBSD.
- Added support for GrombyangOS.
- Added support for Joyent SmartOS.
- Added support for Mer.
- Added support for MINIX.
- Added support for MX.
- Added support for Open Source Media Center (OSMC).
- Added support for SalentOS.
- Added support for TrueOS.
- Added support for Windows (MSYS2).


## General

- The default config file is now installed to `/etc/neofetch/config` and acts as a system-wide config file for Neofetch. Editing this file will make the changes available to all users on the system. Those packaging Neofetch **without** using the Makefile will need to make changes to support this.
- The Makefile was rewritten to remove GNU-isms.
- Removed executable permission from config files. BASH can source them even if they're un-executable.
- Travis now runs [shellcheck](https://github.com/koalaman/shellcheck) on every commit and pull request.
    - We've had to exclude around 10 lint errors, see this wiki page for why we did this:
    - https://github.com/dylanaraps/neofetch/wiki/Shellcheck-Exclusions
- Neofetch now supports relative path values when specifying the location to images, ascii files and config files.
    - For example, `neofetch --w3m Pictures/Wallpapers/10.jpg` and `neofetch --w3m 10.jpg` now work.
- Optimize usage of `get_de()`, `get_wm()` and `get_term().
    - We were calling these multiple times, we now only run them once and check to see if they were run previously.
- Optimize info caching, only check for cache files in functions that use caching.
- The manpage is now generated using `help2man`. `help2man` parses the output of `--help` and `--version` to create a manpage. This ensures that our manpage stays 1:1 with the script documentation. We actually found a lot of outdated info in the old manpage thanks to this.
    - A new flag was added called `--gen-man` which generates a neofetch manpage in your current directory.
- Delete most of `info()` and instead call `prin()`.
    - This removes a lot of duplicate code between `info()` and `prin()`.
- Remove `printf` subshells and instead use `printf -v` to declare the variables.
- Fixed artifacts when using line-breaks in TTYs.
- All errors are now sent to `stderr`.
- Renamed `XFCE` --> `Xfce`. **[@gavinhungry](https://github.com/gavinhungry)**
- Cleanup `main()`.
- Renamed `old_flags()` --> `old_options()`.


## Info

**Shell**<br \>

- [Fish] Fixed memory leak caused by Fish.
- Added support for `xonsh`.
- Fixed version output on `ksh`.
- Rewrote the function to remove duplicate code.

**Uptime**<br \>

- Moved duplicate code to a function.
- Changed `$uptime_shorthand` to `on` by default.

**Desktop Environment**<br \>

- Fixed issues where MATE wouldn't be detected properly.
- Added fallback to `$DESKTOP_SESSION`, `$MATE_DESKTOP_SESSION_ID` and `$GNOME_DESKTOP_SESSION_ID`.
- Hide Desktop Environment if it matches Window Manager.

**CPU**<br \>

- [Linux] Don't simplify `cpufreq` speed option names for no reason.
- [Linux] Fixed issues with CPU name detection for architectures other than x86/amd64/ARM.
- [NetBSD] Remove case statement in favor of 1 line test.
- Simplify check for low CPU speeds.
- Expanded `cpu_temp` to take the values `C` and `F`. This means you can now display the CPU temperature as Fahrenheit.

**CPU Usage**<br \>

- Added Haiku cores command.
- Updated Linux and macOS commands to the match the commands in the `get_cpu()` function.

**GPU**<br \>

- [Linux] Each GPU is now printed on a separate line.
- [Linux] Added `--gpu_type` / `$gpu_type` which lets you display `all`, `dedicated` or `integrated` GPUs.

**Memory**<br \>

- [Solaris] Fixed inaccurate used memory size.

**Resolution**<br \>

- [Windows] Declare variables locally to fix conflicts in other functions.

**~~Birthday~~ Install Date**<br \>

- Renamed `get_birthday()` -- > `get_install_date()`
- Removed all `date` command usage from `get_install_date()`.
- Added a new function called `convert_time()` which takes the time stamped `ls` output and converts it to a pretty format. The function only uses bash so its much faster than calling `date`. This makes things simple and keeps the output consistent across all Operating Systems. Example: `2016-12-06 16:58:58.000000000` --> `Tue 06 Dec 2016 4:58 PM`
- Added an option so users can choose between using 24-hour and 12-hour time format
- `get_install_date()` will detect which `ls` program is being used instead of hardcoding them per OS.

**Disk**<br \>

- Rewrote function from scratch.
    - The function is `40` lines smaller than before and works on all \[1\] versions of `df` we tested on \[2\].
- Added the option/flag `disk_show` which allows you to specify which disks, mount points or directories to show the disk info of. (One per line)
- Added the option/flag `disk_subtitle` which allows you to specify how we label each disk. (Mount point or Disk name)
- Removed all percentage calculation since `df` already provides us with the percentage.
- Warn the user if `df` isn't installed.
- Fixed broken output if `df` wasn't installed but the function was enabled.

\[1\] The function doesn't work on Haiku since their `df` is wildly non-standard. (The output format and flags are 100% different from all of the other `df` versions floating around.)

\[2\] Tested on `GNU`, `Busybox`, `BSD`, `Solaris` and `macOS` `df` versions.

**Theme**<br \>

- [KDE] Don't display GTK Themes if KDE is detected.
- [KDE] If `kde[0-9]-config` isn't found, try and look for `$HOME/.kde`.

**Window Manager Theme**<br \>

- Fixed WM Theme not detected on MATE. **[@mstraube](https://github.com/mstraube)**
- Fixed WM Theme detection on KDE. **[@mstraube](https://github.com/mstraube)**

**Song**<br \>

- Added support for xmms2. **[@z33ky](https://github.com/z33ky)**
- Added support for Exaile music player. **[@mstraube](https://github.com/mstraube)**
- Added support for JuK .**[@mstraube](https://github.com/mstraube)**
- Added support for Bluemindo. **[@mstraube](https://github.com/mstraube)**
- Added support for Guayadeque Player. **[@mstraube](https://github.com/mstraube)**
- Added support for Yarock. **[@mstraube](https://github.com/mstraube)**
- Added support for Qmmp. **[@mstraube](https://github.com/mstraube)**
- Added support for QuodLibet. **[@mstraube](https://github.com/mstraube)**
- Added support for Mopidy. **[@d3rrial](https://github.com/d3rrial)**
- [cmus] Simplify block and fix `artistsort` bug.
- Removed `state` detection.
- Removed duplicate `dbus-send` commands. **[@mstraube](https://github.com/mstraube)**
- Hide output if no song is playing.
- Enforce order `artist - title` in `get_song_dbus()`. **[@mstraube](https://github.com/mstraube)**

**Terminal Font**<br \>

- Added support for Alacritty.
- Added support for Konsole. **[@mstraube](https://github.com/mstraube)**
- Added support for Sakura Terminal. **[@mstraube](https://github.com/mstraube)**
- Added support for Pantheon Terminal. **[@mstraube](https://github.com/mstraube)**
- Added support for deepin-terminal. **[@mstraube](https://github.com/mstraube)**
- [Termite] Fixed incorrect font chosen. **[@mstraube](https://github.com/mstraube)**
- [Termite] Also look at default config. **[@mstraube](https://github.com/mstraube)**

**Battery**<br \>

- [MacOS] Fixed issue where battery always appears as charging. **[@jorgegonzalez](https://github.com/jorgegonzalez)**

**Local IP**<br \>

- [BSD and Solaris] Merged the detection to Linux.
- [Windows] Support multiple interfaces.

**Color Blocks**<br \>

- Use `start++` instead of adding it manually after case. **[@konimex](https://github.com/konimex)**
- Fixed bug where color blocks wouldn't respect width in TTYs.
- Cursor positioning now takes `$block_height` into account.
- Fixed all artifacts in virtual consoles.
- Merged `$start` and `$end` into an array called `block_range`.
    - This makes the config option match the command-line flag `--block_range`.


## Images

- [iTerm2] Fixed blank images.
- Fixed bug where image mode would attempt to run in a TTY.
- All of the image/ascii backend handling was rewritten. Backend and Image/File/Directory selection is universal now and should make usage easier.
    - Added `catimg` backend.
    - Added `caca` backend.
    - Added `jp2a` backend.
    - `--image` has been replaced with `--backend`.
        - `--backend` takes `ascii`, `caca`, `catimg`, `jp2a`, `iterm2`, `off`, `tycat`, `w3m`.
    - Shortcut flags were added for easy picking of backends.
        - Each flag can take a file, image or directory as an argument.
        - For example: `neofetch --w3m /path/to/img.jpg` `neofetch --ascii /path/to/file`
        - `--w3m`
        - `--iterm2`
        - `--tycat`
        - `--ascii`
        - `--off`
        - `--catimg`
        - `--caca`
        - `--jp2a`
    - All image and ascii file selection has been replaced with the universal `--source`.
       - The value of `--source` can be any of the following:
       - `auto`, `ascii`, `wallpaper`, `/path/to/img`, `/path/to/ascii`, `/path/to/dir/`.
- Fixed bugs with image shuffle mode.


## Wallpaper

- Decode URI filenames.


## Ascii

- Simplified ascii file handling.
    - Removed a call to `tr` for those using `bash 3`.
    - Fixed distro detection issues.
    - Removed the assumption that `first word in distro --> ascii file name`
- Added Ubuntu-Studio. **[@konimex](https://github.com/konimex)**
- Fixed bug causing macOS ascii art to be used on other Operating Systems.
- Display warning about 'ascii' being the new default mode.
- Removed `ascii_logo_size` in favor of `ascii_distro='{arch,crux,gentoo}_small'`.
- [PCBSD] Use TrueOS ascii art.
- Added Void Linux (small) and Alpine Linux (small).


## Screenshot

- Use arrays for `$scrot_program`


## Args

- Fixed bug where `neofetch --config` sourced the user config twice.
- Cleaned up config arg handling.

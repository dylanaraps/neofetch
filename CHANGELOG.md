## Neofetch 2.0

This is the biggest release of Neofetch in a long time. 97 files were changed with 2700~ additions to 2900~ deletions. Although the changelog isn't as interesting this time majority of the script has been rewritten, restructered and cleaned up. Every function and variable name follows a proper naming scheme and a large number of bugs were fixed.

Since this version of Neofetch differs so much from the previous versions expect a 2.0.1 release a few days later to fix any bugs that are found after release.

The ascii file handling was rewritten, ascii art is now stored/read as plain text! All `eval` usage was removed from Neofetch, vim fold markers/comments are no longer enforced and we now run on GNU Hurd, Haiku and more.

When I was rewriting parts of the script I thought to myself; Neofetch is using the bash shebang and does depend on bash so why not take full advantage of the features bash has to offer? All tests were changed from `[` to `[[`, arithmetic tests now use `(())` and C style for loops are used where possible.

All of the config file documentation was rewritten and multiple wiki pages were created to hopefully make using/configuring Neofetch easier than ever before. You can see the wiki here: [Neofetch Wiki](https://github.com/dylanaraps/neofetch/wiki)

Some of the config options/arguments were renamed/changed and Neofetch will warn you on run if you're using deprecated options (`neofetch -v`). For this release Neofetch **will** include backwards compatibility with the old config file but I'd like to remove this stuff in 2.1. I recommend using this release with a fresh config file so that you can make use of the new documentation.

I say this every release; This changelog is incomplete, for a full list of changes take a look through the commit history. Neofetch now has an unspoken commit style so reading the commit history won't hurt as much as it used to.

Thanks to all of the contributors this time around, you guys are a big help and I really appreciate your work towards making Neofetch better and better each release. :)

## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@TonCherAmi](https://github.com/TonCherAmi)**
- **[@JorgeGonzalez](https://github.com/JorgeGonzalez)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@iwamatsu](https://github.com/iwamatsu)**
- **[@Brottweiler](https://github.com/Brottweiler)**


## Packages

- Neofetch is now in Debian's official repos.
- Neofetch is now in Ubuntu's official repos.


## General

- All functions/variables now follow the same naming scheme. `example_func_name`
- Call `uname` once and cache the output instead of calling `uname` 4-5 times.
- Cleaned up and rewrote large chunks of the script.
- Convert math tests to correct syntax.
- Fixed `--disable` and capitalized arguments.
- Fixed issue where `bold=off` wouldn't work.
- Fixed issue where info wasn't detected properly but the subtitle was still displayed.
- Fixed issue where using `--disable func func` broke other args.
- Removed all traces of `eval` from Neofetch.
- Removed all vim fold markers and stopped enforcing folding for vim users.
    - See [#431](https://github.com/dylanaraps/neofetch/pull/431)
- Rewrote all of config file documentation.
- Swap all tests from `[` to `[[`.


## Operating System

- Added support for ChaletOS.
- Added support for DracOS.
- Added support for GNU Hurd. **[@konimex](https://github.com/konimex)**
- Added support for Haiku. **[@konimex](https://github.com/konimex)**
- Added support for Korora. **[@konimex](https://github.com/konimex)**
- Added support for Netrunner. **[@konimex](https://github.com/konimex)**
- Added support for Pardus.
- Added support for iPhone 7 and 7 Plus.


## Ascii

- Ascii art is no longer read as a script and is now read as plain text.
  - See this wiki page about the new ascii art format.
  - https://github.com/dylanaraps/neofetch/wiki/Custom-Ascii-art-file-format
- Neofetch now displays your OS's ascii logo if your distro's logo isn't found. **[@konimex](https://github.com/konimex)**
    - Example: [Linux] Tux is displayed if there's no distro ascii.
- `neofetch --ascii_distro x` now sets the mode to ascii for you. You no longer have to use a combination of `--ascii` and `--ascii_distro`.
- [Arch Linux] Changed default ascii colors.
- [Bunsenlabs] Changed default ascii colors.
- Fixed issue with Solarized and certain ascii art.
- Remove all duplicates from `get_distro_colors()`.
- Remove execution permission flag from ascii art files. **[@iwamatsu](https://github.com/iwamatsu)**
- Rename `colors()` to `get_distro_colors()`.
- Rename `setcolors()` to `set_colors()`.
- Update Netrunner ascii art.
- Added old arch ascii logo. **[@Brottweiler](https://github.com/Brottweiler)**
    - Useable by using `--ascii_distro arch_old` or by editing the config.


## Images

- Fixed images not appearing in st.
- Added `to_ascii()` and `to_off()`.
    - These functions are used when falling back to different image modes.
- Renamed `check_old_flags()` to `old_flags()` to match `old_functions()`.
- Split `get_image()` into `get_term_size()`, `get_image_size()`, `get_image_program()` and `make_thumbnail()`.
- Use `$XDG_CACHE_HOME` as the thumbnail dir if available.


## Wallpaper

- Added support for Cinnamon.


## Bars

- Rename all `progress_` variables to `bar_` to match the function name.


## Info

**Distro**<br \>

- [Linux] Source `/etc/*-release` files instead of having a dozen separate `awk` commands.
    - We source `/etc/os-release` before falling back to `/etc/*-release`.
- Remove lsb_release detection.
    - This change was made since lsb_release prints innacurate results on some distros.
- Added fallback when distro isn't found. **[@konimex](https://github.com/konimex)**
    - Example: `Linux (Unknown)`

**Packages**<br \>

- [Solus] If `pisi` is unavailable, use `eopkg`.
- Added package detection for Lunar Linux. **[@konimex](https://github.com/konimex)**
- Added package detection for TinyCore. **[@konimex](https://github.com/konimex)**
- Remove `/usr/games` from `$PATH` to fix issues with pacman game.

**GPU**<br \>

- GPU is now cached till reboot.
- [Linux] Prefer dedicated GPU over integrated GPU.

**Terminal**<br \>

- Added support for HyperTerm. **[@JorgeGonzalez](https://github.com/JorgeGonzalez)**

**Terminal Font**<br \>

- Added support for HyperTerm. **[@JorgeGonzalez](https://github.com/JorgeGonzalez)**

**CPU**<br \>

- [BSD] Added cpu_temp support. **[@konimex](https://github.com/konimex)**

**CPU Usage**<br \>

- [iOS] Fixed CPU usage.

**Shell**<br \>

- [bash] Simplify bash version.

**Song**<br \>

- Added support for Clementine. **[@konimex](https://github.com/konimex)**
- Added support for GNOME Music. **[@konimex](https://github.com/konimex)**
- Added support for Lollypop. **[@konimex](https://github.com/konimex)**
- Added support for Pragha. **[@konimex](https://github.com/konimex)**

**Public IP**<br \>

- Cache the output of the command. **[@konimex](https://github.com/konimex)**
- [dig] Fixed connection timed out with public_ip. **[@iandrewt](https://github.com/iandrewt)**

**Resolution**<br \>

- [MacOS] If refresh rate is empty don't append Hz.

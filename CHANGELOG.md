## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@TonCherAmi](https://github.com/TonCherAmi)**
- **[@JorgeGonzalez](https://github.com/JorgeGonzalez)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@iwamatsu](https://github.com/iwamatsu)**


## General

- Fixed issue where info wasn't detected properly but the subtitle was still displayed.
- Fixed issue where `bold=off` wouldn't work.
- Fixed issue where using `--disable func func` broke other args.
- Swap all tests from `[` to `[[`.
- Cleaned up and rewrote various functions.
- Removed all traces of `eval` from neofetch.
- All functions/variables now follow the same naming scheme. `example_func_name`
- Convert math tests to correct syntax.
- Removed all vim fold markers and stopped enforcing folding for vim users.
    - See [#431](https://github.com/dylanaraps/neofetch/pull/431)
- Call `uname` once and cache the output instead of calling `uname` 4-5 times.


## Operating System

- Added support for Haiku OS. **[@konimex](https://github.com/konimex)**
- Added support for GNU Hurd. **[@konimex](https://github.com/konimex)**
- Added support for ChaletOS.
- Added support for DracOS.
- Added support for Pardus.
- Added support for Netrunner. **[@konimex](https://github.com/konimex)**
- Added support for Korora. **[@konimex](https://github.com/konimex)**
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
- Rename `colors()` to `get_distro_colors()`.
- Rename `setcolors()` to `set_colors()`.
- Remove all duplicates from `get_distro_colors()`.
- Remove execution permission flag from ascii art files. **[@iwamatsu](https://github.com/iwamatsu)**
- Update Netrunner ascii art.


## Images

- Fixed images not appearing in st.
- Added `to_ascii()` and `to_off()`.
    - These functions are used when falling back to different image modes.
- Renamed `check_old_flags()` to `old_flags()` to match `old_functions()`.
- Split `get_image()` into `get_term_size()`, `get_image_size()`, `get_image_program()` and `make_thumbnail()`.
- Use `$XDG_CACHE_HOME` as the thumbnail dir if available.


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

**GPU**<br \>

- [Linux] Properly detect gpu in multi gpu setups. **[@TonCherAmi](https://github.com/TonCherAmi)**

**Terminal**<br \>

- Added support for HyperTerm. **[@JorgeGonzalez](https://github.com/JorgeGonzalez)**

**Terminal Font**<br \>

- Added support for HyperTerm. **[@JorgeGonzalez](https://github.com/JorgeGonzalez)**

**CPU Usage**<br \>

- [iOS] Fixed CPU usage.

**Shell**<br \>

- [bash] Simplify bash version.

**Song**<br \>

- Added support for GNOME Music. **[@konimex](https://github.com/konimex)**
- Added support for Lollypop. **[@konimex](https://github.com/konimex)**

**Public IP**<br \>

- [dig] Fixed connection timed out with public_ip. **[@iandrewt](https://github.com/iandrewt)**

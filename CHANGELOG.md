## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@TonCherAmi](https://github.com/TonCherAmi)**
- **[@JorgeGonzalez](https://github.com/JorgeGonzalez)**


## General

- Fixed issue where info wasn't detected properly but the subtitle was still displayed.
- Fixed issue where `bold=off` wouldn't work.
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
- Added support for DracOS.
- Added support for Pardus.
- Added support for Netrunner. **[@konimex](https://github.com/konimex)**
- Added support for Korora. **[@konimex](https://github.com/konimex)**
- Added support for iPhone 7 and 7 Plus.


## Ascii

- Ascii art is no longer read as a script and is now read as plain text.
  - See this wiki page about the new ascii art format.
  - https://github.com/dylanaraps/neofetch/wiki/Custom-Ascii-art-file-format
- Added generic Linux ascii art to display if neofetch doesn't have the right logo for your distro.
- `neofetch --ascii_distro x` now sets the mode to ascii for you. You no longer have to use a combination of `--ascii` and `--ascii_distro`.


## Images

- Fixed images not appearing in st.


## Info

**Distro**<br \>

- [Linux] Source `/etc/*-release` files instead of having a dozen separate `awk` commands.

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

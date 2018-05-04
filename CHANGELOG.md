This release bumps the version number up to `4.0.0` as it contains major
changes to how Neofetch is packaged and installed.

The entirety of Neofetch is now contained within a single executable.
Everything has been in-lined. Installing Neofetch is now as easy as
downloading the script and running it.

Packaging Neofetch is now easier as well. We were using `sed` in the
`Makefile` to replace specific paths and we have had to work around
different system hierarchies. None of this is necessary anymore.

Those using distributions with an outdated Neofetch version in their repos
can now easily install the latest version.

Thanks to those who contributed this time around and thanks to those who
discussed proposed changes in the bug tracker. I appreciate it. :+1:


## Contributors

<!-- - [**@**](https://github.com/) -->
- [**@aidanharris**](https://github.com/aidanharris)
- [**@DanySpin97**](https://github.com/DanySpin97)
- [**@SolitudeSF**](https://github.com/SolitudeSF)
- [**@Kayant**](https://github.com/Kayant)
- [**@robertwolter**](https://github.com/robertwolter)
- [**@TsundereBug**](https://github.com/TsundereBug)
- [**@dawidd6**](https://github.com/dawidd6)
- [**@mstraube**](https://github.com/mstraube)


## Operating System

- Added support for ArcoLinux.


## General

- Neofetch is now a single executable.
- Simplified `--version` output.
- Fixed theme issues by setting `GIO_EXTRA_MODULES`.


## Images

- Added `wal`/`pywal` support to get the current wallpaper.
- Added `kitty` image backend. [**@SolitudeSF**](https://github.com/SolitudeSF)
- Added `setroot` wallpaper support. [**@SolitudeSF**](https://github.com/SolitudeSF)


## Ascii

- Updated Android ascii art to better work on non-unicode terminals. [**@TsundereBug**](https://github.com/TsundereBug)


## Info

**Title**

- Fixed unexpected backslash being inserted on some systems.

**CPU**

- Added temperature support for Zen processors. [**@Kayant**](https://github.com/Kayant)

**GPU**

- Fixed duplicate Intel GPUs.

**Terminal Font**

- Added support for `st`. [**@aidanharris**](https://github.com/aidanharris)
- Added support for `qterminal`. [**@mstraube**](https://github.com/mstraube)

**Packages**

- Fixed package count in Exherbo. [**@DanySpin97**](https://github.com/DanySpin97)

**Desktop Environment**

- Fixed Unity output in Ubuntu 18.04. [**@dawidd6**](https://github.com/dawidd6)

**Window Manager**

- Added support for detecting `dwm`.

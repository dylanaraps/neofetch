# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [6.0.1] - N/A

- **ascii**: Fixed bug causing files to not work.
- **ascii**: Fixed bug causing files named `ascii` to not load.
- **term_font** [kitty]: Fixed bug with empty config.
- **get_cols**: Variables are now local. [**@asantam**](https://github.com/asantam)
- **man_page**: More consistent arg documentation. [**@xPMo**](https://github.com/xPMo)


## [6.0.0] - 2019-01-08

<img src="https://i.imgur.com/ZQI2EYz.png" alt="logo" height="100px">

This release fixes a wide range of bugs and adds some neat new features.
Scroll down to "highlights" to see the bigger changes from this release.
A big thank you to @konimex, @iandrewt and the contributors below who
kept development going during my absence.

Expect a minor bug fix release sometime this week as I'm sure new bugs
will come up. I've done extensive testing but things always slip through.

**Contributors**

[**@konimex**](https://github.com/konimex), [**@iandrewt**](https://github.com/iandrewt), [**@arisinfenix**](https://github.com/arisinfenix), [**@xPMo**](https://github.com/xPMo), [**@nero**](https://github.com/nero), [**@alyssais**](https://github.com/alyssais),
[**@plgruener**](https://github.com/plgruener), [**@StarryTony**](https://github.com/StarryTony), [**@julianaito**](https://github.com/julianaito), [**@HolyStephano**](https://github.com/HolyStephano),
[**@nikitenich**](https://github.com/nikitenich), [**@Appadeia**](https://github.com/Appadeia), [**@marlonn**](https://github.com/marlonn), [**@Snuggle**](https://github.com/dylanaraps/neofetch/commits?author=Snuggle), [**@Phuurl**](https://github.com/Phuurl), [**@erikdubois**](https://github.com/erikdubois)


**Breaking Changes**

- **Config**: Removed `get_line_break()`.
    - Alternative: `prin '\n'`
    - Rationale: fix a bug that's been lingering for a couple of years now.

**OS**

- Added support for Bedrock Linux. [**@paradigm**](https://github.com/paradigm)
- Added support for Namib GNU/Linux. [**@arisinfenix**](https://github.com/arisinfenix)
- Added support for Reborn OS. [**@iandrewt**](https://github.com/iandrewt)
- Added support for OpenMandriva Lx. [**@konimex**](https://github.com/konimex)
- Added support for Star. [**@arisinfenix**](https://github.com/arisinfenix)
- Added support for BlueLight OS.
- Added support for Huayra Linux.
- Added support for Pentoo.

**Highlights**

[ASCII] Added support for command output. You can now use whatever
terminal commands you like as the ASCII art.

```sh
# Use fortune and cowsay as ascii art.
neofetch --ascii "$(fortune|cowsay -W 30)"

# use figlet as ascii art.
neofetch --ascii "$(figlet -w 30 hello world)"
```

<img src="https://i.imgur.com/ozoXAvz.jpg" alt="scrot" height="400px">

Added a new "simple" mode. You can now use neofetch for scripting
by getting it to output individual info functions in plain text.

```sh
# Example:
neofetch uptime --uptime_shorthand tiny
> uptime: 32m

# Example:
neofetch uptime disk wm memory
> uptime: 33 mins
> disk (/): 212G / 235G (96%)
> wm: Openbox
> memory: 1215MiB / 7881MiB

# This can be used in bars and scripts like so:
memory="$(neofetch memory)"; memory="${memory##*: }"

# For multiple outputs at once (each line of info in an array):
# Much faster than running neofetch multiple times.
IFS=$'\n' read -d "" -ra info < <(neofetch memory uptime wm)
info=("${info[@]##*: }")
```

Added new image backend [chafa](https://hpjansson.org/chafa/) (`--chafa`)
which displays images in the terminal using unicode characters.

```sh
neofetch --chafa ~/Pictures/meow.jpg
```

<img src="https://i.imgur.com/fCOoWlA.jpg" alt="scrot" height="400px">


**Info**

- **Color Blocks**: Fixed issue where disabling blocks caused an extra newline to appear.
- **Color Blocks**: Color blocks now have their padding built in. No more need for `get_line_break()`.
- **Song**: Added snippet to display music player.
    - `[[ $player ]] && prin "Music Player" "$player"`
    - NOTE: Must have `info "Song" song` enabled.
- **Song**: Added support for Netease Cloud.
- **Song**: Fixed issues in various players. [**@arisinfenix**](https://github.com/arisinfenix) [**@xPMo**](https://github.com/xPMo)
- **Song**: Fixed issues with non-English tags.
- **Song**: Fixed issues with broken newlines.
- **Song**: Fixed issues with Deadbeef.
- **Song**: Fixed issues with `qmmp`.
- **Song**: Removed `gpmdp-remote` support (unmaintained/no longer works).
- **Shell**: Fixed output for mksh [**@nero**](https://github.com/nero)
- **Packages**: Added support for `scoop`. [**@Phuurl**](https://github.com/Phuurl)
- **Packages**: Added support for `puyo`. [**@Appadeia**](https://github.com/Appadeia)
- **Packages**: Added support for `spm`. [**@Appadeia**](https://github.com/author=Appadeia)
- **Packages** [macOS]: Added detection of Nix [**@alyssais**](https://github.com/alyssais)
- **Packages**: Fixed packages from pkginfo (pkgutils) not appearing in CRUX/Janus Linux.
- **Terminal Font**: Added support for Yakuake [**@plgruener**](https://github.com/plgruener)
- **Terminal Font** [Kitty]: Use `kitty --debug-config` to get font information.
- **Memory** [Solaris]: Updated memory detection to use pages. [**@konimex**](https://github.com/konimex)
- **Memory**: Added option to show memory percentage (`--memory_percent`).
- **Model** [OpenBSD]: Added vmm (OpenBSD hypervisor) support [**@julianaito**](https://github.com/julianaito)
- **Model** [macOS]: Added VirtualSMC as a new FakeSMC alternative for Hackintosh. [**@nikitenich**](https://github.com/nikitenich)
- **WM**: Added detection for FVWM. [**@julianaito**](https://github.com/julianaito)
- **WM** [OpenBSD]: Added a new `ps_flags` to correctly detect non-EWMH WMs. [**@julianaito**](https://github.com/julianaito)
- **Disk** [OpenBSD]: Added a separate disk array creation using `awk` since one cannot directly use `/dev/...` unless being root or in the `operator` group. [**@julianaito**](https://github.com/julianaito)
- **Battery** [OpenBSD]: Improve charge `%` and add status. **Charlène**
- **GPU** [AMD]: Remove unnecessary check.
- **Public IP**: Added configurable timeout to requests.
- **Resolution**: If resolution is not found, don't print anything.

**ASCII**

- Fixed issues with various ASCII arts (namely the `_small` ones).
- Added support for command output.
    - `neofetch --ascii "$(fortune|cowsay -W 30)"`
    - `neofetch --ascii "$(figlet -w 30 hello world)"`
- Added small ArcoLinux logo. [**@erikdubois**](https://github.com/erikdubois)
- Added new Lubuntu logo. [**@marlonn**](https://github.com/marlonn)
- Fixed a bug where ASCII logo changes the terminal foreground color. [**@plgruener**](https://github.com/plgruener)
- Fixed a bug when files named `auto` or `ascii` exist.
- Do not parse file as ASCII if the source is an image file.

**Image**

- Added new image backend [chafa](https://hpjansson.org/chafa/) (`--chafa`).
- **w3m**: Fixed issues with URxvt and internal borders.
- **w3m**: Fixed issues with URxvt and cursor position.
- **w3m**: Fixed issue with `bash 3`.
- **macOS**: Unset IFS to get window size. [**@StarryTony**](https://github.com/StarryTony)
- **Kitty**: Use `kitty +kitten icat` instead of the deprecated `kitty icat`. [**@HolyStephano**](https://github.com/HolyStephano)
- **Kitty**: Update docs. [**@Snuggle**](https://github.com/dylanaraps/neofetch/commits?author=Snuggle)
- Thumbnails are high quality again.
- Cached thumbnails are now stored with PATH to prevent collision issues.

## [5.0.0] - 2018-06-18

<img src="https://i.imgur.com/ZQI2EYz.png" alt="logo" height="100px">

A lot of the script has been rewritten and all lint errors have been resolved. There's probably a few bugs so the version number has been bumped to `5.0`. Expect a minor release in the coming days to fix any bugs that come up. Thanks to everyone who contributed to this release.

**Contributors**

- [**@arisinfenix**](https://github.com/arisinfenix)
- [**@iandrewt**](https://github.com/iandrewt)
- [**@konimex**](https://github.com/konimex)
- [**@MindTooth**](https://github.com/MindTooth)

**Operating System**

- Added support for Condres OS. [**@arisinfenix**](https://github.com/arisinfenix)
- Added support for RedCore Linux. [**@arisinfenix**](https://github.com/arisinfenix)
- Added support for Regata OS. [**@arisinfenix**](https://github.com/arisinfenix)
- Added support for ClearOS. [**@arisinfenix**](https://github.com/arisinfenix)
- Added support for PureOS.
- Added support for Kibojoe Linux.
- Added support for SharkLinux.
- Added support for Linux Lite.
- Added support for macOS 10.14 Mojave. [**@iandrewt**](https://github.com/iandrewt)

**General**

- **output**: Added `--json` to output the info in `json`.
- **cursor**: Fixed prompt location issues after Neofetch is run.
- **macOS**: Fixed neofetch launching XQuartz.
- **misc**: Removed `uppercase()`.
- **misc**: Removed all instances of `export`.
- **misc**: Removed all deprecated options and functions.
- **info**: Removed `get_install_date()`.

**Ascii**

- Fixed a bug causing Windows 7 ASCII art to not display.
- Simplified ASCII art handling.
- Updated Funtoo ASCII art.

**Image**

- Improved performance of image handling.
- Removed `catimg` support (*It didn’t allow us to specify height so we
  couldn’t accurately place the cursor*).
- Fixed `tycat`, `sixel` and `kitty icat` image sizes.
- Simplified `w3m-img` code.

**Screenshot**

See: https://github.com/dylanaraps/neofetch/issues/1001

- Removed screenshot functionality.
- Removed screenshot upload functionality.

**Info**

- **cpu**: Remove extra call to `uname`.
- **cpu**: Simplify core calculation.
- **disk**: Clean up.
- **font**: Fix iTerm2 checking for 2 extra profiles that don't exist. [**@iandrewt**](https://github.com/iandrewt")
- **gpu**: Fixed ATI/AMD branding issue.
- **gpu**: Removed `glxinfo` usage (*too slow*).
- **packages**: Added support for `flatpak`. [**@konimex**](https://github.com/konimex)
- **packages**: Added support for `snap`. [**@konimex**](https://github.com/konimex)
- **packages**: Added used package managers to output (`Packages: 900
  (pacman, snap)`).
- **packages**: Fixed issues with `pacman` 5.1.
- **packages**: Fixed issues with `dpkg`.
- **packages**: Removed `find` usage.
- **packages**: Removed `ls` usage.
- **packages**: Removed `wc -l` usage.
- **song**: Added support for `gmusicbrowser`. [**@arisinfenix**](https://github.com/arisinfenix)
- **song**: Added support for `SMPlayer`. [**@arisinfenix**](https://github.com/arisinfenix)
- **song**: Added support for `Dragon Player`. [**@arisinfenix**](https://github.com/arisinfenix)
- **song**: Fixed song detection on macOS.
- **song**: Fixed song output on systems using `C` locale.
- **song**: Added `mpc_args` to send additional arguments to `mpc`.
- **term\_font**: Clean up of config file handling.
- **resolution**: Added support for `xwininfo`.

## [4.0.2] - 2018-05-19

### This fixes default config issues on Android, AIX, HP-UX and possibly others.

- [config] Fixed `/dev/stdin` error.
- [config] Added `--print_config` to display the default config file.
- [macOS] Fixed xquartz issue.

## [4.0.1] - 2018-05-18

### Note: This release is only required for those running `bash <3.3`.

- [config] Fixed issue with default config in bash3.
- [packages] Simplified code.
- [term] Fixed macOS issue.
- [term] Fixed `tmux` issue.


## [4.0.0] - 2018-05-17

<h1><img src="https://i.imgur.com/JFxwJtU.png" alt="logo" height="100px"></h1>

This release bumps the version number up to `4.0.0` as it contains major
changes to how Neofetch is packaged and installed.

The entirety of Neofetch is now contained within a single executable.
Everything has been in-lined. Installing Neofetch is now as easy as
downloading the script and running it.

Those using distributions with an outdated Neofetch version in their repos
can now easily install the latest version themselves.

Thanks to those who contributed this time around and thanks to those who
discussed proposed changes in the bug tracker and Discord. I appreciate
it. :+1:


## Discord

Neofetch now has a Discord server. Come and join the discussion!

<a
href="https://discord.gg/BtnTPFF"><img
src="https://img.shields.io/discord/440354555197128704.svg"></a>


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
- [**@iandrewt**](https://github.com/iandrewt)
- [**@MindTooth**](https://github.com/MindTooth)


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

**Song**

- Added support for VLC. [**@mstraube**](https://github.com/mstraube)
- Added support for Sayonara. [**@mstraube**](https://github.com/mstraube)
- Added album data to song output. [**@mstraube**](https://github.com/mstraube), [**@iandrewt**](https://github.com/iandrewt)
- Added `song_format` to change the display format of the data.
    - Default: `%artist% - %album% - %title%`.

**Title**

- Fixed unexpected backslash being inserted on some systems.

**CPU**

- Added temperature support for Zen processors. [**@Kayant**](https://github.com/Kayant)

**GPU**

- Fixed duplicate Intel GPUs.

**Terminal Font**

- Added support for `st`. [**@aidanharris**](https://github.com/aidanharris)
- Added support for `qterminal`. [**@mstraube**](https://github.com/mstraube)
- Fixed `kitty` font bug. [**@MindTooth**](https://github.com/MindTooth)

**Packages**

- Fixed package count in Exherbo. [**@DanySpin97**](https://github.com/DanySpin97)

**Desktop Environment**

- Fixed Unity output in Ubuntu 18.04. [**@dawidd6**](https://github.com/dawidd6)

**Window Manager**

- Added support for detecting `dwm`.


## [3.4.0] - 2018-04-05

This release adds support for a large number of Linux distros as well as support for the latest macOS and iOS devices. This release also contains a large number of bug fixes and some minor features.

I'm pretty sure that this release is the largest in terms of number of contributors. Thanks to everyone who contributed this release!

## Contributors

- [**@yslgirl**](https://github.com/yslgirl)
- [**@iandrewt**](https://github.com/iandrewt)
- [**@chrisweeksnz**](https://github.com/chrisweeksnz)
- [**@dawidd6**](https://github.com/dawidd6)
- [**@MitchWeaver**](https://github.com/MitchWeaver)
- [**@StarryTony**](https://github.com/StarryTony)
- [**@rage311**](https://github.com/rage311)
- [**@matoro**](https://github.com/matoro)
- [**@szfcbr**](https://github.com/szfcbr)
- [**@ArmstrongJ**](https://github.com/ArmstrongJ)
- [**@robertwolter**](https://github.com/robertwolter)
- [**@JadeMatrix**](https://github.com/JadeMatrix)
- [**@MindTooth**](https://github.com/MindTooth)
- [**@aidanharris**](https://github.com/aidanharris)
- [**@khoacao96**](https://github.com/khoacao96)


## OS

- Added support for ArchMerge.
- Added support for MagpieOS.
- Added support for PostMarketOS.
- Added support for Hyperbola GNU/Linux-libre [**@mstraube**](https://github.com/mstraube)
- Added support for macOS High Sierra. [**@yslgirl**](https://github.com/yslgirl)
- Added support for Container Linux by CoreOS. [**@chrisweeksnz**](https://github.com/chrisweeksnz)
- Added support for 2017 iOS devices. [**@iandrewt**](https://github.com/iandrewt)
- Added support for LEDE. [**@dawidd6**](https://github.com/dawidd6)
- Added support for Pop!\_OS. [**@jliles**](https://github.com/jliles)
- Added support for Lunar Linux.
- Added support for 32-bit IRIX. [**@szfcbr**](https://github.com/szfcbr)
- Added support for FreeMINT. [**@ArmstrongJ**](https://github.com/ArmstrongJ)
- Added support for Anarchy Linux. [**@robertwolter**](https://github.com/robertwolter)
- Added support for Calculate Linux. [**@robertwolter**](https://github.com/robertwolter)
- Added support for NuTyX. [**@robertwolter**](https://github.com/robertwolter)
- Added support for openSUSE Tumbleweed. [**@robertwolter**](http://github.com/robertwolter)
- Fixed detection bug with Gentoo.
- Fixed detection bug with OpenWRT. [**@dawidd6**](https://github.com/dawidd6)
- Fixed detection bug with LEDE. [**@dawidd6**](https://github.com/dawidd6)
- Fixed detection bug with TrueOS. [**@dawidd6**](https://github.com/dawidd6)
- Fixed detection bug with Windows Subsystem for Linux and Crouton when an OS without lsb_release is installed.
- Fixed ChromeOS detection.


## General

- Added more info to verbose mode for debugging.
- Fixed bug in prompt location calculation.
- Fixed prompt bug in OpenBSD.
- Fixed broken AppleScript blocks. [**@JadeMatrix**](https://github.com/JadeMatrix)
- Fixed  function not working in bash 3. [**@JadeMatrix**](https://github.com/JadeMatrix)
- Swapped sequences from `\033` to `\e`.
- Fixed Pacman name conflict with the game. [**@MitchWeaver**](https://github.com/MitchWeaver)
- Removed the last `echo` in the script.
- Fixed typo. [**@khoacao96**](https://github.com/khoacao96)


## Ascii

- Added color updates for Kubuntu logo. **Maulik Mistry**
- Added new DragonflyBSD logo. [**@MitchWeaver**](https://github.com/MitchWeaver)


## Images

- [MacOS/iTerm2] Fixed thumbnail not appearing. [**@StarryTony**](https://github.com/StarryTony)
- Fixed bug with getting wallpaper from feh.
- Added `pixterm` backend.
- Don't force resolution in `catimg`.

## Info

**Desktop Environment**

- Added GNOME version.
- Added support for TDE.

**Window Manager**

- Added support for most (*if not all*) current Wayland compositors/window manager's.
- Added support for some non-EWMH window managers.
- [macOS] Fixed `chunkwm` being detected as `Kwm`. [**@iandrewt**](https://github.com/iandrewt)

**Window Manager Theme**

- Fixed `sawfish` detection.
- [macOS] Now detects Light/Dark theme. [**@JadeMatrix**](https://github.com/JadeMatrix)

**Install Date**

- [macOS] Fixed Install Date. [**@iandrewt**](https://github.com/iandrewt)

**Theme**

- Fixed KDE font issue. [**@mstraube**](https://github.com/mstraube)

**CPU**

- [linux] Detect the correct temperature file to use.
- [windows] Removed `$temp` usage as it's an envar.
- [OpenBSD] Fixed CPU temperature that fails to appear in some systems. [**@rage311**](https://github.com/rage311)

**GPU**

- [linux] Added driver version to NVIDIA output.
- [linux] Added driver version to Intel output.
- [macOS] Added NVIDIA support. [**@iandrewt**](https://github.com/iandrewt)

**Memory**

- [OpenBSD] Fixed memory usage values. [**@rage311**](https://github.com/rage311)

**Package Manager**

- Added detection for Sabotage Linux's `butch` [**@MitchWeaver**](https://github.com/MitchWeaver)
- Changed `pacman` detection to fix issues in other distros. [**@MitchWeaver**](https://github.com/MitchWeaver)

**Resolution**

- [macOS] Fixed errors on non-retina screens. [**@iandrewt**](https://github.com/iandrewt)

**Song**

- Added option to manually specify the player to use.
- Added support for Elisa. [**@mstraube**](https://github.com/mstraube)
- macOS detection is now more reliable. [**@JadeMatrix**](https://github.com/JadeMatrix)

**Model**

- Remove more unneeded outputs. [**@konimex**](https://github.com/konimex)

**Disk**

- Update Haiku's detection. [**@dawidd6**](https://github.com/dawidd6)

**Battery**

- Fixed Windows detection. [**@matoro**](https://github.com/matoro)

**Shell**

- Added support for `tcsh`. [**@szfcbr**](https://github.com/szfcbr)

**Terminal Font**

- Added more paths for Alacritty.
- Added font support for Kitty. [**@MindTooth**](https://github.com/MindTooth)
- Fixed Kitty `font_size` regex. [**@aidanharris**](https://github.com/aidanharris)
- Added support for `XTerm.vt11.facename`. [**@aidanharris**](https://github.com/aidanharris)


## [3.3.0] - 2017-09-14

Thanks to everyone who contributed this release, I appreciate ya!

## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@mstraube](https://github.com/mstraube)**
- **[@dominiklohmann](https://github.com/dominiklohmann)**
- **[@ybden](https://github.com/ybden)**
- **[@lexruee](https://github.com/lexruee)**
- **[@AMDmi3](https://github.com/AMDmi3)**
- **[@deadda7a](https://github.com/deadda7a)**
- **[@winneon](https://github.com/winneon)**
- **[@DamnWidget](https://github.com/DamnWidget)**


## General

- Config file now has a `.conf` suffix.
- Neofetch now assumes target directories (config file and ASCII directory) at install time, this fixes problems with systems such as NixOS.
- `stdout` mode is now reimplemented.
    - This mode prints the information in plain text.
    - You can use it with `--stdout`.
    - Example: https://gist.github.com/dylanaraps/151c205322cf3acae62661b76464a3f7
- Fixed prompt location if color blocks are disabled.
- Make makefile more portable. **[@AMDmi3](https://github.com/AMDmi3)**


## Operating System

- Added support for AryaLinux. **[@mstraube](https://github.com/mstraube)**
- Added support for Amazon Linux AMI.
- Added support for Artix Linux. **[@DamnWidget](https://github.com/DamnWidget)**
- Added support for Endless OS.
- Added support for Sabotage Linux.
- Added support for Siduction. **[@lexruee](https://github.com/lexruee)**
- Added support for Source Mage.
- Added support for Parsix GNU/Linux. **[@mstraube](https://github.com/mstraube)**
- Added support for Nurunner. **[@mstraube](https://github.com/mstraube)**
- Fixed Raspbian being detected as ChromeOS.


## Images

- [w3m] Fixed w3m-img not found on NixOS.
- Added support for using all image types as input.
    - Neofetch now supports `svg`, `tiff` etc.


## ASCII

- Added small Debian.
- Added small FreeBSD.
- Added small macOS.
- Added small NixOS.


## Info

**GPU Driver**

- [Linux] Added a new info function (*off by default*) to display the GPU Driver currently in use.
- Add `info "GPU Driver" gpu_driver` to your config to use it.

**CPU**

- [Linux] Fixed inaccurate output on ARM SoC devices.
- [Linux] Fixed CPU speed not appearing on PowerPC systems.
- [NetBSD] Added support for CPU temperature. (NOTE: This only supports newer Intel processors)
- Fixed inaccurate speed output in systems with CPU speed less than 1 GHz.
- Deprecated `cpu_shorthand` in favor of `cpu_brand`.

**GPU**

- [Linux] Filter out duplicate entries.

**Model**

- Added support for QEMU/KVM.
- Renamed subtitle to `Host:`.

**Uptime**

- [AIX/IRIX] Fixed Neofetch crashing when calculating uptime.

**Terminal**

- [SSH] Fixed infinite loop if neofetch is run on non-interactive shells.

**Terminal Font**

- Added support for LXTerminal. **[@mstraube](https://github.com/mstraube)**
- Added support for GNUStep Terminal. **[@mstraube](https://github.com/mstraube)**
- Fixed Xfce4-terminal font output when system-wide font is used. **[@mstraube](https://github.com/mstraube)**
- Fixed MATE-Terminal issue. **[@mstraube](https://github.com/mstraube)**
- Fixed URxvt font detection failing if `.` is used. **[@winneon](https://github.com/winneon)**

**Theme**

- [Qt/KDE] Fixed inaccurate theme naming. **[@mstraube](https://github.com/mstraube)**
- [Qt/KDE] GTK theme is now shows as well.

**Window Manager**

- [macOS] Added support for `chunkwm`. **[@dominiklohmann](https://github.com/dominiklohmann)**
- Fix incorrect output when using WindowMaker. **[@mstraube](https://github.com/mstraube)**

**Song**

- Added support for Pogo. **[@mstraube](https://github.com/mstraube)**
- Fixed bug with players not being found.

**Battery**

- Added battery support for Thinkpads and other devices that use the `CMB` naming for batteries. **[@deadda7a](https://github.com/deadda7a)**


## Images

- Fixed division by 0 error in XTerm.

## Screenshot

- Use `maim` over `scrot`. **[@ybden](https://github.com/ybden)**
- Fixed `scrot_cmd` arguments not being used. **[@winneon](https://github.com/winneon)**


## [3.2.0] - 2017-06-21

This release was long overdue and I apologise for the delay. I've been busy with study among other things. This update is smaller than usual but fixes some important bugs.


Thanks once again to everyone that contributed!


## Contributors

- **[@MatthewCox](https://github.com/MatthewCox)**
- **[@dawidd6](https://github.com/dawidd6)**
- **[@erikdubois](https://github.com/erikdubois)**
- **[@konimex](https://github.com/konimex)**
- **[@mstraube](https://github.com/mstraube)**
- **[@Artoriuz](https://github.com/Artoriuz)**
- **[@WilsonRU](https://github.com/WilsonRU)**
- **[@Takeya-Yuki](https://github.com/Takeya-Yuki)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@LER0ever](https://github.com/LER0ever)**


## Operating System

- Added support for IRIX.
- Added support for Arch XFerience. **[@mstraube](https://github.com/mstraube)**
- Added support for CloverOS.
- Added support for Maui. **[@mstraube](https://github.com/mstraube)**
- Added support for KS Linux. **[@Takeya-Yuki](https://github.com/Takeya-Yuki)**


## General

- Minimum required BASH version is now 3.2.
    - (Neofetch has always used 3.2+ features, I've just made it obvious now in the documentation.)
- Fixed config file not being created on first install.


## Images

- [w3m] Added `--loop` flag which makes Neofetch draw the image once per second.
    - This is a workaround to the images disappearing on resize and workspace switch.
    - Use Ctrl+C to exit.
- [w3m] Fixed w3m-img not found on FreeBSD 12. **[@Artoriuz](https://github.com/Artoriuz)**


## Ascii

- Added Ubuntu-MATE ascii art.
- Fixed ArchLabs ascii art.  **[@erikdubois](https://github.com/erikdubois)**
- Updated GoboLinux ascii art. **[@WilsonRU](https://github.com/WilsonRU)**
- Fixed `--ascii_distro windows10` not working.


## Info

**Distro**

- [Solaris, AIX, Haiku] The machine architecture will now be shown properly instead of machine ID.

**Terminal Emulator**

- Added support for Neovim terminal emulator. **[@LER0ever](https://github.com/LER0ever)**
- Added font support for mate-terminal. **[@mstraube](https://github.com/mstraube)**
- [Termite] Fix font mismatch. **[@MatthewCox](https://github.com/MatthewCox)**
- Use `$SSH_TTY` for terminal detection if machine is connected via SSH.
- Break from loop if PPID can't be accessed/not found.

**GPU**

- [Linux] Fixed GPU sort.

**Song**

- Do not detect ibus\* or indicator\* as player. **[@dawidd6](https://github.com/dawidd6)**

**Model**

- Specify when running on a Hackintosh. **[@LER0ever](https://github.com/LER0ever)**


**Memory**

- [FreeBSD]: Fix inaccurate free memory calculation.


## [3.1.0] - 2017-04-25

Hi, It's been quite a while since the last release. I've been extremely busy with university and I finally found some time to flag a new release. (I've been meaning to do this for a few weeks now)

Though I haven't worked on Neofetch as much as I'd have liked, most of the changes this time round come from some familiar faces as well as some new contributors! Thanks to everyone for contributing, I appreciate it.


## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@mstraube](https://github.com/mstraube)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- **[@ikeydoherty](https://github.com/ikeydoherty)**
- **[@eliezio](https://github.com/eliezio)**
- **[@nilesr](https://github.com/nilesr)**
- **[@dritter](https://github.com/dritter)**
- **[@HebaruSan](https://github.com/HebaruSan)**
- **[@LER0ever](https://github.com/LER0ever)**
- **[@obrevenge](https://github.com/obrevenge)**
- **[@ajjames31](https://github.com/ajjames31)**
- Eliezio Oliveira


## Operating System

- Added Chrome OS Crouton support. **[@LER0ever](https://github.com/LER0ever)**
- Added support for SliTaz. **[@nilesr](https://github.com/nilesr)**
- Added support for Nitrux. **[@mstraube](https://github.com/mstraube)**
- Added support for DesaOS.
- Added support for MinGW.
- Added support for OBRevenge. **[@obrevenge](https://github.com/obrevenge)**
- Added support for ArchLabs. **[@obrevenge](https://github.com/obrevenge)**


## Screenshot

The screenshot feature no longer requires any configuration before working. We no longer hardcode `${HOME}/Pictures/neofetch` as the screenshot location. Here's how the `-s` and `-su` flags now function:

- `neofetch -s` will save a file in the current directory named: `neofetch-$(date +%F-%I-%M-%S-${RANDOM}).png`
- `neofetch -s test.png` will save a file in the current directory called `test.png`
- `neofetch -s ~/` will save a file in `~` called `neofetch-$(date +%F-%I-%M-%S-${RANDOM}).png`
- `neofetch -s ~/test.png` will save a file in `~` called `test.png`.


## ASCII

- Arch ASCII art now uses lighter colors.
- Fixed Ubuntu-Studio ASCII setting. **[@@HebaruSan](https://github.com/HebaruSan)**
- Updated Parabola logo. **[@mstraube](https://github.com/mstraube)**
- Updated Raspbian ASCII art.


## Images

- Added `libsixel` backend.
- Added `termpix` backend.
- Only use a zero width space in the `w3m` backend.
- Fixed bug causing terminal size to not be found.
- [iTerm2] Fixed images not appearing inside `tmux`.


## Info

**Locale**

- Added a new function to display system locale. (Disabled by default)

**CPU**

- Added option to show decimals in CPU speed.

**Terminal Font**

- Added \*experimental\* font detection for iTerm2. **[@dritter](https://github.com/dritter)**

**Window Manager**

- [MacOS] Added support for Kwm. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- [MacOS] Added support for Spectacle. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- [MacOS] Added support for Amethyst. **[@jorgegonzalez](https://github.com/jorgegonzalez)**

**Battery**

- Added battery support for Bay Trail devices.  **[@mstraube](https://github.com/mstraube)**

**Disk**

- Added new option to only show dir name in subtitle.

**Song**

- Added support for Deepin Music. **[@mstraube](https://github.com/mstraube)**
- Added support for Tomahawk. **[@mstraube](https://github.com/mstraube)**
- Fixed Audacious song output when `dbus-send` fails. **[@mstraube](https://github.com/mstraube)**

**Local IP**

- [Linux] Fixed UID showing instead of Local IP on several versions/configs of iproute2.

**Packages**

- [eopkg] Use a faster detection method. **[@ikeydoherty](https://github.com/ikeydoherty)**

**Resolution**

- [macOS] Fixed `screenresolution` not appearing at all on newer versions. **[@eliezio](https://github.com/eliezio)**
- [Linux] Show decimals.

**GPU**

- [Linux] Hide duplicate GPU lines (Only display 1).


## [3.0.1] - 2017-01-30

This minor release fixes all of the bugs that were found in the 3.0 release.

Thanks for all of the bug reports and contributions. :)

## Contributors
- **[@SomaUlte](https://github.com/SomaUlte)**
- **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- **[@dawidd6](https://github.com/dawidd6)**
- **[@mstraube](https://github.com/mstraube)**
- **[@YellowApple](https://github.com/YellowApple)**
- **[@siiptuo](https://github.com/siiptuo)**
- **[@Head-on-a-Stick](https://github.com/Head-on-a-Stick)**
- **[@konimex](https://github.com/konimex)**

## Operating System
- Added support for ArchBox Linux.

## General
- Fixed output if subtitles are disabled and `prin` is used in an info function.
- Fixed underlines not working when used with `prin`.
- Fixed HAIKU install path. **[@YellowApple](https://github.com/YellowApple)**

## Config
- Fixed default config not found.
- Don't set locale in config file.

## Info

**Memory**<br \>
- Changed memory label to `MiB` on OS that output memory in Mebibytes.

**Shell**<br \>
- Fixed a crash when the user has `bash 3` installed.

**Packages**<br \>
- Added support for Chromebrew.

**GPU**<br \>
- [Linux] Display detailed information about Intel GPUs. **[@SomaUlte](https://github.com/SomaUlte)**

**Color Blocks**<br \>
- Fixed issue with `color_blocks="off"` adding an extra newline to the output.

**Song**<br \>
- Don't print `$song` if it's empty and `song_shorthand` is on. **[@mstraube](https://github.com/mstraube)**
- Fixed `mpd` detection when `mpd` is on a different host. **[@dawidd6](https://github.com/dawidd6)**
- Use `get_song_dbus` for Audacious. **[@mstraube](https://github.com/mstraube)**

**Terminal Font**<br \>
- [Alacritty] Fixed font detection. **[@siiptuo](https://github.com/siiptuo)**

## Images
- [iTerm2] Fixed issue with line-breaks printing spaces over the image. **[@jorgegonzalez](https://github.com/jorgegonzalez)**
- Fixed issue with images not working in Terminology.
- Fixed issue when `image_source` was set to `wall`.
- [w3m-img] Fixed issues with `w3m-img` and `tmux`.

## Ascii
- [Windows 10] Fixed `ascii_distro` not working.
- Fixed a bug where the backend is `ascii` but the image_source is an image file.
- Fixed custom ascii files not working.
- Removed extra backslashes from OpenBSD ascii art. **[@Head-on-a-Stick](https://github.com/Head-on-a-Stick)**

## Scrot
- Added message to let users know that a screenshot was taken.


## [3.0] - 2017-01-23

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
  - The function is `40` lines smaller than before and works on all [1] versions of `df` we tested on [2].
- Added the option/flag `disk_show` which allows you to specify which disks, mount points or directories to show the disk info of. (One per line)
- Added the option/flag `disk_subtitle` which allows you to specify how we label each disk. (Mount point or Disk name)
- Removed all percentage calculation since `df` already provides us with the percentage.
- Warn the user if `df` isn't installed.
- Fixed broken output if `df` wasn't installed but the function was enabled.

[1] The function doesn't work on Haiku since their `df` is wildly non-standard. (The output format and flags are 100% different from all of the other `df` versions floating around.)

[2] Tested on `GNU`, `Busybox`, `BSD`, `Solaris` and `macOS` `df` versions.

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


## [2.0.2] - 2016-12-07

This minor release fixes some issues related to new features added in 2.0. These issues weren't picked up in the time between 2.0 and 2.1 and another minor release is needed due to the Packages issue being rather important.

These issues were fixed by reverting the GPU caching and Packages optimizations. These issues occurred because not enough testing was done before these were implemented in master. In the future I'll take more care with testing these larger changes before they hit the master branch and I apologize for there being yet another release in one week.

I also want to apologize to those packaging Neofetch for this unexpected release.

## Info

**Packages**<br \>
- Fixed issue where package output was off by one.

**GPU**<br \>
- Fixed bug with `--gpu_brand` not working.

**Theme**<br \>
- [Cinnamon] Fixed incorrect information.


## [2.0.1] - 2016-12-06

This release of Neofetch fixes some important bugs that were found after 2.0 was release. This includes: Detection issues on CentOS and Linux Mint systems, Incorrect Memory usage on BSD, Linux GPU detection issues and more.

This release also includes a rewrite of the screenshot functions. You no longer have to set the program to use in your config. Neofetch now automatically finds and uses whatever screenshot tool is available on your machine.

See the screenshot section below for more info.

The `get_packages()` function was optimized. Neofetch's packages function works by detecting which package managers are installed on your system and then using a sum of those as the packages output.

Previously the function would call `wc -l` for every package manager, instead we now call `wc -l` only once at the end of the function.

Thanks for reporting these bugs and also suggesting these features. Don't be shy, report any bugs, annoyances or etc with Neofetch and I'll happily help you out.

Thanks to **[@konimex](https://github.com/konimex)** for all of his contributions this release. :)

## Contributors
- **[@konimex](https://github.com/konimex)**

## General
- Use `$kernel_name` instead of `$distro` in some functions. **[@konimex](https://github.com/konimex)**

## Info

**Distro**<br \>
- Added support for Apricity OS.
- Added support for GoboLinux. **[@konimex](https://github.com/konimex)**
- Added support for SwagArch.
- Added support for AOSC OS.
- Added support for Parrot Security.
- Fixed bug that caused Linux Mint systems to be identified as Ubuntu.
- Fixed bug that caused CentOS systems to not be detected.

**Memory**<br \>
- [BSD] Fixed high memory output.

**GPU**<br \>
- [Linux] Fixed bug where sound card was detected as GPU.

**Packages**<br \>
- Only call `wc -l` once at the end of the function instead of calling it once per package manager.

**Desktop Environment**<br \>
- Show Cinnamon version.

## Image
- Changed default image mode to `ascii`.
  - See: [Images in the terminal](https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal#enabling-image-mode)

## Wallpaper
- Rewrote wallpaper function.
- Prioritize DE wallpaper setters before falling back to `feh`/`nitrogen`.
- Added support for XFCE's wallpaper setter.
- Added support for Solaris and GNU Hurd. **[@konimex](https://github.com/konimex)**

## Ascii

![ubuntu](https://u.teknik.io/zILeY.png)
<br \><sub>Old Ubuntu Logo vs New Ubuntu Logo</sub>
- Updated Ubuntu logo to the latest version.
  - You can use the old logo by launching neofetch with `--ascii_distro ubuntu_old` or by changing `$ascii_distro` to `ubuntu_old` in your config file.
- `--ascii_colors` no longer changes text colors.
- Added ascii art for Ubuntu-Budgie.
  - You can use the ascii art by launching Neofetch with `--ascii_distro ubuntu-budgie` or by changing `$ascii_distro` to `ubuntu-budgie` in your config file.
- Fixed bug causing RFRemix to use the incorrect ascii art.

## Screenshots

Neofetch will now automatically find and use whatever screenshot tool is available on your system. The screenshot tool is no longer hardcoded and you don't have to edit your config file to specify what program to use.

On Haiku and macOS, Neofetch will use the built-in tools to take screenshots. On systems with an X server Neofetch will look for and use the following programs: `scrot`, `maim`, `import (imagemagick)`, `imlib2_grab` and `gnome-screenshot`.

The config option `scrot_cmd` and the commandline flag `--scrot_cmd` are still there for those who want to use custom flags, programs or scripts to take screenshots.
- Automatically use whatever screenshot tool is available.
- Added screenshot support to macOS
- Added screenshot support to Haiku

## Screenshot Upload
- [teknik.io] Fixed images not uploading with the right filetype.
- Changed default image upload host to `teknik.io`.
  - teknik doesn't compress images whereas imgur does.
  - You can change this back to imgur by using `--image_host imgur` or by editing your config file.


## [2.0] - 2016-12-02

This is the biggest release of Neofetch in a long time. 97 files were changed with 2700~ additions to 2900~ deletions. Although the changelog isn't as interesting this time majority of the script has been rewritten, restructered and cleaned up. Every function and variable name follows a proper naming scheme and a large number of bugs were fixed.

Since this version of Neofetch differs so much from the previous versions expect a 2.0.1 release a few days later to fix any bugs that are found after release.

The ascii file handling was rewritten, ascii art is now stored/read as plain text! All `eval` usage was removed from Neofetch, vim fold markers/comments are no longer enforced and we now run on GNU Hurd, Haiku and more.

When I was rewriting parts of the script I thought to myself; Neofetch is using the bash shebang and does depend on bash so why not take full advantage of the features bash has to offer? All tests were changed from `[` to `[[`, arithmetic tests now use `(())` and C style for loops are used where possible.

All of the config file documentation was rewritten and multiple wiki pages were created to hopefully make using/configuring Neofetch easier than ever before. You can see the wiki here: [Neofetch Wiki](https://github.com/dylanaraps/neofetch/wiki)

Some of the config options/arguments were renamed/changed and Neofetch will warn you on run if you're using deprecated options (`neofetch -v`). For this release Neofetch **will** include backwards compatibility with the old config file but I'd like to remove this stuff in ~~2.1~~ 3.0. I recommend using this release with a fresh config file so that you can make use of the new documentation.

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


## [1.9.1] - 2016-11-04

This is a small release which fixes various issues found in 1.9.

Note: Those packaging neofetch can ignore the new file: `config/travis`

## Contributors
- **[@konimex](https://github.com/konimex)**
- **[@fornwall](https://github.com/fornwall)**
- **[@Head-on-a-Stick](https://github.com/Head-on-a-Stick)**

## Packages
- Neofetch is now in Termux`s repos.

## General
- [Cursor Position] Fix cursor position in URxvt when using terminal padding.
- [Termux] Fix default ascii location. **[@konimex](https://github.com/konimex)**
- [Termux] Fix default config location. **[@fornwall](https://github.com/fornwall)**
- If a function fails to detect info, let the user know in verbose mode. (`-v`)
- Removed `--test` in favor of a separate config file. Travis.ci now uses `neofetch --config travis` instead of a hacked together arg.

## Operating System
- Added support for BlankOn Linux.

## Images
- Fix division by 0 error.

## Ascii
- [Tails] Update ascii art.
- [OpenBSD] Made ascii art thinner

## Info

**Prin**<br \>
- Fix color breakage.
- Fix bold not working.

**Terminal**<br \>
- Fix whitespace error.

**Terminal Font**<br \>
- [Termite] Fix incorrect Termite font chosen.
- [Termite] Simplify `awk` command.
- [xfce4-terminal] Simplify `awk` command.

**Theme**<br \>
- [Budgie] Fix incorrect GTK Theme/Icons

**Window Manager Theme**<br \>
- [Budgie (Mutter)] Don't print WM Theme.

**Memory**<br \>
- [OpenBSD] Fixed used memory usage. **[@Head-on-a-Stick](https://github.com/Head-on-a-Stick)**


## [1.9] - 2016-11-01

This change log won't cover everything that's changed. Have a look through the commit
history for more info.

There were a lot of major changes made to how things work in this release so I'm expecting
bugs/things not working for people. Expect a 1.9.X release.

I'm also looking for neofetch screenshots for the Readme, see this issue: [#405](https://github.com/dylanaraps/neofetch/issues/405)

Thanks to everyone below who contributed, it's nice to see some new faces too. :)

## Contributors
- **[@konimex](https://github.com/konimex)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@coypoop](https://github.com/coypoop)**
- **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**
- **[@koreacomputercenter](https://github.com/koreacomputercenter)**

## General
- Added new function called `checkoldflags` which informs users about deprecated config options.
- Change all `OS X` references to `macOS`. **[@iandrewt](https://github.com/iandrewt)**
- Fix corrupted text when long lines are cut-off.
- Don't dynamically place prompt in `image=off` mode.
- Cursor Position: Fix issues when using URxvt+Padding

## Operating System

![android](https://u.teknik.io/4XdJy.png)
- Added support for Android.
  - Dependencies:
    - Required: `bash` and `busybox`
    - Note: I recommend installing `termux` from the Play Store or F-Droid. Termux provides you with a fully
      working Linux environment, doesn't require root acess and includes all dependencies.
    - Note2: Neofetch will be packaged in `termux` thanks to **[@konimex](https://github.com/konimex)**
      - PR [#351](https://github.com/termux/termux-packages/pull/531)
- Added support for Bitrig. **[@konimex](https://github.com/konimex)**
- Added support for Sparky Linux.
- Added support for Porteus. **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**
- Added support for Red Star OS. **[@koreacomputercenter](https://github.com/koreacomputercenter)**

## Packages
- Neofetch is now in Gentoo's official repos.

## Images

**Fixed rendering issues in URxvt when using an XFT font.**

![scrot](https://i.sli.mg/6qp9Cg.png)

This was first thought to be an issue between URxvt and W3m-img and I apologize for immediately closing bug reports and dismissing comments about this.

I spent yesterday trying to fix this issue and found out that launching neofetch with `--bold off`
reduced the rendering problems. I did more digging and found out that removing all text formatting fixes the issue entirely. I later found out that adding a single unformatted character before the formatted text fixed the issue while keeping the formatting the same.

I opened up this PR https://github.com/dylanaraps/neofetch/pull/358 which added options to enable a border between the image and the text to fix the issue. **[@konimex](https://github.com/konimex)** later commented informing me that we could just use a `zero-width space` to fix the issue and that we didn't need a new function/args/ugly border. doh

The final fix was as simple as adding a zero-width space before the info, here's the commit.

https://github.com/dylanaraps/neofetch/commit/3e9c3d648cb4c6f0d5fe5f0b96f9e29429af39d9

**Removed hard dependency on `\033[14t`**

Neofetch no longer requires a terminal emulator that supports `\033[14t` this means that neofetch now works in Konsole. Instead of using the escape sequence users now have three options for getting the terminal size in pixels.
- `xdotool`
- `xwininfo` + `xprop`
- `xwininfo` + `xdpyinfo`

Neofetch will detect whatever combination you have insalled and use these programs.

Note: `\033[14t` is still supported, if images already work for you then you don't have to install anything else.
- [w3m-img] Draw the image twice to fix rendering issues in Konsole.
- [w3m-img] Fix cursor position when using `yoffset`.
- [w3m-img] Add `-bg` support with the new option `--bg_color`.
  - `neofetch --bg_color blue` will make the background behind the image blue.
  - Note: The background color is only visible behind transparent parts of the image.
- If the terminal width is found as `0`, fallback to ascii mode.

## Ascii
- Bold ascii art by default.
- Fixed incorrect prompt location when using `ascii_logo_size small`.
- Fixed incorrect colors used on light terminals.
- Update Void Linux ascii art. **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**
- Update Solus ascii art.

## Info

**Distro**<br \>
- Expanded `distro_shorthand` to macOS, BSD and Solaris. **[@konimex](https://github.com/konimex)**
- Removed `osx_buildversion` and `osx_codename` in favour of `distro_shorthand`. **[@konimex](https://github.com/konimex)**

**Desktop Environment**<br \>
- [Windows] Added support for showing DE.
  - Windows 8 and above: `Modern UI/Metro`
  - Windows 7 and below: `Aero`

**Window Manager**<br \>
- [Windows] Added support for custom WMs/Shells.
  - Neofetch now detects `blackbox`, `bugn`, `Windawesome`, `emerge` and `litestep`.

**Window Manager Theme**<br \>
- [Windows] Added support for Blackbox themes.

**CPU**<br \>
- Added `cpu_speed` which lets you hide/show the speed in the output.
- Expanded `cpu_cores` option by adding two new values, `logical` and `physical`.
  - `logical`: Show all virtual cores (hyperthreaded).
  - `physical`: Only show physical cores.
- [Linux] Added support for showing CPU temperature.
  - Added new option called `cpu_temp`.
  - Note: This is disabled by default and can be enabled by changing the value of `cpu_temp` in your config to `on`.
- [macOS] Print physical cores instead of hyper-threaded cores. **[@iandrewt](https://github.com/iandrewt)**
- [iOS] Rewrite CPU function.

**GPU**
- [iOS] Rewrite GPU function.
- [Linux] Rewrite GPU function.
  - Neofetch also caches the info until reboot.

**Uptime**<br \>
- Rewrote uptime function to use seconds since boot instead of the `uptime` command.
  - Every OS/Distro now has the pretty `uptime -p` output!
- Remove `up` from output.

**Resolution**<br \>
- [macOS] Add @2x label for retina resolutions. **[@iandrewt](https://github.com/iandrewt)**

**Memory**<br \>
- [Linux] Correctly calculate used memory.
  - The output should now match `conky`, `htop` and etc.
  - Source: https://github.com/KittyKatt/screenFetch/issues/386#issuecomment-249312716
- [NetBSD] Fix memory output for sizes over 4GB. **[@coypoop](https://github.com/coypoop)**

**Shell**<br \>
- Hide shell path by default.
- Show shell version by default.

**Battery**<br \>
- [Linux] Rewrote and simplified battery function.
- Removed `battery_shorthand`
- Removed `battery_num`

**Theme Font**<br \>
- [XFCE] Fixed incorrect font output.

**Color Blocks**<br \>
- Fixed `block_width` not working.
- Fixed `% s` appearing in color blocks when neofetch is run from `tty`
- Fixed `block_width` being off by one. A value of `2` made the blocks `3` wide instead of `2` wide.

**Terminal and Terminal Font**<br \>
- [Linux] Use `/proc/$PPID/comm` instead of parsing `ps`.
- Uppercase first letter of `termfont` output.
- Don't print broken output of busybox's `ps`.
- Remove path from output.

**Song**<br \>
- [macOS] Fix iTunes automatically opening. **[@iandrewt](https://github.com/iandrewt)**
- Added support for Audacious. **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**
- Rewrote song function, it's now much faster/cleaner.


## [1.8.1] - 2016-10-04

This release fixes various bugs found in 1.8.

**General**<br \>
- Fixed issues with single args (`-s` `-su`) being treated as values for other args.

## Info

**GPU**<br \>
- Added `gpu_brand` to enable/disable showing GPU brand in output. (AMD/NVIDIA/Intel)

**DE**<br \>
- Added Cinnamon version number to output.

**WM Theme**<br \>
- Fix GNOME showing wrong WM Theme.

**Battery**<br \>
- Fixed battery not appearing when set to `all`.

**Terminal Font**<br \>
- [Termite] Ignore lines starting with `;`.

**Progress Bars**<br \>
- Fixed progress bars displaying incorrectly in image mode.

## Screenshot
- Added support for uploading screenshots to Imgur and Teknik.
  - Adds two new identical flags `--upload` and `-su`.
- Changed default screenshot name so that it works on Windows.

## Images

**General**<br \>
- Added a tiny delay before running w3m-img which suprisingly fixed all flickering issues in VTE based terminals. See [#349](https://github.com/dylanaraps/neofetch/pull/349)

**Wallpaper**<br \>
- Fix wallpapers with spaces in the filename from not showing up.

## Ascii
- Added logo mode which only displays the ascii art.
  - Adds two new identical flags `--logo` and `-L`.


## [1.8] - 2016-10-02

This version of neofetch is vastly different from the previous versions and this
changelog won't cover everything that's changed. Have a look through the commit
history for more info.

There were a lot of major changes to how things work in this release so I'm expecting
bugs/things not working for people. Depending on what comes up we my release a few 1.8.X
versions.

This changelog is a bit of a mess this time around and I apologize but it should at least
get the message across.

Android support didn't make it into this release as it requires testing on more devices.
If you've got a device running android and would like to help test out the branch, check
out the open PR here: [#322](https://github.com/dylanaraps/neofetch/pull/322)

This release also saw a lot more contributors which makes me really happy. Thanks to those
below for helping out. :)

### Contributors
- **[@hashhar](https://github.com/hashhar)**
- **[@williamkray](https://github.com/williamkray)**
- **[@dar-irl](https://github.com/dar-irl)**
- **[@gabe565](https://github.com/gabe565)**
- **[@maddcoder](https://github.com/maddcoder)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@aranega](https://github.com/aranega)**
- **[@vendion](https://github.com/vendion)**
- **[@konimex](https://github.com/konimex)**
- **[@undrskr](https://github.com/undrskr)**

### General
- Added `--version` to print the neofetch version.
- Fix issue when title and background were both color `7`.
- Fix issue with incorrect text color when `barinfo` is set.
- Fixed various Travis.ci bugs.
- Fix lint errors.
- Moved all whitespace trimming to a dedicated function.
  - Neofetch will no longer have any whitespace issues in the output.
  - See [trim()](https://github.com/dylanaraps/neofetch/commit/d3c87cdaacf1ea9fbf245146c910dc53b49dba08#diff-e863270127ca6116fd30e708cdc582fcR2789)
- Quote all variable/command substitutions.
- Removed `line_wrap` as having it set to `on` broke the output.
- Removed `stdout` mode since it's been broken for a while now and I don't see the<br\>
  point in fixing it.
- Removed in-script config in favor of sourcing the default user config.
- Remove all instances of `! -z` since they're pointless.
- Remove all `bc` usage by simplifying math.
- Suppress `getconfig` and `getscriptdir` errors.
- Suppress `xprop` errors since it's now an optional dependency.
- The prompt is now dynamically set in image mode instead of being anchored to the<br \>
  bottom of the window. See [#279](https://github.com/dylanaraps/neofetch/pull/279) and [#299](https://github.com/dylanaraps/neofetch/pull/299) for examples.
- The title at the top is now much more colorful.
- Moved commands near the bottom of the script to a new function called `main`.
- Use `read -s` instead of `stty -echo` and `stty +echo`.
- Use faster `$(())` syntax for index variables.
- `-v` now shows where the config files were sourced from.
- Cleanup
- Neofetch no longer clears the screen when run in ascii or image=off modes.
  - You can use the old behavior by aliasing `clear && neofetch` to `neofetch`.

### OS
- Added support for Windows 10 Linux subsystem. **[@konimex](https://github.com/konimex)**
- Added support for GuixSD. **[@konimex](https://github.com/konimex)**
- Added support for Devuan Linux.
- Added support for GalliumOS.
- Added support for Openwrt.
- Added support for PacBSD. **[@vendion](https://github.com/vendion)**
- Added support for Rosa.
- Added support for Solaris (Oracle / OpenIndiana). **[@konimex](https://github.com/konimex)**
- Added support for macOS Sierra. **[@iandrewt](https://github.com/iandrewt)**
- Fixed various iOS related issues.

### Packages
- Added Cydia package for iOS.
  - See https://github.com/dylanaraps/neofetch#ios-1

### Info

**Terminal and Terminal Font**<br \>

![img](https://ipfs.pics/ipfs/QmR39ScLi56Yt73pA3YWri9ayatN6mpwSTEmM8RVdeRsB1)
- Added `term` function to display current terminal emulator. [1]
- Added `termfont` function to display current terminal font. [2]

[1] Both of these functions are enabled by default.
[2] See this wiki page for more info about the functions: [Link](https://github.com/dylanaraps/neofetch/wiki/Terminal-and-Terminal-Font-detection)

**Model**<br \>
- Added `model` a new function which displays your device's product vendor/name.

![Mode](https://ipfs.pics/ipfs/Qmcy2o5xZCELxroNLHAhY96ZsrwBFR86NGDCu5e2UPVn4b)

**Distro**<br \>
- Added `distro_shorthand` **[@konimex](https://github.com/konimex)**

**Title**<br \>
- Added additional fallback which gets the current username from `$HOME`.

**Color Blocks**<br \>
- Added `--block_height` / `$block_height` to change the number of lines high each<br \>
  block will be.

![Big Blocks](https://ipfs.pics/ipfs/QmZpR8ukZNfGXkhXjTwAy3eWVRCeHdrurhgAdV5CSiTVvR)

**Resolution**<br \>
- [Windows] Fix resolution on Windows 10. **[@dar-irl](https://github.com/dar-irl)**
- [Mac OS X] Hide refresh rate if `0`. **[@iandrewt](https://github.com/iandrewt)**
- Fixed `xrandr` output on systems not using gawk.
- [Linux / BSD] Shortened refresh rate output.

**Shell**<br \>
- Show `fish` shell version. **[@maddcoder](https://github.com/maddcoder)**

**Song**<br \>
- Added support for Deadbeef. **[@konimex](https://github.com/konimex)**
- Added support for Amarok. **[@konimex](https://github.com/konimex)**
- Added support for Banshee. **[@konimex](https://github.com/konimex)**
- Added support for Rhythmbox. **[@konimex](https://github.com/konimex)**
- [Cmus] Prevent `tag artistsort` from showing up in song title. **[@williamkray](https://github.com/williamkray)**
- [Cmus] Fix order of music tags. **[@iandrewt](https://github.com/iandrewt)**
- [Cmus] The function now works on both OS X and Linux.
- [iTunes] Fix song not displaying. **[@iandrewt](https://github.com/iandrewt)**

**CPU**<br \>
- Simplify CPU Core command.

**CPU Usage**<br \>
- Fixed broken CPU usage output on BSD and Windows.
- Fixed misleading output on Linux / Mac OS X.
- Moved CPU Usage to its own dedicated function.

### Image

![terminology](https://ipfs.pics/ipfs/QmbVEUREBg4hMG22WrQ2bkt2sZZzyTEP5EEXmHRw7MHD6A)
- Added image support for terminology with `tycat`. **[@aranega](https://github.com/aranega)** [1]
- Fixed issues with lines getting drawn through images. See [#296](https://github.com/dylanaraps/neofetch/pull/296)
- Added `--crop_mode none` / `crop_mode=none` to disable cropping the images.
- Added `--size none` / `size=none` to disable resizing / cropping the images.
- Removed `image_position`
- `--image off` now behaves like the other image modes.

[1] `tycat` is a terminology builtin that works similarly to w3m-img. Those using terminology<br \>
now have working image support.

##### Shuffle mode
- Fixed directory going out of bounds causing a fallback to ascii mode. **[@gabe565](https://github.com/gabe565)**
- Simplified shuffle function.
- Path no longer requires a `/` at the end. **[@aranega](https://github.com/aranega)**

### Ascii
- Add `ascii_bold` which allows you to bold the ascii art.
- Added `--ascii_distro mac` as a shorter way of using the OS X ascii.
- Added missing `$ascii_distro` config option.
- Better `Ubuntu-GNOME` ascii art. **[@hashhar](https://github.com/hashhar)**
- Custom ascii files (`--ascii path/to/ascii_file`) now follow the same format as the<br\>
  distro ascii files. See this wiki page that explains the syntax. [Link](https://github.com/dylanaraps/neofetch/wiki/Custom-Ascii-art-file-format)
- Fix a color issue with Debian's ascii logo.
- Fix an error with an unescaped char in Windows' ascii art.
- Use a pure bash solution to getting ascii size.
- Updated Solus ascii art to match new logo. **[@undrskr](https://github.com/undrskr)**


## [1.7] - 2016-05-14

Hello, sorry this release took so long. I've been extremely busy with uni and
haven't had as much time to work on neofetch.

As always, check the `Following HEAD` wiki page for all breaking changes
this release.

I'm also looking for some new Readme screenshots, see this github issue: **https://github.com/dylanaraps/neofetch/issues/245**

### Contributers

Thanks to the following people for contributing this release.
- **[@dawidd6](https://github.com/dawidd6)**
- **[@tudurom](https://github.com/tudurom)**
- **[@iandrewt](https://github.com/iandrewt)**

### General
- Made it easier to get verbose logs.
- Added issue template for github.
- New repo for Crux. **[@tudurom](https://github.com/tudurom)**
- Added release badge to readme. **[@dawidd6](https://github.com/dawidd6)**
- Updated man page and usage with newest flags.
- Font is now enabled by default to match Screenfetch's default config.
- Fixed `bold` option not working.

### OS / Distro Support
- Added support for Kogaion Linux.
- Added support for Apple iOS. **[@iandrewt](https://github.com/iandrewt)**
  - Neofetch should now work on your iPhone, iPod and iPad.
- Added support for DragonflyBSD.
- Added support for PCBSD.

![iOS screenshot](https://ipfs.pics/ipfs/QmYmPhwpFrxwySW2phdxH1TyQ6tCgCnxtYtbEEe3RY5TwZ)

### Error Messages

Neofetch now supports displaying error messages and saving a verbose log for
troubleshooting.

![log](https://ipfs.pics/ipfs/QmeTWGKozY79zcxbrgXueyTRfQcTUe7ZmDqLv4ASgJB4G4)
- Added `-v` to print error messages to stdout.
- Added `-vv` to print a verbose log to stdout. [1]

[1] Use `neofetch -vv 2> file` to save a verbose log for bug reporting.

### Info
- Rewrote most BSD info functions, they're now much smaller and work on more
  BSD distros.

**prin**
- Format changes to fix issues with colons in string. This change also makes
  `prin` use the same args as `info`.

``` sh
# OLD Format
prin "Subtitle: Text goes here"

# NEW Format
prin "Subtitle" "Text goes here"
```

**Title**
- Made title faster by using `$HOSTNAME` when available.

**Underline**
- Fixed bug with `--underline on/off` not working.
- Underlining is no longer hardcoded to title length meaning you can now
  underline any part of the output and the length will match.
- `$underline` was renamed to `$underline_enabled`.

``` sh
# OLD Variable
underline="on"

# NEW Variable
underline_enabled="on"
```

**Distro**
- Fix arch issues with ARM cpus.
- We now use `uname -m` to get the arch instead of hardcoding `x86`.
- Moved distro detection to a function called `getdistro`.
- Fixed issue with `ascii_distro` not working.

**CPU**
- Fixed issues when cpu speed was < 1Ghz
- Cleanup of CPU function.
- Don't print `Dual-Core` or `Quad-Core` in CPU output.

**GPU**
- [Linux] More GPU substitutions for AMD cards.
- Added BSD support using `glxinfo`.

**Memory**
- [Linux / Windows] Use `memavail` if available for a more accurate output.

**Packages**
- Package count now works when the user has multiple package managers installed.
  For example, if the user has both `dpkg` and `pacman` installed the function will
  add up the packages from both package managers to get a grand total. (`dpkg pkgs` + `pacman pkgs`)

**Uptime**
- Fixed various issues with OS X and BSD.

**Desktop Environment**
- [ Linux ] Fallback to using `xprop` if `$XDG_CURRENT_DESKTOP` is empty.
- Use `$de` instead of `$XDG_CURRENT_DESKTOP` for wallpaper and theme detection.
- Fixed xprop bug with DE detection when X wasn't running.
- Don't assume that user is using MATE if marco wm is detected.

**Window Manager Theme**
- Fixed bug when `$de` was unset.

**Color Blocks**
- Fixed bug when the blocks wrap a line causing a large white strip to appear.

### Ascii
- Added KDE neon ascii art.
- Added small OpenBSD ascii art.
  - Credit goes to ufetch.
- Reduced the size of NetBSD's ascii art.
- [Windows 8/8.1] Use modern windows ascii art.

### Colors
- Fixed bug with `--colors` not working with all 256 terminal colors.
- `--colors 7` now uses the color white. [1]
- `--colors fg` now uses the foreground color. [1]

[1] Neofetch tried to be smart before by assuming that the foreground color
would be white or black. This caused issues for those setting the foreground
color to red or etc. This change adds a new value for `--colors` and `colors=()`
called `fg` which will set the color to your foreground color.

### Progress Bars
- The default progress bar look was changed to `[=====-----]` instead of `━━━━━━━━━━`
  fix issues with older systems.
- You can now enable/disable a border around the progress bars with `progress_border`.

``` sh
# $progress_border on
[=====-----]

# $progress_border off
=====-----
```
- You can now individually set the progress bar characters by using
  `progress_char_elapsed` and `progress_char_total`. This means that you can
  have a seperate character for the elapsed and total portions of the bar.

``` sh
# Examples with $progress_border on

# Elapsed: =
# Total: -
[=====-----]

# Elapsed: .
# Total: " "
[.....     ]

# Elapsed: /
# Total: " "
[/////     ]
```


## [1.6] - 2016-04-01

# Neofetch 1.6

Another ~~week~~ another release of Neofetch.

This release focused on cleanup, bug fixes and optimization. Neofetch
is now much much faster than last release and more bug free than ever
before!

This release surprisingly didn't break much at all, see the latest entry in
the wiki page `Following HEAD`.

https://github.com/dylanaraps/neofetch/wiki/Following-HEAD

![scrot](https://ipfs.pics/ipfs/QmTD6cRmYfLdrvvyLfGdUfBDCzE5uYNsRpLUx7vLUFkYxM)

### Contributors

Thanks to the following people for contributing this release.
- **[@iandrewt](https://github.com/iandrewt)**
- **[@dawidd6](https://github.com/dawidd6)**
- **[@onodera-punpun](https://github.com/onodera-punpun)**
- **[@onespaceman](https://github.com/onespaceman)**
- **[@firstEncounter](https://github.com/firstEncounter)**
- **[@konimex](https://github.com/konimex)**

### General
- Added Travis CI support.
- Added `--test` which is meant for testing and prints all functions.
- Cleanup of Distro, Uptime, Memory and CPU functions.
- We now use a more reliable white-space trimming substitution for CPU/GPU etc.
- Use `stty` instead of `read -s` to fix an issue with escape sequences<br \>
  appearing in the output.
- Line wrap is now disabled by default.
- Implement base support for caching specific info. This will eventually<br \>
  allow us to speed up the script by caching info that won't change for a<br \>
  long period of time like the CPU/GPU. [1]
- Fixed a locale issue when `LC_ALL` is unset on the user's system.
- Change all usage of `$HOME/.config` to `$XDG_CONFIG_HOME` with a fallback to `$HOME/.config`.

[1] You can clear the cache with `--clean`.

### Colors

![vs](https://ipfs.pics/ipfs/QmNVw4zm78tgBGdhDJ1FZ1aktpEtVapVtNWWMMKh5aitrZ)

<p align="center">Neofetch 1.5  vs  Neofetch 1.6</p>

<p align="center">Neofetch now works with bright color schemes and uses the foreground color instead of hard-coding white.</p>

<br \>
- Fixed buggy colors in older versions of *BSD, OS X and Linux.
- The default text colors now work on bright color schemes. We no longer force<br \>
  the color white, it's now based on your foreground color.
- Progress bars are now by default colored based on your distro's logo colors.
- Color blocks now work in older systems and in Travis CI.

### Packages
- Neofetch is now is Void Linux's official repos. **[@konimex](https://github.com/konimex)**

### Info
- Functions now no longer print `Unknown` when they fail, they now don't appear at all.

**Window Manager Theme**<br \>
- Added new `WM Theme` function to print window manager themes.

**OS**<br \>
- [ CRUX ] Also print the CRUX version. **[@onodera-punpun](https://github.com/onodera-punpun)**
- [ Fedora ] Fixed a weird detection bug.

**CPU**<br \>
- [ Windows ] Don't print CPU cores if detection fails.
- [ BSD ] Fixed extremely long output.
- Fixed broken CPU speed when source is `/proc/cpuinfo`.

**GPU**<br \>
- Don't show GPU output on unsupported OS.
- `Nvidia` is now displayed as `NVIDIA`. **[@firstEncounter](https://github.com/firstEncounter)**
- Intel GPUs now all appear as `Intel Integrated Graphics`. to avoid naming issues.
- [ OS X ] We now cache the GPU value.

**Battery**<br \>
- Show charging state in battery output. **[@dawidd6](https://github.com/dawidd6)** and **[@iandrewt](https://github.com/iandrewt)**
- [ Windows / OpenBSD ] Fix blank battery output when battery isn't found.

**Resolution**<br \>
- [ Windows ] Don't print resolution if detection fails.
- [ Linux / OSX / BSD ] Print refresh rate next to resolutions.
- [ Linux ] Multi monitor support using `xorg-xrandr`.
- [ Linux ] Refresh rate support using `xorg-xrandr`.
- [ OSX ] Added support for using `screenresolution` to print the output.<br \>
  This is much faster than the default method.

**Packages**<br \>
- Listing homebrew packages is now super fast. **[@iandrewt](https://github.com/iandrewt)**

**Public IP**<br \>
- Made public IP function faster by using `dig` if available. **[@iandrewt](https://github.com/iandrewt)**
- Each source now has a timeout to avoid a hang.
- If the IP detection fails we try another method.

**Theme**<br \>
- Use `$GTK2_RC_FILES` if the envar is set. **[@onespaceman](https://github.com/onespaceman)**

**Desktop Environment**<br \>
- Added OS X detection.

**Song**<br \>
- [ MPD ] Fixed function when mpd is running on another PC and not your own.
- Song now displays `Not Playing` instead of `Unknown` when no music player is found.
- Added support for Google Play Music Desktop Player (adds optional dependency of [`gpmdp-bash`](https://github.com/iandrewt/gpmdp-bash)) **[@iandrewt](https://github.com/iandrewt)**

**Disk**<br \>
- Added new display option `perc` to display just the percentage with the progress bar.
- [ FreeBSD ] Fixed disk usage not working.

**Memory**<br \>
- [ OpenBSD ] Fixed completely broken memory output on OpenBSD.
- [ Linux ] Rewrote memory function so that it works on old kernel versions.

**Uptime**<br \>
- [ OSX / BSD ] Performance improvements. **[@iandrewt](https://github.com/iandrewt)**
- [ OpenBSD ] Fixed duplicate `up` in output.

**Birthday**<br \>
- Fix stray `+` sign in output.

### Image
- Remove `shuffledir` in favor of '--image path/to/dir/'
- Use `printf` instead of `shuf` to pick a random image.
- [ OS X ] Fixed issues with wallpaper detection.
- [ OS X ] Wallpaper detection now works on a per desktop basis.
- Removed `image_backend` and instead use iterm2 mode only when iterm2 is detected.

### Ascii
- Added ascii art for Qubes OS.
- Added ascii art for Travis CI.
- Revamped Alpine Linux's ascii art.
- Fixed missing ascii colors for Puppy Linux.
- [ OSX ] Fixed incorrect text colors.
- Sped up ascii function by dropping `wc` usage.

### Scrot
- Fixed scrot function not using user defined options.


## [1.5] - 2016-03-17

# Neofetch 1.5

![Xubuntu](https://ipfs.pics/ipfs/QmWPvwW3nQoKVffHSZUu57MwCpQDZoMVTHQVwwCom2ChqM)

### Contributers

Thanks to the following people for helping me to improve neofetch.
- **[@iandrewt](https://github.com/iandrewt)**
- **[@konimex](https://github.com/konimex)**
- **[@CousinMachu](https://github.com/CousinMachu)**

### General
- Remove all `echo` usage inside the script.
- More cleanup and misc bug fixes.

### Packages
- Neofetch is now packaged for `Fedora` and `Fedora` based distros. **[@konimex](https://github.com/konimex)**.
- Added installation instructions for RHEL and CentOS. **[@konimex](https://github.com/konimex)**.
- Added stable package to the AUR. **[neofetch](https://aur.archlinux.org/packages/neofetch/)**

### Progress Bars

This has finally been merged to master, a big thanks to **[@iandrewt](https://github.com/iandrewt)** for helping
me finish up with this PR.

![bars](https://ipfs.pics/ipfs/Qmbj8S7pi4CVw12XTawtRwRpLvkiZ9cxRxCUPMLQ1Nhhkb)
- Added progress bar support to CPU, Memory, Disk, Battery.
- Added `progress_char` which allows you to change the character used when drawing the bars.
- Added `progress_length` which allows you to set the max length in spaces of the bars.
- Added `progress_elapsed_color` which sets the elapsed color.
- Added `progress_total_color` which sets the total color.
- Added `--progress_colors` which takes two color values: `elapsed`, `total`.
- Added `cpu_display`, `memory_display`, `disk_display` and `battery_display` which allow you<br \>
  to customize where or if the progress bar will appear.
  - Takes these values: `info`, `bar`, `infobar`, `barinfo`

### OS
- Added support for `SteamOS`.

### Images
- Using `xoffset` now also moves the text over.
- Changed default gap size to `2`.
- Fixed an issue with Nitrogen and multi monitor wallpaper setups. **[@CousinMachu](https://github.com/CousinMachu)**

### Ascii
- Kaos: Update ascii logo to the new logo.
- Added ascii logos for `Kubuntu`, `Lubuntu`, `Xubuntu` and `ubuntu-gnome`.
  - You can enable them with `--ascii_distro kubuntu`, `--ascii_distro lubuntu` and etc.

### Info

**OS**<br \>
- [ OSX ] Fix buildversion displaying regardless of on/off. **[@iandrewt](https://github.com/iandrewt)**
- [ OSX ] Added `osx_codename` (on by default) which prints the OSX codename. **[@iandrewt](https://github.com/iandrewt)**

**Disk Usage**<br \>
- Only display usage of local disks.
- Fixed disk usage progress bars when the used value was larger than the total. **[@iandrewt](https://github.com/iandrewt)**

**Theme**<br \>
- Added `/usr/share` as another theme directory to fix an issue with no theme being found. **[@iandrewt](https://github.com/iandrewt)**

**CPU**<br \>
- Added `cpu_shorthand` to shorten the output of CPU. **[@iandrewt](https://github.com/iandrewt)**
  - Takes these values: `name`, `speed`, `tiny`, `on`, `off`
- Added the ability to print the CPU Usage by using `cpu_display="info"` or `--cpu_display off/on info`.
- Added `cpu_cores` to enable/disable showing the number of CPU cores in the output. **[@iandrewt](https://github.com/iandrewt)**

**GPU**<br \>
- Added new `tiny` option to `gpu_shorthand` to further shorten the GPU output. **[@iandrewt](https://github.com/iandrewt)**

**Memory**<br \>
- Fix hang on older systems.

**Desktop Environment**<br \>
- Fixed bug where `i3` would show up as both a DE and a WM.

**Birthday**<br \>
- Fixed the birthday function on OS X, it apparently wasn't working from the start. **[@iandrewt](https://github.com/iandrewt)**

**Song**<br \>
- [ OSX ] Added Spotify support to song. **[@iandrewt](https://github.com/iandrewt)**
- [ OSX ] Added Itunes support to song. **[@iandrewt](https://github.com/iandrewt)**
- Fix bug with `song_shorthand` and songs with more than one occurence of `-`.

**Battery**<br \>
- Fixed a naming error when multiple batteries are displayed. **[@iandrewt](https://github.com/iandrewt)**

### Stdout Mode
- Fixed issues with functions that use `prin`.


## [1.4] - 2016-03-09

Lots of bugs were fixed and a lot of code was cleaned up, this changelog just lists
the major changes made to neofetch. For a full list, checkout the git commit history.

Thanks to everyone for contributing, I appreciate it!
- Renamed `fetch` to `neofetch`. Thanks for voting.
- Neofetch now has a man page. (man neofetch) Thanks **[@konimex](https://github.com/konimex)**
- Added support for `Alpine Linux`.
- Fix issue with color blocks ending up on the same line as the prompt.

### Packages
- Added Debian/Ubuntu package. Thanks **[@dawidd6](https://github.com/dawidd6)**
- Added Homebrew package for OS X. Thanks **[@iandrewt](https://github.com/iandrewt)**

### Info
- Reimplement `color` function.

**Battery**<br \>
- Added support for NetBSD

**Song**<br \>
- [Linux] Added support for Spotify.

**Birthday**<br \>
- Added `--birthday_format` and `$birthday_format` to change the date format of the<br \>
  birthday function. The flag uses the `date` cmd's format options so see `man date`<br \>
  for a list.

**Packages**<br \>
- Fix 0 package count in Slackware. Thanks **[@h3xx](https://github.com/h3xx)**

**GPU**<br \>
- Added more GPU substitutions.

Example:

``` sh
neofetch --birthday_format "%D"
neofetch --birthday_format "%a %d %b %Y %l:%M %p"
neofetch --birthday_format "%c"
```

**Theme**<br \>
- Fix incorrect theme detection on Cinnamon.

### Ascii
- Added small ascii logo variants for Arch, Crux and Gentoo. [1]
- Added new flag/option `ascii_logo_size` that takes the values `normal` and `small`.
- Optimized all ascii art fixing all leading whitespace issues.

[1] The small ascii art was taken from [ufetch](https://github.com/jschx/ufetch).

Example of small ascii logo:

![CRUX](https://ipfs.pics/ipfs/QmSpadVHtBPRBUJEiiztqkXqfhE2fuGS5t8bzsbxWUYaXA)

### Stdout
- Don't create config file when using `--stdout`.
- Simplified stdout function.
- Reimplent `--stdout_separator` and `$stdout_separator` which allow you to change<br \>
  the separator between the info.

Example:

``` sh
# Display memory, battery and disk in a single line separated by "  |  "
# This output can then be used in lemonbar etc.
neofetch --stdout memory battery disk --stdout_separator "  |  "
```


## [1.3] - 2016-02-26

# Fetch 1.3

Hey guys,

This update brought some breaking changes, see this wiki page for what you'll
need to update in your config file.

https://github.com/dylanaraps/fetch/wiki/Following-HEAD

We're in the middle of renaming 'fetch' to something else as there are
already other programs using the name and we don't appear in any searches.

You can help out by voting in our poll here:

http://strawpoll.me/6894425
- Fetch now supports **bash 3.0+**.
- More cleanup
- The text is now by default colored according to your distro's logo.
- Removed `$*_color` variables/flags in favour of a general `$colors`
  variable/flag. See my writeup here: **https://github.com/dylanaraps/fetch/pull/96**

### Image
- You no longer need to set the font_width value, your font size
  is now calculated by fetch automatically.
- Image sizing now takes terminal height into account.
- `--size` now also takes a percentage as a value, for example.

``` sh
# Image takes up 70% of the terminal size.
fetch --size 70%

# Size the image in pixels.
fetch --size 200px
```

### Packages
- Fetch now has a `crux` port. Thanks **[@ix](https://github.com/ix)**.

### OS
- Added support for `BunsenLabs`.
- Added support for `SailfishOS`. (Untested)

### Info
- Don't display Theme, Icons, Font or Window Manager if X isn't running.
- Added function to show currently logged in users.

**Window Manager**
- Add support for Wayland window managers. (Hardcoded)

**Song**
- Added `song_shorthand` which prints the Artist/Title on seperate lines.

**Theme**
- Windows Visual Style is now a part of `getstyle`.
- Disabled theme output on OS X to fix a `gsetttings` related crash.
- Uppercase the first letter of the theme.

**Resolution**
- Added Windows support.
- Enabled by default but only displays info if the dependency is found.

**Battery**
- Added FreeBSD and OpenBSD support. Thanks **[@tudurom](https://github.com/tudurom)**.

**GPU**
- Added more substitutions/

### Stdout

Printing to stdout in a plaintext format for use in scripts is now
much faster and cleaner.
- Removed `--stdout_separator` (Separator is now 2 spaces)
- Removed `--stdout_subtitles`
- Removed `--stdout_title`


## [1.2] - 2016-02-17

# Fetch 1.2

This new release comes with a few config breaking changes, see this wiki page
for info on how you can workaround the issues.

https://github.com/dylanaraps/fetch/wiki/Following-HEAD
- Fetch now has a **gitter** chatroom. [![Gitter](https://badges.gitter.im/dylanaraps/fetch.svg)](https://gitter.im/dylanaraps/fetch?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
- Fixed text padding when the user didn't have the locale `en_US.UTF8` installed.
- Cleaned up parts of the script.

### OS

We now support almost all the Linux distros Screenfetch supports excluding
the distros that have been discontinued.

Added support for these distros:
- `Puppy Linux`
- `Kali Linux`
- `openSUSE`
- `Raspbian`
- `Mageia`
- `PCLinuxOS`
- `Zorin OS`
- `Tails`
- `BLAG`
- `Void Linux`
- `Trisquel`
- `Solus`
- `Peppermint`
- `NixOS`
- `Chakra`
- `Mandriva`
- `gNewSense`
- `LMDE`
- `KaOS`
- `Sabayon`
- `Frugalware`
- `Chapeau`
- `Slackware`
- `Scientific Linux`
- `Exherbo`
- `Chrome OS`
- `Chromium OS`

### Makefile
- Fixed makefile on OS X El Captain.
- `$PREFIX` is now also used when installing ascii art and the default config

### Wallpaper
- Fetch now supports using `MATE` desktop's wallpapers.
- Fetch now fallsback to ascii mode if the found wallpaper is an xml file. This
  fixes issues where the wallpaper set by gsettings is an xml file.

### Info

**Desktop Environment**:
- Added support for showing the user's DE.

**Window Manager**:
- `xprop` is now a required dependency. See **[#79](https://github.com/dylanaraps/fetch/pull/79)**.
- Renamed 'windowmanager' to 'wm'

**IP Address**:
- Added function to get your local IP
- Added function to get your public IP [1]
- Added `--ip_host` and `$public_ip_host` which allow you to change the website we
  ping for the public IP.

[1] Public IP requires an internet connection as we ping a website.

**Packages**:
- Check for packages based on which package manager is installed instead of
  using a hardcoded list of distros.

**Theme**:
- Added support for getting DE theme.
- Added support for getting KDE theme.
- Renamed `getgtk` to `getstyle`.
- Dropped the `gtk` from these printinfo functions `gtktheme`, `gtkicons`
  and `gtkfont`. Theme output will be blank until you make these changes:

``` sh
# Old Naming
info "GTK Theme" gtktheme
info "Icons" gtkicons
info "Font" gtkfont

# New Naming
info "Theme" theme
info "Icons" icons
info "Font" font
```

**GPU**:
- `gpu_shorthand` is now enabled by default.
- We now favor showing the dedicated GPU over the integrated one.

**Song**:
- Added support for `MOC`.
- We now check to see if the player is running before printing anything.
- We now check playback state and show it if relevent.

**Uptime**:
- [Linux] Fixed uptime when it's under 1 minute.

### Ascii Art
- `--ascii_distro` now also enables ascii mode.
-  Fix missing ascii art when fetch is installed in /usr/local
- Update Deepin's ascii art to their new logo


## [1.1] - 2016-02-06

# Fetch 1.1 changelog

Over the past 10~ days over **190** more commits have been pushed to master and the
script has had some big changes. Thanks to everyone who has contributed, you've been
a big help.

![screenfetch mode](http://i.imgur.com/nW3HiNP.png)
<sup>New screenfetch mode</sup>
- If `w3m` or `imagemagick` aren't installed we gracefully fallback to ascii mode.
- Automatically find the `w3m-img` path and fallback to ascii mode if not found. [1]
- Fix padding escape codes on BSD systems.
- Swap escape codes from `\e` to `\033` for consistency.
- We only move the cursor to the bottom of the terminal in w3m/iterm2 rendering modes.
- Cursor position is now dynamic in ascii mode based on the height of the ascii and info text.
- If images and ascii are off, don't clear the terminal
- The script now exits correctly instead of always exiting with status code `1`
- If the script exits for any reason, unhide the cursor.
- Removed duplicate blocks inside `getcpu` and `getmemory`.
- Removed `--colors` as it was apparently broken from day 1.
- Usage has been reformatted so that every flag has a value.

[1] Setting `$w3m_img_path` will make the script look there first.

### Image
- Added support for displaying ascii art inside of text files.
- Added "screenfetch mode" which will display your distro's ascii art next to the info. [1]
- Added `--ascii_distro` to choose which distro's ascii logo to display.
- Added `--ascii_colors` and `$ascii_colors` which allow you to change the colors of the ascii art
  and distro logos. [2]
- Added `--size` and `$image_size` to set the image size in pixels.
- Rename `--shuffledir` and `$shuffledir` to `shuffle_dir`.
- Rename `--imgtempdir` and `$imgtempdir` to `thumbnail_dir`
- Removed `--split_size` and `$split_size` as they were weird and confusing to use.
- Default thumbnail directory is now `$HOME/.cache/thumbnails/fetch`. Thanks @tudurom
- If `--image` and `--ascii` are left empty we fallback to ascii distro mode.

Example usage of ascii from file:

``` sh
fetch --ascii "path/to/ascii" --ascii_color 2

```

[1] **[How do I enable screenfetch mode?](http://github.com/dylanaraps/fetch#how-do-i-enable-screenfetch-mode)**
[2] `ascii_colors` takes a range of colors which allows you to color every aspect of
distro and OS ascii art. For custom art the script will color the entirety of it using
the first value of `ascii_colors`. If `ascii_colors` is left empty, color will be disabled.

### Config file
- Fetch now has a config file that you can share with people and keep between
  script versions! [1]
- Added `--config` and `$config_file` to specify a custom config location.
- Added `--config off`, `--config none` and `$config` to enable / disable config files
  at launch or in script.

[1] https://github.com/dylanaraps/fetch#using-the-config-file

### Makefile
- Fetch now has a make file due to the increasing number of files,
  this allows the script to be easily installed and uninstalled on
  systems it isn't packaged for yet! [1]

[1] The script will still work just fine on its own, you'll just be missing
the distro ascii art and the automatic config creation.

### Packages
- Fetch now has a Gentoo/Funtoo e-build courtesy of **@z1lt0id**

### Stdout
- Added `stdout` mode which allows you to fetch info in a plain text format that works
  with lemonbar and in your scripts. You can use it by launching fetch with `--stdout` to print all
  functions enabled in your `printinfo` function. You can selectively print functions by passing
  arguments to `--stdout` like so:

``` sh
# Print the output of all info functions enabled in printinfo
fetch --stdout

# Print the output of memory
fetch --stdout memory

# Print the output of memory and disk
fetch --stdout disk

# Print the output of all functions excluding x
fetch --stdout --disable kernel packages gtktheme

```
- Added `--stdout_separator` and `$stdout_separator` which takes a string and adds it
  as a separator between the output.
- Added `--stdout_title` and `$stdout_title` which allow you to toggle the `title@hostname`
  from appearing in the output.
- Added `--stdout_subtitles` which allow you to toggle the `Info:` titles from appearing in
  the output.

``` sh
# Hiding subtitles
fetch --stdout --stdout_subtitles off

# Custom separator
fetch --stdout disk gpu --stdout_separator "  |  "

```

**NOTE:** `stdout_subtitles` and `stdout_title` only work when `--stdout` is used on its own
without any args.

### Info
- You can now display info without a subtitle. eg. `info memory`
- Added `--disable` which allows you to stop an info line from appearing at launch.
- Added `--underline` and `$underline` which allow you to toggle visibility of the
  underline at launch and in your config.

``` sh
# Stop cpu, gpu, disk and shell functions from being called
fetch --disable cpu gpu disk shell
```

**Kernel:** Added `--kernel_shorthand` and `$kernel_shorthand` to print less or more kernel info
**Window Manager:** Added support for `$XINITRC`
**GTK:** Fix incorrect GTK3 theme being displayed
**CPU:** `cpu_shorthand`: New substitutions
**GPU:** `[Linux]` Count the number of identical GPUs. eg. `Nvidia Geforce GTX 970 x 2`
**Memory:** `[Mac OS X]` Added wired memory to memory usage.

**Distro:**
- Added support for showing OS architecture. eg `Arch Linux x86_64`, `Windows 7 Ultimate 64-bit` [1]
- Mac OS X: Added support for showing Max OS X build version. [2]
- Windows: Distro now displays Windows edition. eg. `Windows 7 Ultimate`

[1] You can toggle this using `--os_arch` and `$os_arch`.
[2] You can toggle it using `--osx_buildversion` and `$osx_buildversion`.

**Shell:**
- Added `--shell_version` and `$shell_version` to hide/show your shell's version.
- Added `--shell_path` and `$shell_path` to hide/show the path to your shell

**Birthday:**
- Added `birthday` which prints the age of your OS install.
- Added `--birthday_shorthand` and `$birthday_shorthand` to shorten/lengthen
  the output of birthday.
- Added `--birthday_time` and `$birthday_time` to show/hide the time in the output.

**Battery:**
- Added `battery` which prints the battery usage percentage for each battery
  in your system.
- Linux: Added `battery_num` which allows you to choose which battery to display,
  it also takes the value `all` which will print all batteries line by line.
- Linux: Added `battery_shorthand` which when set to `on` prints each battery on the
  same line like so:

``` sh
# battery_shorthand="on"
Battery: 10%, 5%, 67%

# battery_shorthand="off"
Battery0: 10%
Battery1: 5%
Battery2: 67%

# If there's only a single battery in the system
# we ommit the numbered title.
Battery: 10%
```
- **NOTE:** This currently doesn't support BSD systems as we have no one to help us test
  - See **[Issue #46](https://github.com/dylanaraps/fetch/issues/46)**


## [1.0] - 2016-01-27

# Fetch 1.0

There have been over **260** commits to master since I last made a release
and the script is at a point now where I can say that it's feature complete
so I'm releasing 1.0. The script now supports many more OS/distros and has
had lots of bug fixes, changes and features added.

I'm probably missing a bunch of stuff from this changelog so if i've
forgotten anything, let me know!

I'm also slowly adding pages to the wiki so check it out!

# Here's what's new:
- Added full support for **Windows**, **BSD** and **Mac OS X**.
- Fetch is now MIT licensed
- Dropped the `.sh` from the filename and title.
- Dropped support for `mksh` so we can support some `bash` only features.
- Cleanup of everything
- Added `--prompt_height` and `$prompt_height` to fix the script going<br \>
  offscreen due to multi-line shell prompts. This option should be set to<br \>
  your prompt height in lines.
- The script now supports bash **4.0**. It turns out that we only<br \>
  supported bash **4.3**
- Restore cursor and clear screen on ctrl+c.
- Swap `tput` cmds for `ansi escape sequences` where possible.
- Added folds to make the script easier to navigate in *vim.
- Added `-F` to grep where possible for a speedup where possible.
- Fix whitespace issues with different distros.
- Remove uneeded `$` symbols.
- Remove double negative tests.
- Added note about needing `procps` or `procps-ng` for uptime support.
- Fix syntax errors in script and readme.
- All vars now use `on/off` instead of `1/0`.
- Quote things that should be quoted.

**Linux:**
- Fix issues with `Elementary OS` and `CentOS`.

**Mac OS X:**
- Added support for other package managers.
- Fix issue with multiple resolutions in `getresolution`

**Windows:**
- Added `getvisualstyle` function to get the current Windows theme.
- Added `choclatey` support to package count.

**BSD:**
- Fix tput commands not working on BSD

## Info:

As of commit 9daacdd the info array at the top of the script has changed
to a regular function. The benefits of this are pretty cool, you can now
use any bash syntax to customize what gets displayed. You could have an
if statment and only print window manager and gtk themes if X is running
or only show current song if there's one playing.

You can see some examples and read more about it here:

https://github.com/dylanaraps/fetch/wiki/Customizing-Info

<hr>

**All:**
- All functions return `Unknown` or `None` instead of printing nothing.<br \>

**Title:**
- You can now color the `@` symbol in the title using `--at_color`,<br \>
  `$at_color` and `--colors x x x x x x`.

**OS:**
- We now check `lsb_release` before looking inside of files, this fixes<br \>
  detection for some *buntu based distros.
- We now exit if the OS type wasn't detected.

**Window Manager:**
- `wmctrl` is now used by default if found.

**Uptime:**
- Added `--uptime_shorthand` and `$uptime_shorthand` to make the output<br \>
  of `uptime` smaller and prettier.
- Added new `--uptime_shorthand` and `$uptime_shorthand` value<br \>
  called `tiny`. This makes the output even tinier. eg. `1d 10h 32m`

**GTK:**
- Added functions to get GTK Theme, Icons and Font
- Added `--gtk{2,3}` and `$gtk{2,3}` to enable/disable gtk2 or gtk3 from<br \>
  being displayed.
- Added `--gtk_shorthand` and `$gtk_shorthand` to make the output of<br \>
  `gtk*` smaller and prettier.

**Packages:**
- Remove package version and color from `Pacman` output
- All distros are now wildcarded so that version numbers from<br \>
  `lsb_release` are ignored.

**CPU:**
- Added more cpu speed types to `--speed_type` and `$speed_type`.
- Use `cpufreq` when available instead of hardcoding it for specific distros.

**GPU:**

See **[issue #21](https://github.com/dylanaraps/fetch/issues/21)**
- Added function to get the current Graphics Card.
- Added support for VirtualBox GPU.
- Added `--gpu_shorthand` and `$gpu_shorthand` to make the output of `gpu`<br \>
  smaller and prettier.

**Disk:**

See **[issue #27](https://github.com/dylanaraps/fetch/issues/27)**
- Added function to get current/total disk usage.

**Song:**
- Added `cmus` support.

## Images:
- Added support for **iTerm2's** image rendering.
- Added `--image_backend` and `$image_backend` to change which program<br \>
  is used to render the images.
- The image is now displayed **before** the text, this fixes image<br \>
  rendering issues with **vte** based terminal emulators.
- Added `$w3m_img_path` to set the location of `w3mimgdisplay`.
- Unified all image options, the new var `$image` takes these<br \>
  values: `wall`, `shuffle`, `path/to/img.png`, `off`.
- Added `shuffle` to image modes. The script can now pick a random<br \>
  image from a specified folder to display. You can pick the shuffle<br \>
  directory with `--shuffle_dir` and `$shuffle_dir`
- Fixed images getting cut off at the top.
- Added image size to filename which allowed us to remove a _really_<br \>
  slow check.

**Wallpaper:**
- Added `nitrogen` and `gsettings` support.
- Added wallpaper support to `Mac OS X` and `Windows`.
- Fix hang when wallpaper isn't found.
- We now check to see that `feh` set the wallpaper.
- Fixed wallpapers with spaces in the filename.
- `wall` is now the default image source.

## Screenshot:

The script can now take a screenshot on script finish. You can use
the flags `--scrot` or `-s` to take a screenshot.

`--scrot` and `-s` can also take a path/filename so you can choose
where and what to name the file at launch.

If left empty `--scrot` and `-s` will use `$scrot_dir` and
`$scrot_name` when saving the screenshot.

By default the script uses `scrot` as the screenshot program.
You can use the launch flag `--scrot_cmd` or the option `$srot_cmd`
to set the program to use to take the screenshot.

## Wiki:

Added `Customizing Info` page which has info/examples about
the new printinfo function.

https://github.com/dylanaraps/fetch/wiki/Customizing-Info

Added `Customization` which lists all options and their values.

https://github.com/dylanaraps/fetch/wiki/Customization


## [0.2.1] - 2016-01-04

Here's what's new:
- Mac OS X support (It's done now)
- Resolution Detection (Off by default)
- Song info is now off by default.
- You can now display the image on the right with:
  - `--image_position left/right`
- Fixed bug with multiple colons
- Fixed underlines not being drawn the full width.
- Functions now fallback to "Unknown" instead of printing nothing.
- `getos` now gets os type and `getdistro` gets the distro.
  - This makes it even easier to add other os types.

Here's what I'm working on:
- Finishing OpenBSD support
- Cygwin support

Enjoy


## [0.2] - 2016-01-03

I finished my rewrite!

## Here's what's new:
- The script is now way faster.
- You can now pick what gets displayed and where using an array
  at the top of the script. This also allows you to:
  - underline anything
  - print custom info
  - print a custom title
  - add linebreaks
- Mac OS X support and a base that allows us to add other OS later.
- You can now specify split size.
- Fixed issue with 2 line prompts
- Fixed image not displaying in vte based terminals
- Move all config options to the top of the script
- Moved almost everything to a function.
- Removed wmctrl dependency
- Made variable names more consistent
- Added shell substitution for cpu output. This means
  that the cpu output won't include: (tm) (r) "Processor" "CPU"
- Optimized all get\* functions
- Use variable substitution where possible as it's faster than sed/awk
- Moved crop and smart_crop to crop_mode
- Removed --size and --padding in favor of --split_size

## Here's what I'm currently working on:
- Window support (I'm almost done)
- Option to swap the image and text around
- Imagemagick optimizations
- Cleanup of info array handling
- More info outputs. Now that it's easy to customize what's printed and
  everything is a function we can add optional support for pretty much anything.
  - Resolution
  - GTK themes
  - Terminal Font
  - GPU
  - IP
  - etc

## Issues:
- Uptime doesn't work in OS X yet.
- If the customizable info includes a third colon then it breaks.

I'd love to hear your thoughts.


## 0.1 - 2015-12-31

Changelog:
- Added flag to disable bold text `--nobold`
- Added flag to disable text wrapping `--nowrap`
- Moved to using only printf instead of a mix of echo/printf
- The script now aligns the cursor to the bottom of the
  terminal instead of using a hardcoded amount of newlines
- Image size and padding is now dynamic, the only difference on the user
  side is that instead of setting a long line of spaces as
  padding, you set your font width. This means that you set the
  var once and the script will just work at any window size.
- You can disable dynamic images and go back to the old
  behaviour with by using the `--size` or the in config var.
  $img_auto
- Manual padding now takes a count, so `--padding 10` will pad
  the text 10 spaces.
- tput is now a dependency because we need (tput cols/lines/cup)
  for the dynamic images and it allows us to support more terminals.
- Color block width can now be changed with the flag `--blockwidth`.
  It takes a count like `--padding` so `--blockwidth 10` will make
  the color blocks 10 spaces wide.

Let me know if you're having issues.


[Unreleased]: https://github.com/dylanaraps/neofetch/compare/5.0.0...HEAD
[5.0.0]: https://github.com/dylanaraps/neofetch/compare/4.0.2...5.0.0
[4.0.2]: https://github.com/dylanaraps/neofetch/compare/4.0.1...4.0.2
[4.0.1]: https://github.com/dylanaraps/neofetch/compare/4.0.0...4.0.1
[4.0.0]: https://github.com/dylanaraps/neofetch/compare/3.4.0...4.0.0
[3.4.0]: https://github.com/dylanaraps/neofetch/compare/3.3.0...3.4.0
[3.3.0]: https://github.com/dylanaraps/neofetch/compare/3.2.0...3.3.0
[3.2.0]: https://github.com/dylanaraps/neofetch/compare/3.1.0...3.2.0
[3.1.0]: https://github.com/dylanaraps/neofetch/compare/3.0.1...3.1.0
[3.0.1]: https://github.com/dylanaraps/neofetch/compare/3.0...3.0.1
[3.0]: https://github.com/dylanaraps/neofetch/compare/2.0.2...3.0
[2.0.2]: https://github.com/dylanaraps/neofetch/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/dylanaraps/neofetch/compare/2.0...2.0.1
[2.0]: https://github.com/dylanaraps/neofetch/compare/1.9.1...2.0
[1.9.1]: https://github.com/dylanaraps/neofetch/compare/1.9...1.9.1
[1.9]: https://github.com/dylanaraps/neofetch/compare/1.8.1...1.9
[1.8.1]: https://github.com/dylanaraps/neofetch/compare/1.8...1.8.1
[1.8]: https://github.com/dylanaraps/neofetch/compare/1.7...1.8
[1.7]: https://github.com/dylanaraps/neofetch/compare/1.6...1.7
[1.6]: https://github.com/dylanaraps/neofetch/compare/1.5...1.6
[1.5]: https://github.com/dylanaraps/neofetch/compare/1.4...1.5
[1.4]: https://github.com/dylanaraps/neofetch/compare/1.3...1.4
[1.3]: https://github.com/dylanaraps/neofetch/compare/1.2...1.3
[1.2]: https://github.com/dylanaraps/neofetch/compare/1.1...1.2
[1.1]: https://github.com/dylanaraps/neofetch/compare/1.0...1.1
[1.0]: https://github.com/dylanaraps/neofetch/compare/0.2.1...1.0
[0.2.1]: https://github.com/dylanaraps/neofetch/compare/0.2...0.2.1
[0.2]: https://github.com/dylanaraps/neofetch/compare/0.1...0.2

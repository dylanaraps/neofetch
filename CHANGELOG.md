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
- Added suport for openSUSE Tumbleweed. [**@robertwolter**](http://github.com/robertwolter)
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
- Added new DragonflyBSD log. [**@MitchWeaver**](https://github.com/MitchWeaver)


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

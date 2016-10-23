## Contributors

- **[@konimex](https://github.com/konimex)**
- **[@iandrewt](https://github.com/iandrewt)**
- **[@coypoop](https://github.com/coypoop)**
- **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**

<br \>

## General

- Added new function called `checkoldflags` which informs users about deprecated config options.
- Change all `OS X` references to `macOS`. **[@iandrewt](https://github.com/iandrewt)**
- Fix corrupted text when long lines are cut-off.
- Don't dynamically place prompt in `image=off` mode.
- Cursor Position: Fix issues when using URxvt+Padding 


## Operating System

- Added support for Bitrig. **[@konimex](https://github.com/konimex)**
- Added support for Sparky Linux.
- Added support for Porteus. **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**


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


## Ascii

- Bold ascii art by default.
- Fixed incorrect prompt location when using `ascii_logo_size small`.
- Update Void Linux ascii art. **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**


## Info

**Distro**<br \>

- Expanded `distro_shorthand` to macOS and Solaris. **[@konimex](https://github.com/konimex)**
- Removed `osx_buildversion` and `osx_codename` in favour of `distro_shorthand`. **[@konimex](https://github.com/konimex)**

**Desktop Environment**<br \>

- [Windows] Added support for showing DE.
    - Windows 8 and above: `Modern UI/Metro`
    - Windows 7 and below: `Aero`

**Window Manager**<br \>

- [Windows] Added support for custom WMs/Shells.
    - Neofetch now detects `blackbox`, `bugn`, `Windawesome`, `emerge` and `litestep`.
- Uppercase first letter of `wm` output.

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

**Uptime**<br \>

- Rewrote uptime function to use seconds since boot instead of the `uptime` command.
    - Every OS/Distro now has the pretty `uptime -p` output!

**Resolution**<br \>

- [macOS] Add @2x label for retina resolutions. **[@iandrewt](https://github.com/iandrewt)**

**Memory**<br \>

- [Linux] Correctly calculate used memory.
- [NetBSD] Fix memory output for sizes over 4GB. **[@coypoop](https://github.com/coypoop)**

**Shell**<br \>

- Hide shell path by default.
- Show shell version by default.

**Theme Font**<br \>

- [XFCE] Fixed incorrect font output.

**Color Blocks**<br \>

- Fixed `block_width` not working.
- Fixed `% s` appearing in color blocks when neofetch is run from `tty`
- Fixed `block_width` being off by one. A value of `2` made the blocks `3` wide instead of `2` wide.

**Terminal and Terminal Font**<br \>

- Uppercase first letter of `term` and `termfont` outputs.
- Don't print broken output of busybox's `ps`.
- Remove path from output.

**Song**<br \>

- [macOS] Fix iTunes automatically opening. **[@iandrewt](https://github.com/iandrewt)**
- Added support for Audacious. **[@ncmprhnsbl](https://github.com/ncmprhnsbl)**

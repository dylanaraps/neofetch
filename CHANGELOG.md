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


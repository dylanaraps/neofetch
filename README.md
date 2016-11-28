# Neofetch

[![Gitter](https://badges.gitter.im/dylanaraps/fetch.svg)](https://gitter.im/dylanaraps/fetch?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Build Status](https://travis-ci.org/dylanaraps/neofetch.svg?branch=master)](https://travis-ci.org/dylanaraps/neofetch) [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) [![Latest release](https://img.shields.io/github/release/dylanaraps/neofetch.svg)](https://github.com/dylanaraps/neofetch/releases)

Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ascii file of your choice. The main purpose of neofetch is to be used in screenshots to show other users what OS/Distro you're running, what Theme/Icons you're using and etc.

Neofetch is highly customizable through the use of commandline flags or the user config file. There are over 50 config options to mess around with and there's the `print_info()` function and friends which let you add your own custom info.

Neofetch can be used on any OS that has BASH, it's just a matter of adding support. If your OS/Distro isn't in the list below, feel free to open an issue on the repo and I'll gladly add support. Neofetch currently supports `Linux`, `MacOS`, `iOS`, `BSD`, `Solaris`, `Android`, `Haiku`, `GNU Hurd` and `Windows (Cygwin/Windows 10 Linux subsystem)`. 

For more information:

**https://github.com/dylanaraps/neofetch/wiki**

![1](https://ipfs.pics/ipfs/QmTtF9Sx8o617QE88GH3Z4yX7mRyi4yS1hsMHyRVmn14vJ)


## Dependencies

https://github.com/dylanaraps/neofetch/wiki/Dependencies


## Installation

https://github.com/dylanaraps/neofetch/wiki/Installation


## Post Install


### Using the config file

Neofetch will by default create a config file at `$HOME/.config/neofetch/config` and this file contains all of the script's options/settings. The config file allows you to keep your customizations between script versions and allows you to easily share your customizations with other people.

You can launch the script without a config file by using the flag `--config none` and you can specify a custom config location using `--config path/to/config`.


### Customizing what info gets displayed

https://github.com/dylanaraps/fetch/wiki/Customizing-Info


### Customizing the script using a custom alias

If you don't want to use the config file you can customize almost everything using launch flags!

Here's an example neofetch alias:

```sh
alias neofetch2="neofetch \
--config off \
--block_range 1 8 \
--bold off \
--uptime_shorthand on \
--gtk_shorthand on \
--colors 4 1 8 8 8 7 \
"
```


## Frequently Asked Questions


### How do I enable screenfetch mode?

Launching the script with `--ascii` or setting `image="ascii"` inside the config file will launch the script in "screenfetch mode". The script will display your distro's ascii next to the info, exactly like screenfetch.

**NOTE:** If you **don't** have an image-mode dependency installed screenfetch mode will be used automatically.

### Why doesn't Neofetch support my wallpaper setter?

It's hard to add support for other wallpaper setters as they don't provide a way of getting the current wallpaper from the cli.

If your wallpaper setter **does** provide a way of getting the current wallpaper or you know where the wallpaper is stored then adding support won't be a problem!


## Issues and Workarounds

### getgpu doesn't show my exact video card name

If your `lspci | grep "VGA"` output looks like this:

```
01:00.0 VGA compatible controller: NVIDIA Corporation Device 1401 (rev a1)
```

Instead of this:

```
01:00.0 VGA compatible controller: NVIDIA Corporation GM206 [GeForce GTX 960] (rev a1)
```

Then you're affected by the issue.

This is caused by your `/usr/share/misc/pci.ids*` files being outdated and you can fix it by running this command as root.

```
sudo update-pciids
```

### Neofetch doesn't work correctly with ConEmu.

You need to be using the CYGWIN/Msys connector for Neofetch to work seamlessly with ConEmu.

https://conemu.github.io/en/CygwinMsysConnector.html


## Thanks

Thanks to:

- [Screenfetch](https://github.com/KittyKatt/screenFetch):
    - I've used some snippets as a base for a few functions in this script.
    - Some of the ascii logos.
- [ufetch](https://github.com/jschx/ufetch):
    - Tiny ascii logos
- Everyone else helped out in one way or another. I'd list all of the names but there's just too many of you. :)

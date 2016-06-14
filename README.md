# Neofetch

[![Gitter](https://badges.gitter.im/dylanaraps/fetch.svg)](https://gitter.im/dylanaraps/fetch?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Build Status](https://travis-ci.org/dylanaraps/neofetch.svg?branch=master)](https://travis-ci.org/dylanaraps/neofetch) [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) [![Latest release](https://img.shields.io/github/release/dylanaraps/neofetch.svg)](https://github.com/dylanaraps/neofetch/releases)

This is the home of my fetch script! This script gathers info <br />
about your system and prints it to the terminal next to an image, <br \>
your distro's logo or any ascii art of your choice!

Have a look at the wiki, I've updated/added some new pages!<br \>
**https://github.com/dylanaraps/neofetch/wiki**

![1](https://ipfs.pics/ipfs/QmTtF9Sx8o617QE88GH3Z4yX7mRyi4yS1hsMHyRVmn14vJ)


<!-- Table of Contents {{{ -->


## Table of Contents

- [Screenshots](#screenshots)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
    - [Arch Linux](#arch)
    - [Gentoo / Funtoo](#gentoo--funtoo)
    - [CRUX](#crux)
    - [Ubuntu](#ubuntu)
    - [Debian](#debian)
    - [Fedora / RHEL / CentOS](#fedora--rhel--centos)
    - [Void Linux](#void-linux)
    - [BunsenLabs](#bunsenlabs)
    - [Mac OS X](#mac-os-x)
    - [Others](#others)
- [Post Install](#post-install)
- [Usage](#usage)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Issues and Workarounds](#issues-and-workarounds)
- [Thanks](#thanks)


<!-- }}} -->


<!-- Screenshots {{{ -->


## Screenshots

![Linux](https://ipfs.pics/ipfs/QmRRYwcSRz1FHNx8VQiBixZq3qvBNk487fKGwUNTs7GQjA)
![Windows](https://ipfs.pics/ipfs/Qmf5GpmqnMRhEzC1qoQ2tM4699tEXLManZTs5pz4mWJbCg)
![Mac OS X](https://ipfs.pics/ipfs/QmWA8XX6pFkEuLLcrq5JZBx1KFEUaXanTy1jMxzKVRpwaT)
![bsd](https://ipfs.pics/ipfs/QmSpyCGzSgYnyfbMetKqxy9cU3UFbneS3G8JrbdxkiNLgm)
![bsd](https://ipfs.pics/ipfs/QmeZhs3CwGtM8CSVoorA2d2CqLxRzbJkdD7aYxa4Dixsea)


<!-- }}} -->


<!-- Features {{{ -->


## Features

- Supports **Linux**, **Mac OS X**, **iOS**, **BSD** and **Windows** (Cygwin)
- Display a **full color image**, a file containing **ascii art** or your **distro's logo** in ascii next to the info.
- The script is **fast**. We use bash builtins wherever possible and only spawn external processes when necessary.
- Take a screenshot of your desktop on script finish.
- Customize **which** info is displayed, **where** it's displayed and **when** it's displayed.
    - See this **[wiki page](https://github.com/dylanaraps/neofetch/wiki/Customizing-Info)**


<!-- }}} -->


<!-- Dependences {{{ -->


## Dependencies

### Required dependencies:

- `Bash 3.0+`
    - Alpine Linux: You also need `ncurses`.


##### Windows (CYGWIN)

- `procps-ng` or `procps`

##### iOS

These dependencies can all be installed through Cydia.

- `Bourne-Again SHell`
- `Core Utilities`
- `Core Utilities (/bin)`
- `Darwin Tools`
- `system-cmds`
- `bc`
- `Gawk`
- `grep`

### Optional dependencies:

- Desktop Environment and Window Manager: `xprop` \[1\]
- Displaying images: `w3m-img` \[2\] \[3\] or `iTerm2` or `Terminology` \[4\]
- Thumbnail creation: `imagemagick`
- Displaying song information from Google Play Music Desktop Player: [`gpmdp-remote`](https://github.com/iAndrewT/gpmdp-remote)

##### Linux / BSD

- Wallpaper: `feh`, `nitrogen` or `gsettings`
- Current Song: `mpc`, `cmus`, `moc`, `spotify`, `gpmdc`
- Resolution: `xorg-xrandr` or `xorg-xdpyinfo` \[5\]
- Screenshot: `scrot` \[6\]

##### OSX

- Resolution (quicker): `screenresolution`

##### BSD

- GPU: `glxinfo`
    - Not required on FreeBSD.

\[1\] See **[#79](https://github.com/dylanaraps/neofetch/issues/79)** about why this is now a required dependency.

\[2\] `w3m-img` is sometimes bundled together with `w3m`.

\[3\] Image support only works in certain terminal emulators. The script will fallback to ascii mode on<br \>
terminal emulators that don't support the xterm escape sequences we're using for image sizing.

\[4\] Image support is built into Terminology and iTerm2, and doesn't require w3m-img.

\[5\] Xrandr is prefered over xdpyinfo as Xrandr supports multi monitor and refresh rate display in the<br \>
output.

\[6\] You can use the launch flag `--scrot_cmd` or change the config option `$scrot_cmd` to your screenshot<br \>
program's cmd and neofetch will use it instead of scrot.


<!-- }}} -->


<!-- Installation {{{ -->


## Installation

Those using a git version of neofetch should check this page after<br \>
updating, this page lists any breaking changes that were made and<br \>
how you can workaround them.

https://github.com/dylanaraps/neofetch/wiki/Following-HEAD

- [Arch Linux](#arch)
- [Gentoo / Funtoo](#gentoo--funtoo)
- [CRUX](#crux)
- [Ubuntu](#ubuntu)
- [Debian](#debian)
- [Fedora / RHEL / CentOS](#fedora--rhel--centos)
- [Void Linux](#void-linux)
- [BunsenLabs](#bunsenlabs)
- [Mac OS X](#mac-os-x)
- [Others](#others)


### Arch

1. Install **[neofetch](https://aur.archlinux.org/packages/neofetch/)** or **[neofetch-git](https://aur.archlinux.org/packages/neofetch-git/)** from the aur.


### Gentoo / Funtoo

1. Add the 3rd party repo
    - `# wget https://git.io/vocNV -O /etc/portage/repos.conf/konimex.conf`
2. Sync the repo
    - `# emerge --sync konimex`
3. To enable additional features such as w3m and music support, enable the appropriate USE flags. For example:
    - `# echo "app-misc/neofetch X -moc" >> /etc/portage/package.use`
4. Install the package
    - `# emerge -a app-misc/neofetch`

To install the git version, just add `app-misc/neofetch ~<your architecture>` to `package.accept_keywords`


### CRUX

1. Install git and the git ports(8) driver
    - `sudo prt-get depinst git`
2. Add the 3rd party repo
    - `sudo wget -O /etc/ports/tudurom.git https://git.io/vV46y`
3. Sync the repos
    - `sudo ports -u`
4. Add the repo to /etc/prt-get.conf with your text editor of choice
    - `prtdir /usr/ports/tudurom`
5. Install the package
    - `sudo prt-get depinst neofetch`

Or alternatively use the [port](https://github.com/tudurom/crux-ports/blob/master/neofetch/Pkgfile):

1. Download port
    - `wget -O ~/work/neofetch/Pkgfile https://raw.githubusercontent.com/tudurom/crux-ports/master/neofetch/Pkgfile`
2. Build the package
    - `fakeroot pkgmk -d`
3. Install the package
    - `sudo pkgadd neofetch#git-*.pkg.tar.gz`

### Ubuntu

1. Add PPA
    - `sudo add-apt-repository ppa:dawidd0811/neofetch`
2. Update repositories
    - `sudo apt update`
3. Install the package
    - `sudo apt install neofetch`

### Debian

1. Add the 3rd party repo
    - `echo "deb http://dl.bintray.com/dawidd6/neofetch jessie main" | sudo tee -a /etc/apt/sources.list`
2. Add public key (you need to have curl installed)
    - `curl -L "https://bintray.com/user/downloadSubjectPublicKey?username=bintray" -o Release-neofetch.key && sudo apt-key add Release-neofetch.key && rm Release-neofetch.key`
3. Update repositories
    - `sudo apt-get update`
4. Install the package
    - `sudo apt-get install neofetch`


### Fedora / RHEL / CentOS

**NOTE**: If you are using RHEL/CentOS, change `dnf` into `yum`.

1. Make sure you have installed `dnf-plugins-core`
2. Enable COPR repository
    - `sudo dnf copr enable konimex/neofetch`
3. Install the package
    - `sudo dnf install neofetch`

Alternatively:

1. Change your working directory to `/etc/yum.repos.d/`
2. Fetch the repo file
    - `wget https://copr.fedorainfracloud.org/coprs/konimex/neofetch/repo/epel-7/konimex-neofetch-epel-7.repo`
        * **NOTE**: If you are using Fedora, change `epel-7` to `fedora-23` or your Fedora version respectively. However if you are using RHEL/CentOS 6, change it to `epel-6`.
3. Install the package
    - `sudo dnf install neofetch`

### Void Linux
1. Install it from the official repositories
    - `sudo xbps-install -S neofetch`

### BunsenLabs
Neofetch is available in the official repos.

1. `sudo apt-get update`
2. `sudo apt-get install neofetch`

### Mac OS X

1. Install `neofetch` with Homebrew
    - `brew install neofetch`


### Others

1. Download the latest source at https://github.com/dylanaraps/neofetch
2. Run `make install` inside the script directory to install the script.
    - **El Capitan**: `PREFIX=/usr/local make install`

**NOTE:** Neofetch can be uninstalled easily using `make uninstall`.

**NOTE:** Neofetch can also be run from any directory like a normal script,<br \>
you'll just be missing the ascii distro logos and automatic config file creation.


<!-- }}} -->


<!-- Post Install {{{ -->


## Post Install


#### Using the config file

Neofetch will by default create a config file at `$HOME/.config/neofetch/config` and this file<br \>
contains all of the script's options/settings. The config file allows you to keep your<br \>
customizations between script versions and allows you to easily share your customizations<br \>
with other people.

You can launch the script without a config file by using the flag `--config none` and you can<br \>
specify a custom config location using `--config path/to/config`.


#### Setting the prompt height

If your shell prompt's height is greater than 1 line high, you'll need to change a config<br \>
option to avoid issues with the top lines in the script output getting cut off. Set the variable<br \>
`$prompt_height` to your shell prompt's height in lines or use the launch flag `--prompt_height`.


#### Customizing what info gets displayed

In the config file there's a function that allows you to customize all of the info that<br \>
gets displayed.

Here's what you can do:

- Add new info lines
- Change the ordering of the info
- Remove unwanted info lines
- Use bash syntax to control when info gets displayed

See this wiki page that goes more in-depth about it:

https://github.com/dylanaraps/fetch/wiki/Customizing-Info


#### Customizing the script using a custom alias

If you don't want to use the config file you can customize almost everything using launch flags!

Here's what my fetch alias looks like:

```sh
alias fetch2="fetch \
--block_range 1 8 \
--line_wrap off \
--bold off \
--uptime_shorthand on \
--gtk_shorthand on \
--colors 4 1 8 8 8 7 \
"
```

<!-- }}} -->


<!-- Usage {{{ -->


## Usage


    usage: neofetch --option "value" --option "value"

    NOTE: There's also a config option for each flag below.

    Info:
    --disable infoname          Allows you to disable an info line from appearing
                                in the output.
                                NOTE: You can supply multiple args. eg.
                                'neofetch --disable cpu gpu disk shell'
    --osx_buildversion on/off   Hide/Show Mac OS X build version.
    --osx_codename on/off       Hide/Show Mac OS X codename.
    --os_arch on/off            Hide/Show Windows architecture.
    --speed_type type           Change the type of cpu speed to display.
                                Possible values: current, min, max, bios,
                                scaling_current, scaling_min, scaling_max
                                NOTE: This only support Linux with cpufreq.
    --cpu_shorthand type        Shorten the output of CPU
                                Possible values: name, speed, tiny, on, off
    --cpu_cores on/off          Whether or not to display the number of CPU cores
    --kernel_shorthand on/off   Shorten the output of kernel
    --uptime_shorthand on/off   Shorten the output of uptime (tiny, on, off)
    --refresh_rate on/off       Whether to display the refresh rate of each monitor
                                Unsupported on Windows
    --gpu_shorthand on/off      Shorten the output of GPU (tiny, on, off)
    --gtk_shorthand on/off      Shorten output of gtk theme/icons
    --gtk2 on/off               Enable/Disable gtk2 theme/icons output
    --gtk3 on/off               Enable/Disable gtk3 theme/icons output
    --shell_path on/off         Enable/Disable showing \$SHELL path
    --shell_version on/off      Enable/Disable showing \$SHELL version
    --battery_num num           Which battery to display, default value is 'all'
    --battery_shorthand on/off  Whether or not each battery gets its own line/title
    --ip_host url               Url to ping for public IP
    --song_shorthand on/off     Print the Artist/Title on seperate lines
    --birthday_shorthand on/off Shorten the output of birthday
    --birthday_time on/off      Enable/Disable showing the time in birthday output
    --birthday_format format    Format the birthday output. (Uses 'date' cmd format)


    Text Formatting:
    --colors x x x x x x        Changes the text colors in this order:
                                title, @, underline, subtitle, colon, info
    --underline on/off          enable/disable the underline.
    --underline_char char       Character to use when underlining title
    --line_wrap on/off          Enable/Disable line wrapping
    --bold on/off               Enable/Disable bold text


    Color Blocks:
    --color_blocks on/off       Enable/Disable the color blocks
    --block_width num           Width of color blocks in spaces
    --block_height num          Height of color blocks in lines
    --block_range start end     Range of colors to print as blocks


    Progress Bars:
    --progress_char 'elapsed char' 'total char'
                                Characters to use when drawing progress bars.
    --progress_border on/off    Whether or not to surround the bar with '[]'
    --progress_length num       Length in spaces to make the progress bars.
    --progress_colors num num   Colors to make the progress bar.
                                Set in this order: elapsed, total
    --cpu_display mode          Progress bar mode.
                                Takes: bar, infobar, barinfo, off
    --memory_display mode       Progress bar mode.
                                Takes: bar, infobar, barinfo, off
    --battery_display mode      Progress bar mode.
                                Takes: bar, infobar, barinfo, off
    --disk_display mode         Progress bar mode.
                                Takes: bar, infobar, barinfo, off


    Image:
    --image type                Image source. Where and what image we display.
                                Possible values: wall, ascii,
                                /path/to/img, /path/to/dir/, off
    --size 00px | --size 00%    How to size the image.
                                Possible values: auto, 00px, 00%, none
    --crop_mode mode            Which crop mode to use
                                Takes the values: normal, fit, fill
    --crop_offset value         Change the crop offset for normal mode.
                                Possible values: northwest, north, northeast,
                                west, center, east, southwest, south, southeast

    --xoffset px                How close the image will be to the left edge of the
                                window. This only works with w3m.
    --yoffset px                How close the image will be to the top edge of the
                                window. This only works with w3m.
    --gap num                   Gap between image and text.
                                NOTE: --gap can take a negative value which will
                                move the text closer to the left side.
    --clean                     Remove all cropped images


    Ascii:
    --ascii value               Where to get the ascii from, Possible values:
                                distro, /path/to/ascii
    --ascii_colors x x x x x x  Colors to print the ascii art
    --ascii_distro distro       Which Distro's ascii art to print
    --ascii_logo_size           Size of ascii logo.
                                Supported distros: Arch, Gentoo, Crux, OpenBSD.
    --ascii_bold on/off         Whether or not to bold the ascii logo.


    Stdout:
    --stdout info info          Launch neofetch in stdout mode which prints the info
                                in a plain-text format that you can use with
                                lemonbar etc.
    --stdout_separator string   String to use as a separator in stdout mode.


    Screenshot:
    --scrot /path/to/img        Take a screenshot, if path is left empty the screen-
                                shot function will use \$scrot_dir and \$scrot_name.
    --scrot_cmd cmd             Screenshot program to launch


    Other:
    --config /path/to/config    Specify a path to a custom config file
    --config none               Launch the script without a config file
    --help                      Print this text and exit
    --version                   Show neofetch version
    --test                      Launch the script with all functions / options enabled.
                                This should only be used for testing purposes, ie Travis.CI.
    -v                          Display error messages.
    -vv                         Display a verbose log for error reporting.


<!-- }}} -->


<!-- Frequently Asked Questions {{{ -->


## Frequently Asked Questions


#### How do I enable screenfetch mode?

Launching the script with `--ascii` or setting `ascii="distro"` and `image="ascii"` <br \>
inside the config file will launch the script in "screenfetch mode". The script will<br \>
display your distro's ascii next to the info, exactly like screenfetch.

**NOTE:** If you **don't** have `w3m-img` or `imagemagick` installed screenfetch mode will be<br \>
used automatically

![arch](http://i.imgur.com/uCMjgf6.png)


#### Why doesn't Neofetch support my wallpaper setter?

It's hard to add support for other wallpaper setters as they don't provide a way of <br \>
getting the current wallpaper from the cli.

If your wallpaper setter **does** provide a way of getting the current wallpaper or you<br \>
know where it's stored then adding support won't be a problem!<br \>


<!-- }}} -->


<!-- Issues and Workarounds {{{ -->


## Issues and Workarounds


#### The text is too long for my terminal window and wraps to the next line

There are a few ways to fix this.

* Disable line wrapping with `line_wrap=off` in the script or with the launch flag `--line_wrap off`
* The uptime and gtk info lines each have a shorthand option that makes their output smaller. You can <br \>
  enable them by changing these variables or using these flags.

```sh
# Config options
uptime_shorthand="on"
gtk_shorthand="on"
gpu_shorthand="on"
birthday_shorthand="on"

# Launch flags
--uptime_shorthand on
--gtk_shorthand on
--gpu_shorthand on
--birthday_shorthand on

```

* Edit the config to make the subtitles shorter
* Resizing the terminal so that the lines don't wrap.


#### The text is pushed over too far to the right

The easiest way to fix this is to change the value of `--gap` or `$gap`<br \>
to a negative value. For example `--gap -10` will move the text 10 spaces to the left.


#### getgpu doesn't show my exact video card name

If your `lspci | grep "VGA"` output looks like this:

```
01:00.0 VGA compatible controller: NVIDIA Corporation Device 1401 (rev a1)
```

Instead of this:

```
01:00.0 VGA compatible controller: NVIDIA Corporation GM206 [GeForce GTX 960] (rev a1)
```

Then you're affected by the issue.

This is caused by your `/usr/share/misc/pci.ids\*` files being outdated and you can fix it<br \>
by running this command as root.

```
sudo update-pciids
```

#### Neofetch doesn't work correctly with ConEmu.

You need to be using the CYGWIN/Msys connector for Neofetch to work seamlessly with ConEmu.

https://conemu.github.io/en/CygwinMsysConnector.html


<!-- }}} -->


<!-- Thanks {{{ -->


## Thanks

Thanks to:

- [Screenfetch](https://github.com/KittyKatt/screenFetch):
    - I've used some snippets as a base for a few functions in this script.
    - Most of the ascii art.
- [ufetch](https://github.com/jschx/ufetch): Tiny ascii logos
- [@metakirby5](https://github.com/metakirby5): Providing great feedback as well as ideas for the script.
- [@jrgz](https://github.com/jrgz): Helping me test the Mac OS X version.
- [@mclado](https://github.com/mclado): Helping me with Max OS X testing
- [@xDemonessx](https://github.com/xDemonessx): Helping me test the Windows version.
- [@tudurom](https://github.com/tudurom): Helping me test **everything**.
- [@iandrewt](https://github.com/iandrewt): OS X related bug fixes and features.
- [@konimex](https://github.com/konimex): Packaging neofetch for a wide range of distros.
- [@dawidd6](https://github.com/dawidd6): Packaging neofetch for Debian / Ubuntu.
- Everyone else who has helped test the script, given feedback or reported bugs.


<!-- }}} -->

# fetch

This is the home of my fetch script! This script gathers info <br />
about your system and prints it to the terminal next to an image of your choice!

**NOTE: See this wiki page for info on the new info function and it's usage**

https://github.com/dylanaraps/fetch/wiki/Customizing-Info


![1](http://i.imgur.com/oTxq5fA.png)


<!-- Table of Contents {{{ -->


## Table of Contents

- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Post Install](#post-install)
- [Usage](#usage)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Issues and Workarounds](#issues-and-workarounds)
- [Todo](#todo)
- [Thanks](#thanks)


<!-- }}} -->


<!-- Features {{{ -->


## Features

- **Supports Linux, Mac OS X, BSD and Windows (Cygwin)!**
    - If the script doesn't work on your system, open an issue.
- **It's Fast**
    - The script makes heavy use of bash builtins and <br \>string manipulation.
- **Display an image next to the info. (or don't!)**
    - Use your current wallpaper, shuffle through a directory or just <br \>display an image of your choice.
    - Supports using w3m or iTerm2 to display the images.
- **Highly Customizable**
    - You can customize almost everything.
        - See Usage below or lines 23-233 in script
- **Take a screenshot at the end.**
    - It's disabled by default and you can specify the cmd <br \>to use with `--scrotcmd cmd` at launch or by <br \>changing the value of `$scrotcmd` in the script.
- **Smart crop (or Waifu crop)**
    - See https://github.com/dylanaraps/fetch/wiki/What-is-Smart-Crop%3F


<!-- }}} -->


<!-- Dependences {{{ -->


## Dependencies


### Required dependencies:

**All OS:**

-  `Bash 4.0+`
-  Text formatting, dynamic image size and padding: `tput`

**Linux / BSD / Windows:**

-  Uptime detection: `procps` or `procps-ng`

### Optional dependencies:

**All OS:**

-  Displaying Images: `w3m`
    - You may also need `w3m-img`
    - **Note:** The script can now also use iTerm2's builtin image rendering instead of w3m!
        - Enable it by changing `image_backend` to `iterm2` or by using the launch flag `--image_backend`.
-  Image Cropping, Resizing etc: `ImageMagick`
-  Window manager detection: `wmctrl`
    - This is used as a fallback to parsing `.xinitrc` and `$XDG_CURRENT_DESKTOP`.

**Linux / BSD:**

-  Display Wallpaper: `feh` or `nitrogen`
-  Current Song: `mpc` or `cmus`
-  Resolution Detection: `xorg-xdpyinfo`
-  Take a screenshot on script finish: `scrot`
    - You can change this to another program with a `--scrotcmd` and an in script option.


<!-- }}} -->


<!-- Installation {{{ -->


## Installation


### Arch

1. Install **[fetch-git](https://aur.archlinux.org/packages/fetch-git/)** from the aur.


### Others

1. Download the latest source at https://github.com/dylanaraps/fetch
2. Make the file executable using chmod. `chmod +x /path/to/fetch`
3. Move the script to somewhere in your $PATH or just run it from where it is.


<!-- }}} -->


<!-- Post Install {{{ -->

## Post Install


#### Sizing the image correctly

**NOTE:** For the images to be sized correctly you need to set the `$font_width` variable.
If you don't know your font width in pixels keep trying values until the image is sized correctly.

You can also use the launch flag `--font_width` to set it on the fly.


#### Customizing what info gets displayed

At the top of the script there's a function that allows you to customize all of the info that gets displayed.

Here's what you can do:

- Add new info lines
- Change the ordering of the info
- Remove unwanted info lines
- Use bash syntax to control when info gets displayed

See this wiki page that goes more in-depth about it:

https://github.com/dylanaraps/fetch/wiki/Customizing-Info


#### Customizing the script using a custom alias

If you don't want to edit the script you can customize almost everything using launch flags!

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


    usage: ${0##*/} [--colors 1 2 3 4 5] [--kernel "\$\(uname -rs\)"]

    Info:
    --speed_type           Change the type of cpu speed to display.
                           Possible values: current, min, max, bios,
                           scaling_current, scaling_min, scaling_max
                           NOTE: This only support Linux with cpufreq.
    --uptime_shorthand     Shorten the output of uptime
    --gpu_shorthand on/off Shorten the output of GPU
    --gtk_shorthand on/off Shorten output of gtk theme/icons
    --gtk2 on/off          Enable/Disable gtk2 theme/icons output
    --gtk3 on/off          Enable/Disable gtk3 theme/icons output

    Text Colors:
    --colors 1 2 3 4 5     Change the color of text
                           (title, subtitle, colon, underline, info)
    --title_color num      Change the color of the title
    --subtitle_color num   Change the color of the subtitle
    --colon_color num      Change the color of the colons
    --underline_color num  Change the color of the underlines
    --info_color num       Change the color of the info

    Text Formatting:
    --underline on/off     Enable/Disable title underline
    --underline_char char  Character to use when underlineing title
    --line_wrap on/off     Enable/Disable line wrapping
    --bold on/off          Enable/Disable bold text
    --prompt_height num    Set this to your prompt height to fix
                           issues with the text going off screen at the top

    Color Blocks:
    --color_blocks on/off  Enable/Disable the color blocks
    --block_width num      Width of color blocks
    --block_range start end --v
                           Range of colors to print as blocks

    Image:
    --image                Image source. Where and what image we display.
                           Possible values: wall, shuffle, /path/to/img, off
    --shuffledir           Which directory to shuffle for an image.
    --font_width px        Used to automatically size the image
    --image_position       Where to display the image: (Left/Right)
    --split_size num       Width of img/text splits
                           A value of 2 makes each split half the terminal
                           width and etc
    --crop_mode            Which crop mode to use
                           Takes the values: normal, fit, fill
    --crop_offset value    Change the crop offset for normal mode.
                           Possible values: northwest, north, northeast,
                           west, center, east, southwest, south, southeast

    --xoffset px           How close the image will be
                           to the left edge of the window
    --yoffset px           How close the image will be
                           to the top edge of the window
    --gap num              Gap between image and text right side
                           to the top edge of the window
                           NOTE: --gap can take a negative value which will
                           move the text closer to the left side.
    --clean                Remove all cropped images

    Screenshot:
    --scrot /path/to/img   Take a screenshot, if path is left empty
                           the screenshot function will use
                           \$scrot_dir and \$scrot_name.
    --scrot_cmd            Screenshot program to launch

    Other:
    --help                 Print this text and exit


<!-- }}} -->


<!-- Frequently Asked Questions {{{ -->


## Frequently Asked Questions


#### Why doesn't fetch support my wallpaper setter?

It's hard to add support for other wallpaper setters as<br \>
they don't provide a way of getting the current wallpaper from the cli.

If your wallpaper setter **does** provide a way of getting the current wallpaper<br \>
or you know where it's stored then adding support won't be a problem!<br \>


<!-- }}} -->


<!-- Issues and Workarounds {{{ -->


## Issues and Workarounds


#### The image is rendering with black lines in Urxvt while using an xft font.

This is an issue with w3mimgdisplay and not the script. You can find a workaround here:

https://github.com/hut/ranger/issues/86#issuecomment-17346249


#### The text is too long for my terminal window and wraps to the next line causing the image to not render correctly.

There are a few ways to fix this.

* Disable line wrapping with `$line_wrap off` in the script or with the launch flag `--line_wrap off`

* The uptime and gtk info lines each have a shorthand option that makes their output smaller. You can <br \>
  enable them by changing these variables or using these flags.

```sh
# In script options
uptime_shorthand="on"
gtk_shorthand="on"
gpu_shorthand="on"

# Launch flags
--uptime_shorthand on
--gtk_shorthand on
--gpu_shorthand on
```

* Edit the info array to make the subtitles shorter

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

<!-- }}} -->


<!-- Todo {{{ -->


## Todo

Here's what's on my todo list

- More info outputs. Now that it's easy to customize what's printed and<br \>
  everything is a function we can add optional support for pretty much anything.

    - Resolution (Just missing Windows support)
    - ~~GTK themes~~
    - Terminal Font
        - This will be difficult to add as there's no standard way of getting this info. We can't check<br \>
        for terminal config files because the user may have multiple terminals installed.<br \>
        Using `$PPID` isn't an option because it won't work in tmux/screen, subshells or neovim terminal splits.
    - GPU (In master but experimental) See **[issue #21](https://github.com/dylanaraps/fetch/issues/21)**.


<!-- }}} -->


<!-- Thanks {{{ -->


## Thanks

Thanks to:

- metakirby5: Providing great feedback as well as ideas for the script.

- Screenfetch: I've used some snippets as a base for a few functions in this script.

- @jrgz: Helping me test the Mac OS X version.

- @xDemonessx: Helping me test the Windows version.


<!-- }}} -->

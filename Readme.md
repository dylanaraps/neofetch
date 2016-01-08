# fetch

## Big updates: Check the releases page.

This is the home of my fetch script! This script gathers info <br\>
about your system and prints it to the terminal.

The script currently supports Linux, Mac OS X and Windows (Cygwin), if your OS or distro isn't
supported open an issue and I'll add support for it.

![1](https://sr.ht/Jd8Y.png)


<!-- Dependences {{{ -->


## Dependencies


These are the script's required dependencies

-  Text formatting, dynamic image size and padding: tput
-  Uptime detection: procps or procps-ng

These are the script's optional dependencies:

-  Displaying Images: w3m
    - You may also need w3m-img
-  Image Cropping: ImageMagick
-  Display Wallpaper: feh
-  Current Song: mpc
-  Resolution Detection: xorg-xdpyinfo
-  Window manager detection: wmctrl
    - This is used as a fallback to parsing ```.xinitrc``` and ```$XDG_CURRENT_DESKTOP```.
-  Take a screenshot on script finish: scrot
    - You can change this to another program with a ```--scrotcmd``` and an in script option.


<!-- }}} -->


<!-- Usage {{{ -->


## Usage

The script now supports dynamic image sizing and padding,
<br\> it's enabled by default and there's a variable you
<br\> need to set for it to work correctly.

You can either change the variable $fontwidth inside of the
<br\> script or launch it with ```--font_width num```.

Once you set the var the script will scale the image and padding
<br\> to fit your terminal window.

Please report any bugs or issues you're having with this as I can't
<br\> test with many configurations.


```
 usage: ${0##*/} [--colors 1 2 3 4 5] [--kernel "\$\(uname -rs\)"]

    Info:
    --title string         Change the title at the top
    --distro string/cmd    Manually set the distro
    --kernel string/cmd    Manually set the kernel
    --uptime string/cmd    Manually set the uptime
    --uptime_shorthand on/off --v
                           Shorten the output of uptime
    --packages string/cmd  Manually set the package count
    --shell string/cmd     Manually set the shell
    --winman string/cmd    Manually set the window manager
    --use_wmctrl on/off    Use wmctrl for a more accurate reading
    --cpu string/cmd       Manually set the cpu name
    --memory string/cmd    Manually set the memory
    --speed_type           Change the type of cpu speed to get
                           Possible values: current, min, max
    --song string/cmd      Manually set the current song

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
    --clean                Remove all cropped images

    Screenshot:
    --scrot                Take a screenshot
    --scrotdir             Directory to save the scrot
    --scrotfile            File name of scrot

    Other:
    --help                 Print this text and exit
```


<!-- }}} -->


<!-- TODO {{{ -->


## TODO

Here's what's on my todo list

- Cleanup of info array handling

- Windows support (I'm almost done)

- Imagemagick optimizations

- More info outputs. Now that it's easy to customize what's printed and
  everything is a function we can add optional support for pretty much anything.

    - Resolution (Done!)
    - GTK themes
    - Terminal Font
    - GPU
    - IP
    - etc

<!-- }}} -->


### Crop mode comparison

#### Fit
![fit](https://imgur.com/MI0UtSV.png)

#### Fill
![fill](https://imgur.com/LvxYwki.png)


### Thanks

Thanks to:

- metakirby5: Providing great feedback as well as ideas for the script.

- Screenfetch: I've used some snippets as a base for a few functions in this script.

- @jrgz: Helping me test the Mac OS X version.

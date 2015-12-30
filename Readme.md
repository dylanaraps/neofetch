# fetch.sh

https://github.com/dylanaraps/fetch.sh


This is the home of my fetch script! This script gathers info <br\>
about your system and prints it to the terminal.

I've spent the past few days rewriting this and it now supports <br\>
other distros as well as a ton of new features and bug fixes.

If you're having any issues or have any ideas, please open an issue! <br\>
I can't test on many other distros and I want this to work <br\>
for as many people as possible.

![1](https://sr.ht/5aNV.png)


## Dependencies

These are the script's dependencies:

-  Displaying Images: w3m
-  Image Cropping: ImageMagick
-  Display Wallpaper: feh
-  Current Song: mpc

These are the script's optional dependencies
-  Window Manager Detection: wmctrl
    - You can manually set this at launch with:

        ```sh
        scrot.sh --winman string
        ```

## Usage

The whitespace


```
usage: scrot.sh [--colors 1 2 4 5] [--kernel "$(uname -rs)"]

Info:
--title string         Change the title at the top
--distro string/cmd    Manually set the distro
--kernel string/cmd    Manually set the kernel
--uptime string/cmd    Manually set the uptime
--packages string/cmd  Manually set the package count
--shell string/cmd     Manually set the shell
--winman string/cmd    Manually set the window manager
--cpu string/cmd       Manually set the cpu name
--memory string/cmd    Manually set the memory
--speed string/cmd     Manually set the cpu speed
--speed_type           Type of cpu speed to get Possible values:
                       current, min, max
--song string/cmd      Manually set the current song

Text Colors:
--colors 1 2 3 4       Change the color of text
                       (title, subtitle, colon, info)
--titlecol num         Change the color of the title
--subtitlecol num      Change the color of the subtitle
--coloncol num         Change the color of the colons
--infocol num          Change the color of the info

Color Blocks:
--printcols start end  Range of colors to print as blocks
--nopal                Disable the color blocks

Image:
--image                Image to display with the script
                       The image gets priority over other
                       images: (wallpaper, \$img)
--size px              Change the size of the image
--cropoffset value     Change the crop offset. Possible values:
                       northwest, north, northeast, west, center
                       east, southwest, south, southeast
--padding              How many spaces to pad the text
                       to the right
--xoffset px           How close the image will be
                       to the left edge of the window
--yoffset px           How close the image will be
                       to the top edge of the window
--noimg                Disable all images
--nowall               Disable the wallpaper function
                       and fallback to \$img
--clean                Remove all cropped images

Other:
--help                 Print this text and exit
```


## TODO

Here's what's on my todo list

- Add an easy way to define info prefixes at launch.
- Find a reliable way to set the text padding dynamically. I can get this to
  <br/> work based on font width but there's no reliable way of getting
  <br/> fontwidth for every terminal afaik.

If you've got any ideas on how to solve these problems, let me know!


## Customization

I launch fetch using a shell function and a ton of flags. Here's how it looks:

```sh
fetch () {
    fetch.sh \
        --printcols 1 7 \
        --cpu "AMD FX-6300" \
        --song "$(mpc current | cut -c 1-30)" \
        --uptime "$(uptime -p | sed -e 's/minutes/mins/')" \
        --title "dylan's pc" \
        $@
}
```

Notice how you can even pass commands? This allows you to easily use custom
<br/> commands or even just bare strings to change the info.


## Screenshots

#### The color script is now builtin.
![2](https://sr.ht/Z9hZ.png)

#### You can now customize the color of everything.
![3](https://sr.ht/hy7m.png)

#### You can now disable all images with a flag.
![4](https://sr.ht/zujR.png)

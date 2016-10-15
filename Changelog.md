## Contributors

- **[@konimex](https://github.com/konimex)**

<br \>

**General**<br \>

-
-
-


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


## Ascii

- Fixed incorrect prompt location when using `ascii_logo_size small`.
- Bold ascii art by default.


## Info

**Theme Font**<br \>

- [XFCE] Fixed incorrect font output.


**Color Blocks**<br \>

- Show 16 colors by default instead of 8.

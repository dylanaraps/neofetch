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

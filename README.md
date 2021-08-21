A fork of neofetch that adds an "Updates" tab to the output.

Requirements:
- Pacman (Arch Linux)
- pacman-contribs

Installation:
Latest Git Master (Bleeding Edge)
Git clone the repo.
git clone https://github.com/dylanaraps/neofetch
Change working directory to neofetch.
cd neofetch
Install neofetch using the Makefile.
make install
MacOS: make PREFIX=/usr/local install
Haiku: make PREFIX=/boot/home/config/non-packaged install
OpenIndiana: gmake install
MinGW/MSys: make -i install
NOTE: You may have to run this as root.
NOTE: Neofetch can be uninstalled easily using make uninstall. This removes all of files from your system.

NOTE: You can run neofetch from any folder on your system, all the makefile does is move the files to a "sane" location. The Makefile is optional.

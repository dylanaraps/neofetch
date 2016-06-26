PREFIX        ?=  /usr
RM            ?=  rm -f
INSTALL_DIR   ?=  install -m755 -d
INSTALL_PROG  ?=  install -m755
INSTALL_FILE  ?=  install -m644

all:
	@echo Run \'make install\' to install Neofetch

install:
	# Neofetch
	$(INSTALL_DIR) $(DESTDIR)$(PREFIX)/bin
	$(INSTALL_PROG) neofetch $(DESTDIR)$(PREFIX)/bin/neofetch
	#
	# Config
	$(INSTALL_PROG) config/config $(DESTDIR)$(PREFIX)/share/neofetch/config
	#
	# Man page
	$(INSTALL_DIR) $(DESTDIR)$(PREFIX)/share/man/man1
	$(INSTALL_FILE) neofetch.1 $(DESTDIR)$(PREFIX)/share/man/man1/neofetch.1
	#
	# Ascii art
	$(INSTALL_DIR) $(DESTDIR)$(PREFIX)/share/neofetch/ascii/distro
	$(install_prog) ascii/distro/* $(destdir)$(prefix)/share/neofetch/ascii/distro
	#
	# Info functions
	$(INSTALL_DIR) $(DESTDIR)$(PREFIX)/share/neofetch/ascii/functions/info
	$(install_prog) functions/info/* $(destdir)$(prefix)/share/neofetch/functions/info

uninstall:
	$(RM) $(DESTDIR)$(PREFIX)/bin/neofetch
	$(RM) $(DESTDIR)$(PREFIX)/share/man/man1/neofetch.1
	$(RM) -r $(DESTDIR)$(PREFIX)/share/neofetch



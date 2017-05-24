PREFIX = /usr

all:
	@echo Run \'make install\' to install Neofetch

install:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(DESTDIR)$(PREFIX)/share/man/man1
	mkdir -p $(DESTDIR)/etc/neofetch
	mkdir -p $(DESTDIR)$(PREFIX)/share/neofetch/ascii/distro
	cp -p neofetch $(DESTDIR)$(PREFIX)/bin/neofetch
	cp -p neofetch.1 $(DESTDIR)$(PREFIX)/share/man/man1/neofetch.1
	cp -p config/config $(DESTDIR)/etc/neofetch/config
	cp -p ascii/distro/* $(DESTDIR)$(PREFIX)/share/neofetch/ascii/distro
	# Set the PREFIX/DESTDIR inside Neofetch.
	sed -i'' -e "s|NEOFETCH_PREFIX=\"\/usr\"|NEOFETCH_PREFIX=\"$(PREFIX)\"|" $(DESTDIR)$(PREFIX)/bin/neofetch
	sed -i'' -e "s|NEOFETCH_DESTDIR=\"\"|NEOFETCH_DESTDIR=\"$(DESTDIR)\"|" $(DESTDIR)$(PREFIX)/bin/neofetch

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/neofetch
	rm -f $(DESTDIR)$(PREFIX)/share/man/man1/neofetch.1
	rm -f -r $(DESTDIR)$(PREFIX)/share/neofetch
	rm -f -r $(DESTDIR)/etc/neofetch

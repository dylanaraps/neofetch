UNAME != uname -s
PREFIX=/usr
SHARE=/share
.if "${UNAME}" == "OpenBSD"
PREFIX = /usr/local
SHARE =  
.endif

all:
	@echo Run \'make install\' to install Neofetch

install:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(DESTDIR)$(PREFIX)/man/man1
	mkdir -p $(DESTDIR)/etc/neofetch
	mkdir -p $(DESTDIR)$(PREFIX)$(SHARE)/neofetch/ascii/distro
	cp -p neofetch $(DESTDIR)$(PREFIX)/bin/neofetch
	cp -p neofetch.1 $(DESTDIR)$(PREFIX)/man/man1/neofetch.1
	cp -p config/config $(DESTDIR)/etc/neofetch/config
	cp -p ascii/distro/* $(DESTDIR)$(PREFIX)$(SHARE)/neofetch/ascii/distro

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/neofetch
	rm -f $(DESTDIR)$(PREFIX)/man/man1/neofetch.1
	rm -f -r $(DESTDIR)$(PREFIX)$(SHARE)/neofetch
	rm -f -r $(DESTDIR)/etc/neofetch

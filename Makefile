NF_PREFIX ?= /usr
NF_MANDIR ?= $(NF_PREFIX)/share/man

all:
	@echo Run \'make install\' to install Neofetch.

install:
	@mkdir -p $(NF_DESTDIR)$(NF_PREFIX)/bin
	@mkdir -p $(NF_DESTDIR)$(NF_MANDIR)/man1
	@cp -p neofetch $(NF_DESTDIR)$(NF_PREFIX)/bin/neofetch
	@cp -p neofetch.1 $(NF_DESTDIR)$(NF_MANDIR)/man1
	@chmod 755 $(NF_DESTDIR)$(NF_PREFIX)/bin/neofetch

uninstall:
	@rm -rf $(NF_DESTDIR)$(NF_PREFIX)/bin/neofetch
	@rm -rf $(NF_DESTDIR)$(NF_MANDIR)/man1/neofetch.1*

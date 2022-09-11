PREFIX = /usr
MANDIR = $(PREFIX)/share/man

all:
	@echo Run \'make install\' to install Neofetch.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(MANDIR)/man1
	@cp -p neofetch $(DESTDIR)$(PREFIX)/bin/unifetch
	@cp -p neofetch.1 $(DESTDIR)$(MANDIR)/man1/unifetch.1
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/unifetch

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/unifetch
	@rm -rf $(DESTDIR)$(MANDIR)/man1/unifetch.1*

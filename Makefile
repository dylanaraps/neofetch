PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man

all:
	@echo Run \'make install\' to install Neofetch.

install:
	@echo 'Making directories...'
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(MANDIR)/man1

	@echo 'Installing binaries...'
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/neofetch

	@echo 'Installing man page...'
	@cp -p neofetch.1 $(DESTDIR)$(MANDIR)/man1

uninstall:
	@echo 'Removing files...'
	@rm -rf $(DESTDIR)$(PREFIX)/bin/neofetch
	@rm -rf $(DESTDIR)$(MANDIR)/man1/neofetch.1*

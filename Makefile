PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man
COMDIR ?= $(PREFIX)/share/bash-completion/completions

all:
	@echo Run \'make install\' to install Neofetch.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(MANDIR)/man1
	@mkdir -p $(DESTDIR)$(COMDIR)
	@cp -p neofetch $(DESTDIR)$(PREFIX)/bin/neofetch
	@cp -p neofetch.1 $(DESTDIR)$(MANDIR)/man1
	@cp -p completions/neofetch-completion.bash $(DESTDIR)$(COMDIR)/neofetch
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/neofetch

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/neofetch
	@rm -rf $(DESTDIR)$(MANDIR)/man1/neofetch.1*
	@rm -rf $(DESTDIR)$(COMDIR)/neofetch

# Nix Manual

First add `doc\manual\version.txt` file with version number in it.

Then:

```bash
sudo apt install docbook5-xml docbook-xsl-ns xsltproc fop xmlto libxml2-utils xmlstarlet
xsltproc --xinclude /usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook.xsl book.xml > book.fo
fop -fo book.fo -pdf book.pdf
```

## XML manual modification

Due to multiple ID error of `xsltproc` I removed conflicting ID's by `[ ]*(xml:id|linkend)=("|')<CONFLICTING ID HERE>("|')`

## Manual FO modification

Due to columns error I removed column definitions by `<fo:table-column[^>]*/>`

It's preferable to remove `wrap-option="no-wrap"` from `fo:block`'s in `book.fo`.

# NixOS Manual

Based on [original README](https://github.com/NixOS/nixpkgs/blob/master/nixos/doc/manual/README)

## Use Nix

To build the manual, you need Nix installed on your system (no need for NixOS). To install Nix, follow the instructions at [Nix](https://nixos.org/nix/download.html).

In Void Linux, Nix can be installed via standard `xbps-install`:

```bash
sudo xbps-install -S nix
sudo ln -s /etc/sv/nix-daemon /var/service/
```

On WSL we should [use](https://github.com/NixOS/nix/issues/2292) (thanks to @rdbuf):

```bash
sudo mkdir /etc/nix; echo 'use-sqlite-wal = false' | sudo tee -a /etc/nix/nix.conf && sh <(curl https://nixos.org/nix/install)
```

On WSL 32-bit libraries are unsupported, so there is a [workaround](https://github.com/NixOS/nixpkgs/issues/24954) originating from [Stackoverflow](https://stackoverflow.com/questions/42120938/exec-format-error-32-bit-executable-windows-subsystem-for-linux/49405605#49405605) (thanks to @eqyiel):

```bash
sudo apt install qemu-user-static
sudo update-binfmts --install i386 /usr/bin/qemu-i386-static --magic '\x7fELF\x01\x01\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x01\x00\x00\x00' --mask '\xff\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xff\xff\xf8\xff\xff\xff\xff\xff\xff\xff'
sudo service binfmt-support start #Every time WSL is started
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install gcc:i386
```

Add `"i686-linux"` to `nixos/release.nix`:

```nix
  supportedSystems ? [ "x86_64-linux" "i686-linux" "aarch64-linux" ]
```

When you have Nix on your system, in the root directory of the project (i.e., `nixpkgs`), run:

```bash
nix-build nixos/release.nix -A manual.x86_64-linux
```

or:

```bash
nix-build nixos/release.nix -A manual.i686-linux
```

When this command successfully finishes, it will tell you where the manual got generated. We should find new `nixos-manual-combined` package in `/nix/store` and convert the corresponding `manual-combined.xml` to PDF.

Or we can do it other way:

```bash
cd nixos/doc/manual
sed -i.bak 's/x86_64/i686/' Makefile
make generated
```

After that we can convert manual to PDF.

## XML to PDF

```bash
sudo apt install docbook5-xml docbook-xsl-ns xsltproc fop xmlto libxml2-utils xmlstarlet
xsltproc --xinclude /usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook.xsl book.xml > book.fo
fop -fo book.fo -pdf book.pdf
```

It's preferable to remove `wrap-option="no-wrap"` from `fo:block`'s in `book.fo`.

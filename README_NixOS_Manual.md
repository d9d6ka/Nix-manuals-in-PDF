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

Then we should do some manual acions:

```bash
cd nixos/doc/manual
sed -i.bak 's/x86_64/i686/' Makefile
make generated
cp -rL generated/ gen/
sudo cp /nix/store/*.xml gen/
sudo chown <user>:<group> gen/*
sudo sed -i 's|/nix/store/||g' gen/modules.xml
rm generated
mv gen generated
```

After that we can convert manual to PDF.

## XML to PDF

```bash
sudo apt install docbook5-xml docbook-xsl-ns xsltproc fop xmlto libxml2-utils xmlstarlet
xsltproc --xinclude /usr/share/xml/docbook/stylesheet/docbook-xsl-ns/fo/docbook.xsl book.xml > book.fo
fop -fo book.fo -pdf book.pdf
```

It's preferable to remove `wrap-option="no-wrap"` from `fo:block`'s in `book.fo`.

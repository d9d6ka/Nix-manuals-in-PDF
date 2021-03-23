# Nix-manuals-in-PDF

[Nix](https://github.com/NixOS/nix) and [NixOS](https://github.com/NixOS/nixpkgs) manuals in PDF.

Manuals converted for convenient offline reading.

1. Generate Nix and NixOS manuals in HTML.
2. Filter HTMLs using `replace.py`.
3. (Optional) Convert SVG to PNG.
   
   ```bat
   for %f in (*.svg) do (C:\Users\vadim\scoop\apps\ImageMagick\current\convert.exe %~nf.svg -resize 10x10 %~nf.png)
   ```
4. Use `pandoc` to convert HTML to PDF.
   ```bat
   pandoc --pdf-engine=xelatex --listings -H ..\listings-setup.tex -V geometry:margin=2cm -o ..\nix-2.3.10.pdf .\manual.html
   pandoc --pdf-engine=xelatex --listings -H ..\listings-setup.tex -V geometry:margin=2cm -o ..\nixos-20.09.pdf .\index.html
   pandoc --pdf-engine=xelatex --listings -H ..\listings-setup.tex -V geometry:margin=2cm -o ..\nixos-20.09-options.pdf .\options.html
   ```
Copyright and/or Copyleft by @NixOS and Eelco Dolstra (@edolstra).

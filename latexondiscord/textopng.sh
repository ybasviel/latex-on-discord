#!/bin/sh
cd ./latexondiscord && yes x | lualatex ./latex-on-discord.tex >/dev/null 2>&1 && pdfcrop --margins "5 5 5 5" ./latex-on-discord.pdf ./croped.pdf >/dev/null 2>&1 && mutool draw -r 600 -o ./image.png ./croped.pdf >/dev/null 2>&1

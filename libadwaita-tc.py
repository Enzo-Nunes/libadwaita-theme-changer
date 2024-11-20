#!/bin/python3

############################################
#
# Libadwaita Theme Changer
# created by OdzioM
#
############################################

import os
import subprocess as sp
import sys

home_dir = os.getenv("HOME")
config_dir = f"{home_dir}/.config"
themes_dir = f"{home_dir}/.themes"
if "--reset" in sys.argv:
    print("\n***\nResetting theme to default!\n***\n")
    sp.run(["rm", f"{config_dir}/gtk-4.0/gtk.css"])
    sp.run(["rm", f"{config_dir}/gtk-4.0/gtk-dark.css"])
    sp.run(["rm", f"{config_dir}/gtk-4.0/assets"])
    sp.run(["rm", f"{config_dir}/assets"])
    exit()

all_themes = str(sp.run(["ls", f"{themes_dir}/"], stdout=sp.PIPE).stdout.decode("UTF-8")).split()
print("Select theme: ")
for i, theme in enumerate(all_themes):
    print(f"{i + 1} - {theme}")
print("e - Exit")

chk = input("Your choice: ")
if chk == "e":
    print("Bye bye!")
    exit()

chk_theme = all_themes[int(chk) - 1]
print(f"\n***\nChoosed {chk_theme}\n***\n")
print("Removing previous theme...")
sp.run(["rm", f"{config_dir}/gtk-4.0/gtk.css"])
sp.run(["rm", f"{config_dir}/gtk-4.0/gtk-dark.css"])
sp.run(["rm", "-r", f"{config_dir}/gtk-4.0/assets"])
sp.run(["rm", "-r", f"{config_dir}/assets"])
print("Installing new theme...")
sp.run(["ln", "-s", f"{themes_dir}/{chk_theme}/gtk-4.0/gtk.css", f"{config_dir}/gtk-4.0/gtk.css"])
sp.run(["ln", "-s", f"{themes_dir}/{chk_theme}/gtk-4.0/gtk-dark.css", f"{config_dir}/gtk-4.0/gtk-dark.css"])
sp.run(["ln", "-s", f"{themes_dir}/{chk_theme}/gtk-4.0/assets", f"{config_dir}/gtk-4.0/assets"])
sp.run(["ln", "-s", f"{themes_dir}/{chk_theme}/assets", f"{config_dir}/assets"])
print("Done.")

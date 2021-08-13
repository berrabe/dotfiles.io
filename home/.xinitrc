# For gnome-keyring (systemPrompter), look at https://bbs.archlinux.org/viewtopic.php?id=202754
dbus-update-activation-environment --systemd DISPLAY

# Run WM
exec i3
# exec bspwm

#!/bin/bash

clear

echo -e "\n[+] Add Repo\n"
sudo add-apt-repository ppa:kgilmer/speed-ricer --yes --no-update; echo "kgilmer/speed-ricer"
sudo add-apt-repository ppa:papirus/papirus --yes --no-update; echo "papirus/papirus"
sudo add-apt-repository ppa:dyatlov-igor/sierra-theme --yes --no-update; echo "dyatlov-igor/sierra-theme"
sudo add-apt-repository ppa:dyatlov-igor/la-capitaine --yes --no-update; echo "dyatlov-igor/la-capitaine"


echo -e "\n[+] Update Repo\n"
sudo apt update


echo -e "\n[+] Install Package\n"
sudo apt install -y\
		i3-gaps-wm\
		compton\
		tint2\
		dunst\
		rofi\
		papirus-icon-theme\
		sierra-gtk-theme\
		la-capitaine-cursor-theme\
		zsh\
		cmus\
		viewnior\
		lxappearance\
		neofetch\
		tty-clock\
		ranger\
		i3lock\
		kazam\
		scrot\
		feh\
		pasystray\
		arandr\
		bwm-ng\
		xautolock\
		pm-utils\

echo -e "\n[+] Done\n"

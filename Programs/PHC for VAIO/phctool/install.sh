#/bin/sh
ROOT_UID=0
PROGPATH=`dirname "$0"`
cd "$PROGPATH"
PROGDIR=`pwd`
GROUPNAME="phcusers"


if [ "$UID" -ne "$ROOT_UID" ]; then
    echo "You don't have sufficient privileges to run this script.";
    echo "Run this as root using a root-shell or sudo.";
    exit 65;
fi


echo "Welcome to the PHCtool installer."
echo "This script helps you to set up PHCtool on your system."
echo "It will create a new group named \"$GROUPNAME\" to your system"
echo "and add this group to /etc/sudoers with permission to PHCtool only."
echo "Every user that is member of this group and root can use PHCtool."
echo ""

echo "----------------------------------";
echo "|       Installing PHCtool       |";
echo "----------------------------------";
echo ""
echo ""

echo "Creating groups:"
echo "----------------"
echo "If you say \"no\" here you need to get root permissions to run PHCtool by your own."
echo "Adding group \"$GROUPNAME\" to your system [y/n]?"
	read ADDGROUP
	if [ $ADDGROUP = "y" ]; then
		groupadd $GROUPNAME

		echo ""
		echo ""
		echo "Set up sudoers:"
		echo "---------------"
		echo "If you say \"no\" here you need to add this group manually to sudoers or"
		echo "get root permissions to run PHCtool by your own."
		echo "Do you wish that \"$GROUPNAME\" will be added to /etc/sudoers [y/n]?"
		read ADDSUDO
		if [ $ADDSUDO = "y" ]; then

			SUDOERS=`cat /etc/sudoers | grep $GROUPNAME`
			if [ "$SUDOERS" = "" ]; then
				echo "%$GROUPNAME ALL=(root) NOPASSWD:$PROGDIR/subphctool.sh" >> /etc/sudoers
			else
				echo "Group seems already added to /etc/sudoers - leaving file as it is."
				echo " "
			fi

		else
			echo ""
			echo "Group not added to sudoers. Make sure by your own that you can run PHCtool as root."
		fi

	else
		echo "Group not automatically added."
		echo "Make sure by your own that you can run PHCtool as root."
	fi


echo "Setting file permissions:"
echo "-------------------------"
echo "chmod 755 phctool"
	chmod 755 ./phctool.sh
	chmod 755 ./phctool.py

echo "chmod 755 phctray"
	chmod 755 ./phctray.sh
	chmod 755 ./phctray.py

echo ""
echo "Thats all."
echo ""
echo "Remember that you need to relogin to have the added group take effect."
echo ""
echo "Run phctool.sh to start PHCtool and phctray.sh to start the tray icon."
echo "Read the manual if you don't know how to autostart phctray."



#!/bin/bash
#
##################################################################################################################
# Written to be used on 64 bits computers
# Author 	: 	Erik Dubois
# Website 	: 	http://www.erikdubois.be
##################################################################################################################
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################

# echo "# Ultimate-Linux-Mint-18" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/erikdubois/Ultimate-Linux-Mint-18-Cinnamon.git
# git push -u origin master

# git config --global user.name x
# git config --global user.email x
# sudo git config --system core.editor nano
# git config --global credential.helper cache
# git config --global credential.helper 'cache --timeout=3600'


# Force git to overwrite local files on pull - no merge

# git fetch all

# git push --set-upstream origin master

# git reset --hard orgin/master


# checking if kernel files are present otherswise github will become too big

if [ -f linux* ]; then
	echo "####################################"
    	echo "Stopping the script!!"
    	echo "Wait for the kernel update script to quit."
    	echo "####################################"
    	exit 0
fi


# checking if I have the latest files from github
echo "Checking for newer files online first"
git pull

# Below command will backup everything inside the project folder
git add --all .

# Give a comment to the commit if you want
echo "####################################"
echo "Write your commit comment!"
echo "####################################"

read input

# Committing to the local repository with a message containing the time details and commit text
curtime=$(date)
git commit -m "Comment : $input on $curtime"

# Push the local files to github

git push -u origin master


echo "################################################################"
echo "###################    Git Push Done      ######################"
echo "################################################################"

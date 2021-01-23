#!/bin/bash

function banner() {
	term_cols=$(tput cols) 
	str=":: $1 ::"
	for ((i=1; i<=`tput cols`; i++)); do echo -n ‾; done
	tput setaf 10; printf "%*s\n" $(((${#str}+$term_cols)/2)) "$str"; tput sgr0
	for ((i=1; i<=`tput cols`; i++)); do echo -n _; done
	printf "\n"
}

banner "Checking for newer files online."
git pull
# Below command will backup everything inside the project folder
git add --all .

banner "Backing up everything in project folder."
git add --all .

banner "Enter your commit message (optional)"

read input

# Committing to the local repository with commit comment if given

banner "Committing to the local repository."
git commit -m "$input"

banner "Pushing local files to Github."
git push -u origin master

banner "Git push completed...all done!"
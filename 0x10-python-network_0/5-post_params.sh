#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,and displays the size of the body of the response
curl -sX POST -d 'email=hr@holbertonschool.com' -d 'subject=I will always be here for PLD' "$1"

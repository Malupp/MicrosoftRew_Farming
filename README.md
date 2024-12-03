### Microsoft Rewards Automation Project
# Overview
This project is designed to automate Microsoft Rewards searches using the Bing search engine. It utilizes Pyautogui library because Selenium is detected and is banned by the rules.

# Prerequisites
Before running the project, ensure that you have the required Python modules installed. You can install them using the following commands:

- pip install Random-Word
- pip install pyautogui

# Execution
* Run the Script:

Execute the main script by running the following command in your terminal or command prompt:

- python pyautoguiScript.py

In order to let the script properly work, you should hover on the searchbar and wait for the script to run. The script will delete research and will enter a random word and then will click enter to do another research. This is a loop for 30 random words, it will take approximately 5 minutes, you can't move the mouse.

Yeah, it sure will be better if we use Selenium, but I already tried it and I get a restriction. With this script you can't be detected.

If you can run in a .bat file too.

You can open a note and write this:

@echo off
cd "your_path_here"
python "pyautoguiScript.py"
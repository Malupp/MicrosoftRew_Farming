### Microsoft Rewards Automation Project
# Overview
This project is designed to automate Microsoft Rewards searches using the Bing search engine. It utilizes the Selenium web automation library to perform searches on Bing and earn Microsoft Rewards points automatically.

# Prerequisites
Before running the project, ensure that you have the required Python modules installed. You can install them using the following commands:

- pip install selenium
- pip install Random-Word
- pip install python-dotenv

# Setup
* Create a .env File:
Inside the project folder, create a file named .env.

Open the .env file and add the following environment variables:

EMAIL_LOGIN=your_email@example.com
PASSWORD_LOGIN=your_password

Replace your_email@example.com and your_password with your Microsoft account email and password.

# Execution
* Run the Script:

Execute the main script by running the following command in your terminal or command prompt:

- python main.py

The project utilizes the Selenium WebDriver for Microsoft Edge. If needed, download the appropriate version of the WebDriver from the official Microsoft Edge WebDriver download page (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and add the WebDriver executable to your system's PATH.

The script is configured to use an existing Microsoft Edge user profile for the enrolled session. Make sure the specified user data directory exists and contains the necessary profile data.

## What directory use
In order to let the browser works, you should put in "edge_dir" the browser's linked path. You will see an example inside the main.py file 

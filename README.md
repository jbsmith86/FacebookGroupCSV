FacebookGroupCSV
================

Create a CSV file containing each member a facebook group in order to easily organize your group for events, parties, etc.


How to get your facebook API key:
Browse to https://developers.facebook.com/tools/explorer/
Login to your facebook account
Copy your access token to use when running the script. Note: This key will change every few hours.

Running the script

Mac/Linux:
Download the file CreateCSV.py
Open a terminal window and change directory to where you downloaded the file. 

Type the following:
python ./CreateCSV.py

Windows:
If you have python in your Path you can run the same command as mac/linux
Otherwise, open a command prompt and cd into where you downloaded the file then run the following:
C:\Python27\python.exe CreateCSV.py

Where "C:\Python27\python.exe" is the path to your python installation. If you don't have python you can download it here: http://www.python.org/getit/ 

Follow the on screen prompts to enter the url of the Facebook group (you must be a member), your API key and a csv filename.
Your CSV file will be generated and placed in the same directory.

Enjoy!

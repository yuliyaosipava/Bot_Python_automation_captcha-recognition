First of all it is neccessary to register chat in telegram:
To built this project you need to install:
1. Python
2. Virtual envourment:
- python -m venv myenv
- myenv\Scripts\activate
- 
3. First of all it is neccessary to install this modules:

pip install selenium webdriver-manager
pip install undetected_chromedriver as uc
pip install telegram
c:\Users\yu\vfs-appointment-bot\VFSBot>VFSBot>python-telegram-bot

From config1.ini login and password to register on site

4. Using the **VFSBot.py** file, we log in to the site using a login and password and enter the words "report + budget" in the search bar and a list of documents with the rtf extension is displayed.
These files are automatically downloaded to the computer.
5. Then, using the **convert4.py** file, files with the rtf extension are converted into files with the docx extension.
6.  **convert1.py** - files with the docx extension are converted into files with the xlsx extension
7. Then, using the **sobstv5.py** file, the share of own budgets is calculated in the files and saved in one file with the xlsx extension



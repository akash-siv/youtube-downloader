# Python program to change the
# current working directory


import os

# Function to Get the current
# working directory
def current_path():
	print("Current working directory")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
current_path()

# Changing the CWD
os.chdir(r'C:\\Program Files\\Google\\Chrome\\Application\\')
# os.system("chrome.exe")
os.system(r'chrome.exe -start-maximized -remote-debugging-port=8282 --user-data-dir="C:\Users\\akash\\PycharmProjects\\airdrop_collector\\chrome_data"')
# Printing CWD after
current_path()

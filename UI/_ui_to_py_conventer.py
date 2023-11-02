import os

command = """
pyuic5 MenuWindowUI.ui -o MenuWindowUI.py
pyuic5 PlayWindowUI.ui -o PlayWindowUI.py
pyuic5 SettingsWindowUI.ui -o SettingsWindowUI.py
pyuic5 StatisticsWindowUI.ui -o StatisticsWindowUI.py
"""
# os.system('ls -lah')
os.system(command)

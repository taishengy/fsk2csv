# fsk2csv
A script that converts from F-Secure KEY exported passwords (*.fsk) to a simple csv that can be imported into KeePass2.

This script takes passwords exported from F-Secure KEY (*.fsk files) and converts them into a simple csv that can be
imported into KeePass2 with the General CSV import tool.
KeePass2 only supports importing 5 fields from csv files: account, username, password, website, and comments. So don't
expect everything to come over perfectly.

Useful for transitioning to a Linux machine, which F-Secure doesn't develop a key client for, and the
Windows client doesn't run in WINE.

To use: Place this script in the directory with the .fsk file and run the script (Python3), it should create a "output.csv" file
in the same directory which can be imported into KeePass2

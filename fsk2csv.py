import json
import os
import sys

"""This script takes passwords exported from F-Secure KEY (*.fsk files) and converts them into a simple csv that can be
imported into KeePass2 with the General CSV import tool.
KeePass2 only supports importing 5 fields from csv files: account, username, password, website, and comments. So don't
expect everything to come over perfectly.

I wrote this because I found myself using a linux machine, which F-Secure doesn't develop a key client for.

To use: Place this script in the directory with the .fsk file and run the script, it should create a "output.csv" file
in the same directory which can be imported into KeePass2"""

# Some small helper functions
def split_ext(file_name):
    index = file_name.rfind('.')
    name = file_name[:index]
    ext = file_name[index:]
    return name, ext


def list_files(dir_path):
    files = []
    for item in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, item)):
            files.append(os.path.join(dir_path, item))
    return files


# Trying to find the .fsk file. Looks in current working directory, if 0 or more than 1 .fsk is found, ask for file path
cwd = os.getcwd()
files = list_files(cwd)
fsk_files = []
for file in files:
    name, ext = split_ext(file)
    if ext == '.fsk':
        fsk_files.append(file)

if len(fsk_files) == 1:
    file_path = fsk_files[0]
    print("Found file in {}".format(cwd))
else:
    file_path = input("Couldn't find figure out where the single .fsk was,\nPlease input the file path of the .fsk file:  ")
    if not os.path.isfile(file_path):
        print("{} doesn't appear to be an .fsk file, exiting...".format(file_path))
        sys.exit()

# Load files and open output file for writing
output_path = os.path.join(cwd, 'output.csv')
fsk_obj = open(file_path, mode='r', encoding='utf-8')
csv_obj = open(output_path, mode='w', encoding='utf-8')

# Open JSON as dictionary
fsk = json.loads(fsk_obj.read())
fsk_count = 0
csv_count = 0

# Iterate over every entry in the JSON format, pull the fields keepass cares about, format them into a string and write
for item in fsk['data']:
    entry = fsk['data'][item]
    fsk_count += 1

    account = entry['service']
    username = entry['username']
    password = entry['password']
    website = entry['url']
    comments = entry['notes']

    entry_string = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"\n".format(account, username, password, website, comments)
    csv_obj.write(entry_string)
    csv_count += 1

print("\n\nCounted {} Entries in .fsk file".format(fsk_count))
print("Wrote {} entries to: {}".format(csv_count, output_path))
if fsk_count != csv_count:
    print("Make sure things look right, different numbers of entries read and written!")

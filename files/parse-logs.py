import re 
import sys 
import os 
import io 
 
input = 'zero-client.log'
output = 'parsed.txt'

match_list = []
 
try:
    with io.open(input, mode = 'r') as f:
#     with io.open(input, mode = 'r', encoding='utf-16', errors = 'replace') as f: (if running on WSL)
        lines = f.readlines()
        for line in lines:
            if line.lower().find('web login'.lower()) > 0:
#                 print(line)
                match_list.append(line)
except IOError:
    print("the file you are trying to open doesn't exist.")

with open(output, "w+") as file:
    file.write("Parsed Logs:\n")
    match_list_clean = list(match_list)
    for item in xrange(0, len(match_list_clean)):
        print match_list_clean[item]
        file.write(match_list_clean[item] + "\n")
file.close()
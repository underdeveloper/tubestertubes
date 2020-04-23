import os
import csv
import auxilliary as flib
import B01

with open(os.path.dirname(__file__) + "\\" + "user.csv", mode = 'r') as f:
    reader = list(csv.reader(f))
    userfile = reader

for i in range (1, flib.length(userfile)):
    password = userfile[i][flib.find_idx(userfile, "Password")]
    userfile[i][flib.find_idx(userfile, "Password")] = B01.hash_pass(password)

with open(os.path.dirname(__file__) + "\\" + "user.csv", mode = 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(userfile)
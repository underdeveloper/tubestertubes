# Program F03
# Menambah entry ke user.csv

# KAMUS
class user:
    datacount = 7
    datadesc = ("nama pemain", "tanggal lahir pemain (DD/MM/YYYY)", "tinggi badan pemain (cm)", "username pemain", "password pemain", "role pemain", "saldo pemain")
    data = ["*" for i in range (datacount)]

# ALGORITMA PROGRAM UTAMA

import os
import datetime
import F01 as load

# REALISASI FUNGSI/PROSEDUR

def main(userfile):
    # procedure main (input/output userfile : array of array [0..6] of string)
    # I.S. userfile terdefinisi
    # F.S. ditambahkan suatu data baru ke userfile
    # KAMUS LOKAL
    # isUsernameOK, isBirthdayOK : boolean
    # i : integer
    # formatcheck : string
    isUsernameOK = False
    isBirthdayOK = False
    isHeightOK = False
    while ((isUsernameOK == False) or (isBirthdayOK == False) or (isHeightOK == False)):
        isUsernameOK = False
        isBirthdayOK = False
        isHeightOK = False
        for i in range (user.datacount):
            if (user.datadesc[i] == "username pemain"):
                user.data[i] = (str(input("Masukkan " + user.datadesc[i] + ": "))).lower()
                if (load.finddata(userfile, "Username", user.data[i]) == []):
                    isUsernameOK = True
            elif (user.datadesc[i] == "tanggal lahir pemain (DD/MM/YYYY)"):
                user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
                try:
                    formatcheck = datetime.datetime.strptime(user.data[i], "%d/%m/%Y")
                    isBirthdayOK = True
                except ValueError:
                    isBirthdayOK = False
            elif (user.datadesc[i] == "tinggi badan pemain (cm)"):
                user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
                try:
                    if (int(user.data[i]) >= 0):
                        isHeightOK = True
                except ValueError:
                    isHeightOK = False
            elif (user.datadesc[i] == "role pemain"):
                user.data[i] = str("Pemain")
            elif (user.datadesc[i] == "saldo pemain"):
                user.data[i] = str("0")
            else:
                user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
        if (isUsernameOK == False):
            print("Username sudah terdaftar. Silakan pilih username yang lain.")
        if (isBirthdayOK == False):
            print("Tanggal lahir Anda tidak valid. Silakan ulangi lagi.")
        if (isHeightOK == False):
            print("Tinggi badan Anda tidak valid. Silakan ulangi lagi.")
    userfile.append(user.data)
    print("")
    print("Selamat menjadi pemain, " + user.data[0] + ". Selamat bermain.")
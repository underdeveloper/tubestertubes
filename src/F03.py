# Program F03
# Menambah entry ke user.csv

import F01 as load
import auxilliary as flib
import B01

# KAMUS
# type custom :
# < constant datadesc : array [0..6] of string = ["nama pemain", "tanggal lahir pemain (DD/MM/YYYY)", "tinggi badan pemain (cm)", "username pemain", "password pemain", "role pemain", "saldo pemain"]
#   constant datacount : integer = flib.length(datadesc)
#   data : array [0..datacount] of string >
class custom:
    datadesc = ("nama pemain", "tanggal lahir pemain (DD/MM/YYYY)", "tinggi badan pemain (cm)", "username pemain", "password pemain", "role pemain", "saldo pemain")
    datacount = flib.length(datadesc)
    data = ["*" for i in range (datacount)]

# ALGORITMA PROGRAM UTAMA

# REALISASI FUNGSI/PROSEDUR

def main(userfile):
    # procedure main (input/output userfile : load.Rekaman, output user.data : custom.data)
    # I.S. userfile terdefinisi
    # F.S. ditambahkan suatu data baru ke userfile
    # KAMUS LOKAL
    # user : custom
    # isUsernameOK, isBirthdayOK, isHeightOK, isEmpty : boolean
    # i : integer
    # sandi : string
    # ALGORITMA
    user = custom()
    isUsernameOK = False
    isBirthdayOK = False
    isHeightOK = False
    isEmpty = False
    while ((isUsernameOK == False) or (isBirthdayOK == False) or (isHeightOK == False) or (isEmpty == True)):
        # Setiap pengulangan loop, semua field harus dicek ulang
        isUsernameOK = False
        isBirthdayOK = False
        isHeightOK = False
        isEmpty = False
        for i in range (user.datacount):
            # Handling username (tidak boleh ada 2 username sama)
            if (user.datadesc[i] == "username pemain"):
                user.data[i] = (str(input("Masukkan " + user.datadesc[i] + ": "))).lower()
                if (flib.find_baris_first(userfile.data, "Username", user.data[i]) == []):
                    isUsernameOK = True
            # Handling tanggal lahir (harus sesuai format DD/MM/YYYY)
            elif (user.datadesc[i] == "tanggal lahir pemain (DD/MM/YYYY)"):
                user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
                isBirthdayOK = flib.validate_date(user.data[i])
            # Handling tinggi badan (tidak boleh bilangan negatif)
            elif (user.datadesc[i] == "tinggi badan pemain (cm)"):
                user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
                try:
                    if (int(user.data[i]) >= 0):
                        isHeightOK = True
                except ValueError:
                    isHeightOK = False
            # Handling role (semua user yang di-generate dengan cara ini adalah "Pemain")
            elif (user.datadesc[i] == "role pemain"):
                user.data[i] = str("Pemain")
            # Handling saldo (semua "Pemain" memiliki saldo awal 0)
            elif (user.datadesc[i] == "saldo pemain"):
                user.data[i] = str("0")
            # BONUS 1! Handling password (di-hash via B01)
            elif (user.datadesc[i] == "password pemain"):
                sandi = str(input("Masukkan " + user.datadesc[i] + ": "))
                user.data[i] = B01.hash_pass(sandi)
            # Handling semua field yang tidak butuh penanganan khusus
            else:
                user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
        # Beritahu user jika ada field yang tidak terisi
        for i in range (user.datacount):
            if ((user.data[i] == "") or (sandi == "")): # (sandi == "") ditambahkan untuk mengakomodasi BONUS 1
                isEmpty = True
        if (isEmpty == True):
            print("Ada field yang lupa Anda isi. Silakan ulangi pengisian.")
        else:
            # Beritahu user jika ia salah meng-input suatu field
            if (isUsernameOK == False):
                print("Username sudah terdaftar. Silakan pilih username yang lain.")
            if (isBirthdayOK == False):
                print("Tanggal lahir Anda tidak valid. Silakan ulangi lagi.")
            if (isHeightOK == False):
                print("Tinggi badan Anda tidak valid. Silakan ulangi lagi.")
    # Simpan data user baru ke database
    load.store(userfile.name, flib.konsDot(userfile.data, user.data))
    print("Selamat menjadi pemain, " + user.data[0] + ". Selamat bermain.")
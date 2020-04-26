# Program F02
# Me-login-kan user ke program utama

# KAMUS

# ALGORITMA PROGRAM UTAMA

import auxilliary as flib
import B01

# REALISASI FUNGSI/PROSEDUR
def main(userfile):
    # function main (userfile : F01.Rekaman) -> array [0..1] of array [0..6] of string
    # Me-loginkan user yang sudah terdaftar ke dalam sistem.
    # KAMUS LOKAL
    # isUser, findpassword : boolean
    # username, password, spw : string
    # finduser : array [0..6] of string
    # user : array [0..1] of array [0..6] of string
    # ALGORITMA
    isUser = False
    while (isUser == False):
        username = str(input("Masukkan username: ")).lower()
        password = str(input("Masukkan password: "))
        # Cek apakah username valid
        finduser = flib.find_baris_first(userfile.data, "Username", username)
        if (finduser != []):
            # Cek apakah password valid
            spw = finduser[flib.find_idx(userfile.data, "Password")]
            findpassword = B01.verify(spw, password)
            if (findpassword == True):
                isUser = True
                print("")
                print("Selamat bersenang-senang, " + finduser[flib.find_idx(userfile.data, "Nama")] + "!")
                print("")
        if (isUser == False):
            print("Username/Password salah")
    user = [userfile.data[0], finduser]
    return user

def getuserdata(user, dataname):
    # function getuserdata (user : array [0..1] of array [0..6] of string, dataname : string) -> string
    # Mengambil data dari user yang telah login
    # KAMUS LOKAL
    # ALGORITMA
    return user[1][flib.find_idx(user, str(dataname))]
    # APLIKASI
    # (pada modul lain)
    # import F04 as login
    # user = array [0..1] of array [0..6] of string { berisi data user yang sedang login }
    # login.getuserdata(user, "Saldo")
    # >> <Saldo dari pemain yang sedang login>
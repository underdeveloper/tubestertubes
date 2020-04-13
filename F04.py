# Program F04
# Me-login-kan user ke program utama

# KAMUS

# ALGORITMA PROGRAM UTAMA

import F01 as load

# REALISASI FUNGSI/PROSEDUR
def main(userfile):
    # function main (userfile : array of array [0..6] of string) -> array [0..1] of array [0..6] of string
    # Me-loginkan user yang sudah terdaftar ke dalam sistem.
    # KAMUS LOKAL
    # isUser : boolean
    # username, password : string
    # finduser, findpassword : array [0..6] of string
    # user : array [0..1] of array [0..6] of string
    isUser = False
    while (isUser == False):
        username = str(input("Masukkan username: "))
        password = str(input("Masukkan password: "))
        finduser = load.finddata(userfile, "Username", username)
        findpassword = load.finddata(userfile, "Password", password)
        if ((finduser == findpassword) and (finduser != []) and (findpassword != [])):
            isUser = True
            print("")
            print("Selamat bersenang-senang, " + finduser[load.findidx(userfile, "Nama")] + "!")
        if (isUser == False):
            print("Username/Password salah")
    user = []
    user.append(userfile[0])
    user.append(finduser)
    return user
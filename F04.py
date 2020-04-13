# Program F04
# Me-login-kan user ke program utama

# KAMUS

# ALGORITMA PROGRAM UTAMA

import auxilliary as aux

# REALISASI FUNGSI/PROSEDUR
def main(userfile):
    # function main (userfile : array of array [0..6] of string) -> array [0..1] of array [0..6] of string
    # Me-loginkan user yang sudah terdaftar ke dalam sistem.
    # KAMUS LOKAL
    # isUser : boolean
    # username, password : string
    # finduser, findpassword : array [0..6] of string
    # user : array [0..1] of array [0..6] of string
    # ALGORITMA
    isUser = False
    while (isUser == False):
        username = str(input("Masukkan username: ")) # Feral
        password = str(input("Masukkan password: ")) # fer4l
        finduser = aux.find_baris_first(userfile.data, "Username", username)
        if (finduser != []):
            findpassword = aux.find_cell(finduser, password)
            if (password == findpassword):
                isUser = True
                print("")
                print("Selamat bersenang-senang, " + finduser[aux.find_idx(userfile.data, "Nama")] + "!")
                print("")
        if (isUser == False):
            print("Username/Password salah")
    user = [userfile.data[0], finduser]
    return user

def getuserdata(user, dataname):
    # function getuserdata (dataname : string) -> string
    # Mengambil data dari user yang telah login
    return user[1][aux.find_idx(user, str(dataname))]
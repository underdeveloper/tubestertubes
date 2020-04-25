#Program F05
#Program untuk pencarian pemain

#KAMUS

#ALGORITMA PROGRAM UTAMA

import F01 as load
import auxilliary as aux

#REALISASI FUNGSI/PROSEDUR
def main():
    # PROCEDURE main ()
    # Pencarian pemain pada sistem

    # KAMUS LOKAL
    # isUserValid = boolean
    # y = string
    # user = array[0..1] of array[0..6] of string
    # finduser = array[0..6] of string

    # ALGORITMA
    userfile = load.use("user.csv")
    
    isUserValid = False
    while isUserValid == False :
        y = str(input("Masukkan username: "))
        finduser = aux.find_baris_first(userfile.data,"Username",y)
        if finduser != [] :
            isUserValid = True
            print("")
            print("Nama Pemain: " + finduser[aux.find_idx(userfile.data,"Nama")])
            print("Tinggi Pemain: " + finduser[aux.find_idx(userfile.data,"Tinggi_Badan")])
            print("Tanggal Lahir Pemain: " + finduser[aux.find_idx(userfile.data,"Tanggal_Lahir")])
        else :
            isUserValid = False
            print("Username tidak ditemukan, silahkan coba lagi.")


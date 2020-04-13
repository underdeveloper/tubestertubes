#Program F05
#Program untuk pencarian pemain

#KAMUS

#ALGORITMA PROGRAM UTAMA

import F01 as load
<<<<<<< Updated upstream
=======
import auxilliary as aux
>>>>>>> Stashed changes

#REALISASI FUNGSI/PROSEDUR
def main(userfile):
    #function main(userfile : array of array [0..6] of string) -> array [0..1] of array [0..6] of string)
    #Pencarian pemain pada sistem

    #KAMUS LOKAL
    #isUserValid = boolean
    # y = string
    # user = array[0..1] of array[0..6] of string
    # finduser = array[0..6] of string

    isUserValid = False
    while isUserValid == False :
        y = str(input("Masukkan username :"))
<<<<<<< Updated upstream
        finduser = load.finddata(userfile,"Username",y)
        if finduser != [] :
            isUserValid = True
            print("")
            print("Nama Pemain: " + finduser[load.findidx(userfile,"Nama")])
            print("Tinggi Pemain: " + finduser[load.findidx(userfile,"Tinggi_Badan")])
            print("Tanggal Lahir Pemain: " + finduser[load.findidx(userfile,"Tanggal_Lahir")])
=======
        finduser = load.find_baris_first(userfile,"Username",y)
        if finduser != [] :
            isUserValid = True
            print("")
            print("Nama Pemain: " + finduser[load.find_idx(userfile,"Nama")])
            print("Tinggi Pemain: " + finduser[load.find_idx(userfile,"Tinggi_Badan")])
            print("Tanggal Lahir Pemain: " + finduser[load.find_idx(userfile,"Tanggal_Lahir")])
>>>>>>> Stashed changes
        else :
            isUserValid = False
            print("Username tidak ditemukan, silahkan coba lagi")
    user = []
<<<<<<< Updated upstream
    user.append(userfile[0])
    user.append(finduser)
=======
    aux.konsDot(user,[userfile[0]])
    aux.konsDot(user,[finduser])
>>>>>>> Stashed changes
    return user



#Program F05
#Program untuk pencarian pemain

#KAMUS

#ALGORITMA PROGRAM UTAMA

import F01 as load

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
        finduser = load.finddata(userfile,"Username",y)
        if finduser != [] :
            isUserValid = True
            print("")
            print("Nama Pemain: " + finduser[load.findidx(userfile,"Nama")])
            print("Tinggi Pemain: " + finduser[load.findidx(userfile,"Tinggi_Badan")])
            print("Tanggal Lahir Pemain: " + finduser[load.findidx(userfile,"Tanggal_Lahir")])
        else :
            isUserValid = False
            print("Username tidak ditemukan, silahkan coba lagi")
    user = []
    user.append(userfile[0])
    user.append(finduser)
    return user



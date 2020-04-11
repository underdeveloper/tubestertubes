#Program F10
#Program menerima kritik dan saran
#Menambah entry data ke kritiksaran.csv

#KAMUS
class kritiksaran :
    datacount = 4
    datadesc = ("ID_Wahana", "Tanggal_Kritik", "Username", "Isi_Kritik")
    data = ["*" for i in range (datacount)]

#ALGORITMA PROGRAM UTAMA
import F01 as load
import datetime
import os

#REALISASI FUNGSI/PROSEDUR
def main(userfile) :
    # prosedur main (input/output userfile : array of array [0..3] of string)
    # I.S. userfile sudah terdefinisi
    # F.S. ditambahkan suatu data baru ke userfile
    # KAMUS LOKAL
    # isDataValid, isUserValid, isValidID : boolean
    # i : integer
    # formatcheck : string
    isDateValid = False
    isUserValid = False
    isValidID = False
    while (isValidID == False) or (isDateValid == False) or (isUserValid == False) :
        for i in range(kritiksaran.datacount) :
            if kritiksaran.datadesc[i] == "ID_Wahana" :
                kritiksaran.data[i] = str(input("Masukkan " + kritiksaran.datadesc[i] + ": "))
                isValidID = True
            elif kritiksaran.datadesc[i] == "Tanggal_Kritik" :
                kritiksaran.data[i] = str(input("Masukkan " + kritiksaran.datadesc[i] + ": "))
                try:
                    formatcheck = datetime.datetime.strptime(kritiksaran.data[i], "%d/%m/%Y")
                    isDateValid = True
                except ValueError:
                    isDateValid = False
            elif kritiksaran.datadesc[i] == "Username" :
                kritiksaran.data[i] = str(input("Masukkan " + kritiksaran.datadesc[i] + ": "))
                isUserValid = True
            else :
                kritiksaran.data[i] = str(input("Masukkan " + kritiksaran.datadesc[i] + ": "))
    userfile.append(kritiksaran.data)
    print("Kritik dan saran Anda kami terima.")
        
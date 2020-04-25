#Program F10
#Program menerima kritik dan saran
#Menambah entry data ke kritiksaran.csv

#ALGORITMA PROGRAM UTAMA
import F01 as load
import auxilliary as aux

#REALISASI FUNGSI/PROSEDUR
def main(userfile) :
    # FUNCTION main (input/output userfile : array of array [0..3] of string)
    # I.S. userfile sudah terdefinisi
    # F.S. ditambahkan suatu data baru ke userfile
    # KAMUS LOKAL
    # isDataValid, isUserValid, isValidID : boolean
    # i : integer
    # formatcheck : string
    # ALGORITMA
    kritiksaran = load.use("kritiksaran.csv")
    isDateValid = False
    isUserValid = False
    isValidID = False
    array_kritik_baru = ["", "", "", ""]
    while (isValidID == False) or (isDateValid == False) or (isUserValid == False) :
        for i in range(kritiksaran.datacount) :
            if kritiksaran.datadesc[i] == "Tanggal_Kritik" :
                kritiksaran.data[i] = str(input("Masukkan " + kritiksaran.datadesc[i] + ": "))
                aux.validate_date(kritiksaran.data[i])
                isDateValid = True
            elif kritiksaran.datadesc[i] == "ID_Wahana" :
                kritiksaran.data[i] = str(input("Masukkan " + kritiksaran.datadesc[i] + ": "))
                isValidID = True
            else :
                kritiksaran.data[i] = str(input("Masukkan " + kritiksaran.datadesc[i] + ": "))
    kritik_added = aux.konsDot(kritiksaran.data, array_kritik_baru)
    userfile.rows = userfile.rows + 1
    userfile.data = kritik_added
    print("")
    print("Kritik dan saran Anda kami terima.")
    return userfile
        
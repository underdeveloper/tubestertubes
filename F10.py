#Program F10
#Program menerima kritik dan saran
#Menambah entry data ke kritiksaran.csv

#KAMUS

#ALGORITMA PROGRAM UTAMA
import F01 as load
import auxilliary as aux

#REALISASI FUNGSI/PROSEDUR
def main(pengguna) :
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
    kritiksaran = load.use("kritiksaran.csv")
    array_kritik_baru = ["Username","Tanggal Kritik","ID_Wahana","Isi Kritik"]
    while (isValidID == False) or (isDateValid == False) or (isUserValid == False) :
        for i in range(aux.length(array_kritik_baru)) :
            if array_kritik_baru[i] == "Username" :
                array_kritik_baru[i] = pengguna[1][aux.find_idx(pengguna,"Username")]
                isUserValid = True
            elif array_kritik_baru[i] == "Tanggal Kritik" :
                array_kritik_baru[i] = str(input("Masukkan Tanggal Kritik : "))
                isDateValid = True
            elif array_kritik_baru[i] == "ID Wahana" :
                array_kritik_baru[i] = str(input("Masukkan ID Wahana : "))
                isValidID = True
            else :
                array_kritik_baru[i] = str(input("Masukkan Isi Kritik : "))
    kritik_added = aux.konsDot(kritiksaran.data,array_kritik_baru)
    kritiksaran.data = kritik_added
    print("")
    print("Kritik dan saran Anda kami terima.")
    return kritiksaran
        
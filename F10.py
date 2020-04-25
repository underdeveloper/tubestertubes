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
    # I.S. kritiksaran sudah terdefinisi
    # F.S. ditambahkan suatu data baru ke kritiksaran
    # KAMUS LOKAL
    
    kritiksaran = load.use("kritiksaran.csv")
    array_kritik_baru = ["","","",""]
    array_kritik_baru[0] = pengguna[1][aux.find_idx(pengguna,"Username")]
    array_kritik_baru[1] = str(input("Masukkan tanggal hari ini :"))
    array_kritik_baru[2] = str(input("Masukkan ID Wahana :"))
    array_kritik_baru[3] = str(input("Masukkan kritik dan saran :"))
    kritik_added = aux.konsDot(kritiksaran.data,array_kritik_baru)
    kritiksaran.data = kritik_added
    print("")
    print("Kritik dan saran Anda kami terima.")
    return kritiksaran
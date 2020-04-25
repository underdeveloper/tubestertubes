# PROGRAM F12
# Menambahkan wahana baru bila user adalah admin.

# ALGORITMA
import auxilliary as aux
import F01 as load

# REALISASI FUNGSI/PROSEDUR
def main():
    # procedure main (input/output wahana : Rekaman)
    # I.S. wahana abstrak
    # F.S. Ditambahkan data wahana baru ke file wahana
    # Fungsi utama F12
    # Semua masukkan diasumsikan valid
    # KAMUS LOKAL
    # wahana : Rekaman
    # array_wahana_baru : array [0..4] of string
    # wahana_baru_added : Rekaman.data
    # ALGORITMA
    wahana = load.use("wahana.csv")
    array_wahana_baru = ["", "", "", "", ""]
    
    print ("Masukkan informasi wahana yang ditambahkan.")
    array_wahana_baru[0] = input("Masukkan ID Wahana: ")
    array_wahana_baru[1] = input("Masukkan Nama Wahana: ")
    array_wahana_baru[2] = input("Masukkan Harga Tiket: ")
    array_wahana_baru[3] = input("Batasan umur (anak-anak, dewasa, semua umur): ")
    array_wahana_baru[4] = input("Batasan tinggi (>170, tanpa batasan): ")
    
    wahana_baru_added = aux.konsDot(wahana.data,array_wahana_baru)
    load.store("wahana.csv", wahana_baru_added)

    print ("\nInfo wahana telah ditambahkan!")
    return 

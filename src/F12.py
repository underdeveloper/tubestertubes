# PROGRAM F12
# Menambahkan wahana baru bila user adalah admin

# Desainer : Stefanny
# Coder : Stefanny

# ALGORITMA
import auxilliary as aux
import F01 as load

# REALISASI FUNGSI/PROSEDUR
def main():
    # Fungsi utama F12
    # Semua masukkan diasumsikan valid
    wahana = load.use("wahana.csv")
    array_wahana_baru = ["", "", "", "", ""]
    
    print ("Masukkan informasi wahana yang ditambahkan.")
    array_wahana_baru[0] = input("Masukkan ID Wahana: ")
    array_wahana_baru[1] = input("Masukkan Nama Wahana: ")
    array_wahana_baru[2] = input("Masukkan Harga Tiket: ")
    array_wahana_baru[3] = input("Batasan umur (anak-anak, dewasa, semua umur): ")
    array_wahana_baru[4] = input("Batasan tinggi (>170, tanpa batasan): ")
    
    wahana_baru_added = aux.konsDot(wahana.data,array_wahana_baru)
    wahana.data = wahana_baru_added

    print ("\nInfo wahana telah ditambahkan!")
    return 

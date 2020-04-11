# Program F02
# Meng-update ke-7 file .csv

# KAMUS
filedesc = ("File User", "File Daftar Wahana", "File Pembelian Tiket", "File Penggunaan Tiket", "File Kepemilikan Tiket", "File Refund Tiket", "File Kritik dan Saran")

# ALGORITMA PROGRAM UTAMA

import os
import csv

# REALISASI FUNGSI/PROSEDUR

def main(datatosave):
    # procedure main (input datatosave : array [0..6] of string)
    # I.S. datatosave terdefinisi
    # F.S. isi dari datatosave telah disalin ke 7 file .csv
    # datatosave = load.file.data
    # KAMUS LOKAL
    # i, j : integer
    # ALGORITMA
    for i in range (len(datatosave)):
        # Masukkan <nama file> yang akan di-save
        filename = str(input("Masukkan nama " + filedesc[i] + ": "))
        # Save datatosave[i] ke <nama file>.csv
        with open(os.path.dirname(__file__) + "\\" + str(filename), mode = 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(datatosave[i])
    print("")
    print("Data berhasil disimpan!")
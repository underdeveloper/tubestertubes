# Program F02
# Meng-update ke-7 file .csv

# KAMUS
filedesc = ("File User", "File Daftar Wahana", "File Pembelian Tiket", "File Penggunaan Tiket", "File Kepemilikan Tiket", "File Refund Tiket", "File Kritik dan Saran", "File Laporan Kehilangan Tiket")

# ALGORITMA PROGRAM UTAMA

import os
import csv
import auxilliary as flib

# REALISASI FUNGSI/PROSEDUR

def main(datatosave):
    # procedure main (input datatosave : array [0..7] of array of string)
    # I.S. datatosave terdefinisi
    # F.S. isi dari datatosave telah disalin ke 7 file .csv
    # datatosave = load.files.data
    # KAMUS LOKAL
    # i, j : integer
    # ALGORITMA
    for i in range (flib.length(datatosave)):
        # Masukkan <nama file> yang akan di-save
        filename = str(input("Masukkan nama " + filedesc[i] + ": "))
        # Save datatosave[i] ke <nama file>.csv
        with open(os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + str(filename), mode = 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(datatosave[i].data)
    print("Data berhasil disimpan!")


def main_auto(datatosave):
    # procedure main (input datatosave : array [0..7] of string)
    # I.S. datatosave terdefinisi
    # F.S. isi dari datatosave telah disalin ke 8 file .csv
    # datatosave = load.files.data
    # KAMUS LOKAL
    # i, j : integer
    # ALGORITMA
    actual_filenames = ["user.csv", "wahana.csv", "pembelian.csv",
                        "penggunaan.csv", "tiket.csv", "refund.csv", "kritiksaran.csv", "hilang.csv"]
    for i in range(flib.length(actual_filenames)):
        filename = actual_filenames[i]
        # Save datatosave[i] ke <nama file>.csv
        with open(os.path.dirname(os.path.dirname(__file__)) + "\\data\\" + str(filename), mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datatosave[i].data)
    print("Data berhasil disimpan!")
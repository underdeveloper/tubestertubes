# Program F01
# Me-load ke-7 file .csv ke sistem

import os
import csv
import auxilliary as flib

# KAMUS
class Rekaman:
    # Tipe bentukan kamus data yang akan dipakai.
    # Rekaman : < name : string
    #             columns : int
    #             rows : int
    #             data : array [0..rows-1] of array [0..columns-1] of string
    def __init__(self, name = "", columns = 1, rows = 1):
        self.name = name
        self.columns = columns
        self.rows = rows
        self.data = [["*" for i in range(columns)] for j in range(rows)]
filedescription = ("File User", "File Daftar Wahana", "File Pembelian Tiket", "File Penggunaan Tiket", "File Kepemilikan Tiket", "File Refund Tiket", "File Kritik dan Saran")
filecount = flib.length(filedescription)
files = [Rekaman() for i in range (filecount)]
# Di atas ini adalah "Rekaman", suatu tipe bentukan, dan 3 variable : tuple [0..7], filecount : integer, files = array [0..filecount] of Rekaman()
# Saat modul ini dijalankan, data ke-7 file .csv akan disimpan ke dalam files
# files inilah yang kemudian akan diakses, diubah valuenya, dst selama program dijalankan
# Modul lain akan akan mengurus penyimpanan kembali files ke-7 file .csv

# REALISASI FUNGSI/PROSEDUR

def main():
    # procedure main (output files : array of Rekaman)
    # I.S. file.data terdefinisi sembarang
    # F.S. ke-7 file .csv di-load ke files
    # KAMUS LOKAL
    # i : integer
    # reader : _csv.reader object
    # ALGORITMA
    for i in range (filecount):
        # Masukkan <nama file> yang akan di-load
        files[i].name = str(input("Masukkan nama " + filedescription[i] + ": "))
        # Load <nama file>.csv ke file.data
        with open(os.path.dirname(__file__) + "\\" + str(files[i].name), mode = 'r') as f:
            reader = list(csv.reader(f))
            files[i].rows = flib.length(reader)
            files[i].columns = flib.length(reader[0])
            files[i].data = reader
    print("")
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
    print("")

def use(filename):
    # function use (filename : string) -> array of array of string
    # Memberikan copy file yang diminta dari versi yang ada di files
    # Syarat: Filename sudah benar.
    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    for i in range(0, filecount+1):
        if (files[i].name == filename):
            return files[i]
    # APLIKASI
    # (pada modul lain)
    # import F01 as load
    # load.use("user.csv")
    # >> files[0]


def store(filename, table_baru):
    # procedure store (input filename : string, output files[i] : Rekaman)
    # Menyetor table_baru ke file bernama filename
    # KAMUS LOKAL
    # i : integer
    # isStored : boolean
    # ALGORITMA
    isStored = False

    for i in range(0, filecount+1):
        if i == filecount and not isStored:
            print("ERROR : Filename salah.")
        elif (files[i].name == filename):
            files[i].rows = flib.length(table_baru)
            files[i].columns = flib.length(table_baru[0])
            files[i].data = table_baru
            isStored = True
    # APLIKASI
    # (pada modul lain)
    # import F01 as load
    # A : array of array of string
    # load.store("user.csv", A)
    # >> files[0] <- A

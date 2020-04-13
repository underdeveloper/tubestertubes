# Program F01
# Me-load ke-7 file .csv ke sistem

# KAMUS

import auxilliary as aux

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
filecount = aux.length(filedescription)
files = [Rekaman() for i in range (filecount)]

# Di atas ini adalah "Rekaman", suatu tipe bentukan, dan 3 variable : tuple [0..7], filecount : integer, files = array [0..filecount] of Rekaman()
# Saat modul ini dijalankan, data ke-7 file .csv akan disimpan ke dalam files
# files inilah yang kemudian akan diakses, diubah valuenya, dst selama program dijalankan
# Modul lain akan akan mengurus penyimpanan kembali files ke-7 file .csv

# ALGORITMA PROGRAM UTAMA

import os
import csv

# REALISASI FUNGSI/PROSEDUR

def main():
    # procedure main (output data : file)
    # I.S. file.data terdefinisi sembarang
    # F.S. ke-7 file .csv di-load ke file.data
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
            files[i].rows = aux.length(reader)
            files[i].columns = aux.length(reader[0])
            files[i].data = reader
    print("")
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
    print("")

def use(filename):
    # function use (filename : string) -> string
    # Memberikan copy file yang diminta dari versi yang ada di file.name
    # KAMUS LOKAL
    # i, j, k : integer
    # isFound : boolean
    # filefound : array [0..files[i].rows] of array [0..files[i].columns] of string
    # ALGORITMA
    try:
        i = 0
        isFound = False
        while ((i < filecount) and (isFound == False)):
            if (str(files[i].name) == filename):
                isFound = True
                filefound = [["*" for k in range (files[i].columns)] for j in range (files[i].rows)]
                filefound = files[i]
            i = i + 1
        if (isFound == False):
            raise ValueError
        return filefound
    except ValueError:
        print("ERROR: Invalid filename.")
        

def store(filename, new_table):
    # procedure store (input filename : string, input new_table : array of array of string)
    # Meng-update salah satu elemen file.name yang sesuai dengan nama file yang di-input
    # KAMUS LOKAL
    # i : integer
    # isStored : boolean
    # ALGORITMA
    i = 0
    isStored = False
    try:
        while ((i < filecount) and (isStored == False)):
            if (files[i].name == filename):
                files[i].data = new_table
                isStored = True
            i = i + 1
        if (isStored == False):
            raise ValueError
    except ValueError:
        print("ERROR: Invalid filename.")

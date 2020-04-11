# Program F01
# Me-load ke-7 file .csv ke sistem

# KAMUS
class file:
    count = 7
    description = ("File User", "File Daftar Wahana", "File Pembelian Tiket", "File Penggunaan Tiket", "File Kepemilikan Tiket", "File Refund Tiket", "File Kritik dan Saran")
    name = ["*" for i in range (count)]
    data = ["*" for i in range (count)]
# Di atas ini adalah "file", suatu tipe bentukan
# Saat modul ini dijalankan, data ke-7 file .csv akan disimpan ke dalam file.data
# file.data inilah yang kemudian akan diakses, diubah valuenya, dst selama program dijalankan
# Modul lain akan akan mengurus penyimpanan kembali file.data ke-7 file .csv

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
    for i in range (file.count):
        # Masukkan <nama file> yang akan di-load
        file.name[i] = str(input("Masukkan nama " + file.description[i] + ": "))
        # Load <nama file>.csv ke file.data
        with open(os.path.dirname(__file__) + "\\" + str(file.name[i]), mode = 'r') as f:
            reader = csv.reader(f)
            file.data[i] = list(reader)
    print("")
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")

def use(filename):
    # function use (filename : string) -> string
    # Memberikan copy file yang diminta dari versi yang ada di file.name
    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    try:
        for i in range (len(file.name)):
            if (str(filename) == file.name[i]):
                return file.data[i]
            else:
                raise ValueError
    except ValueError:
        print("ERROR: Invalid filename.")

def store(filename):
    # function store (filename : string) -> string
    # Meng-update salah satu elemen file.name yang sesuai dengan nama file yang di-input
    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    try:
        for i in range (len(file.name)):
            if(str(filename) == file.name[i]):
                file.name[i] = filename
            else:
                raise ValueError
    except ValueError:
        print("ERROR: Invalid filename.")

def find_idx(array, colname):
    # function find_idx (colname : string) -> integer
    # Mencari nomor indeks suatu kolom bernama colname pada array array
    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    for i in range (len(array[0])):
        if (str(array[0][i]) == str(colname)):
            return int(i)

def find_baris(array, colname, keyword):
    # function find_baris (array : array of array of string, colname : string, keyword : string) -> array of string
    # Mencari baris yang tersimpan dalam array
    # KAMUS LOKAL
    # i, colidx : integer
    # datafound : array of string
    # isFound : boolean
    # ALGORITMA
    for i in range (len(array[0])):
        if (array[0][i] == colname):
            colidx = int(i)
    isFound = False
    for i in range (len(array)):
        if (array[i][colidx] == keyword):
            datafound = array[i]
            isFound = True
    if (isFound == True):
        return datafound
    else:
        datafound = []
        return datafound

def find_kolom(array, colname, keyword):
    # function find_kolom (array : array of array of string, colname : string, keyword : string) -> array of string
    # Mencari kolom yang tersimpan dalam array
    # KAMUS LOKAL
    # i, colidx : integer
    # kolom : array of string
    # isFound : boolean
    # ALGORITMA
    isFound = False
    for i in range (len(array[0])):
        if (array[0][i] == colname):
            colidx = int(i)
            isFound = True
    if (isFound == True):
        kolom = ["*" for i in range (len(array))]
        for i in range (len(array)):
            kolom[i] = array[i][colidx]
        return kolom
    else: # isFound == False
        return []

def find_cell(array, keyword):
    # function find_cell (array : array of string, keyword : string) -> string
    # Mencari cell tertentu yang tersimpan dalam array 1 dimensi
    # KAMUS LOKAL
    # i : integer
    # isFound : boolean
    # cellfound = string
    # ALGORITMA
    i = 0
    isFound = False
    while ((i < len(array)) and (isFound == False)):
        if (array[i] == keyword):
            cellfound = array[i]
            isFound = True
        i = i + 1
    if (isFound == True):
        return cellfound
    else: # isFound == False
        return ""

def search(array, result_column, from_column, from_data):
    # function search(array : array of array of string, result_column : string, from_column : string, from_data : string) -> string
    # SYARAT: result_column, from_column, from_data valid
    # KAMUS LOKAL
    # data : array of string
    # idx : integer
    # ALGORITMA
    data = find_baris(array, from_column, from_data)
    idx = find_idx(array, result_column)
    return data[idx]
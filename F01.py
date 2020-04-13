# Program F01
# Me-load ke-7 file .csv ke sistem

# KAMUS
class FileCSV:
    def __init__(self, count=7):
        self.count = count
        self.description = ("File User", "File Daftar Wahana", "File Pembelian Tiket", "File Penggunaan Tiket", "File Kepemilikan Tiket", "File Refund Tiket", "File Kritik dan Saran")
        self.name = ["*" for i in range (self.count)]
        self.data = ["*" for i in range (self.count)]

file = FileCSV()

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

    for string in file.name:
        print(string)

def use(filename):
    # function use (filename : string) -> string
    # Memberikan copy file yang diminta dari versi yang ada di file.name

    # >>> Asumsi filename sudah benar. <<<

    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    for i in range(0,file.count+1):
        if (str(file.name[i]) == filename):
            return file.data[i]
        elif i == file.count:
            return None # Kalau gaada, dia return None. INI BELUM DIUJI AKAN MERUSAK APA

def store(filename):
    # procedure store (input filename : string, output file.data : FileCSV)
    # Meng-update salah satu elemen file.name yang sesuai dengan nama file yang di-input

    # >>> Asumsi filename sudah benar. <<<

    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    for i in range(0, file.count+1):
        if (str(file.name[i]) == filename):
            file.name[i] = filename
        elif i == file.count:
            print("ERROR : Filename salah.")

def find_idx(table, colname):
    # function find_idx (colname : string) -> integer
    # Mencari nomor indeks suatu kolom bernama colname pada array array
    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    for i in range (len(table[0])):
        if (str(table[0][i]) == str(colname)):
            return int(i)

def find_baris_first(table, colname, keyword, startidx = 0):
    # function find_baris_first (array : array of array of string, colname : string, keyword : string) -> array of string
    # Mencari baris pertama dengan keyword tertentu yang tersimpan dalam table
    # KAMUS LOKAL
    # i, colidx : integer
    # datafound : array of string
    # isFound : boolean
    # ALGORITMA
    if (startidx >= (len(table))):
        datafound = []
        return datafound
    else: # (startidx < len(table))
        for i in range (len(table[0])):
            if (table[0][i] == colname):
                colidx = int(i)
        isFound = False
        i = startidx
        while ((i < (len(table))) and (isFound == False)):
            if (table[i][colidx] == keyword):
                datafound = table[i]
                isFound = True
            i = i + 1
        if (isFound == True):
            return datafound
        else:
            datafound = []
            return datafound

def find_baris_all(table, colname, keyword):
    # function find_baris_all (array : array of array of string, colname : string, keyword : string) -> array of array of string
    # Mencari baris yang tersimpan dalam table
    # KAMUS LOKAL
    # i, colidx : integer
    # datafound : array of array of string
    # ALGORITMA
    for i in range (len(table[0])):
        if (table[0][i] == colname):
            colidx = int(i)
    datafound = []
    for i in range (len(table)):
        if (table[i][colidx] == keyword):
            datafound.append(table[i])
    return datafound

def find_kolom(table, colname, keyword):
    # function find_kolom (table : array of array of string, colname : string, keyword : string) -> array of string
    # Mencari kolom yang tersimpan dalam table
    # KAMUS LOKAL
    # i, colidx : integer
    # kolom : array of string
    # isFound : boolean
    # ALGORITMA
    isFound = False
    for i in range (len(table[0])):
        if (table[0][i] == colname):
            colidx = int(i)
            isFound = True
    if (isFound == True):
        kolom = ["*" for i in range (len(table))]
        for i in range (len(table)):
            kolom[i] = table[i][colidx]
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

def search(table, result_column, from_column, from_data):
    # function search(table : array of array of string, result_column : string, from_column : string, from_data : string) -> string
    # SYARAT: result_column, from_column, from_data valid
    # KAMUS LOKAL
    # data : array of string
    # idx : integer
    # ALGORITMA
    data = find_baris_first(table, from_column, from_data)
    idx = find_idx(table, result_column)
    return data[idx]

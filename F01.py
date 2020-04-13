# Program F01
# Me-load ke-7 file .csv ke sistem

import os
import csv  # Library eksternal untuk mengakses file
import auxilliary as aux  # Library internal, berisi fungsi pembantu

# KAMUS
class Rekaman:
    # Tipe bentukan kamus data yang akan dipakai.
    # Rekaman : < name : string
    #             columns : int
    #             rows : int
    #             data : array [0..rows-1] of array [0..columns-1] of string
    def __init__(self, name="", columns=1, rows=1):
        self.name = name
        self.columns = columns
        self.rows = rows
        self.data = [["*" for i in range(columns)] for j in range(rows)]

# REALISASI FUNGSI/PROSEDUR

# File-file yang kita perlukan. bisa diganti nanti.
filedescs = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "File Kritik dan Saran"]
files = []

def main(filedescs):
    # procedure main (input filenames : array of string
    # output data : file)
    # I.S. file.data terdefinisi sembarang
    # F.S. ke-7 file .csv di-load ke file.data
    # KAMUS LOKAL
    # i : integer
    # reader : _csv.reader object
    # ALGORITMA
    
    file_amount = aux.arr_length(filedescs)
    files = [Rekaman() for i in range(file_amount)] # Array berisi kamus data
    
    for i in range(file_amount):
        # Pemasukan nama file eksternal (csv) yang akan dimuat
        files[i].name = input("Masukkan nama file " + filedescs[i] + ": ")

        # Memuatkan <ext_file>.csv ke kamus data
        with open(os.path.dirname(__file__) + "\\" + files[i].name, 'r') as f:
            file_contents = list(csv.reader(f))

            files[i].columns = aux.arr_length(file_contents[0])
            files[i].rows = aux.arr_length(file_contents)

            files[i].data = file_contents
    
    print("\nFile-file telah dimuat.\n")

def get_data(filename):
    # function get_data (filename : string) -> array of array of string
    # Mengeluarkan tabel yang merupakan isi dari data yang telah dimuat.
    # Syarat: File bernama filename sudah pasti telah dimuat.

    found = False

    for file in files:
        if file.name == filename:
            return file.data
    
    if not found:
        return None

def store_data(filename, new_table):
    # prosedur store_data(input filename : string, output file : Rekaman)
    # I.S. file belum diganti
    # F.S. file telah diganti user
    # Syarat: File bernama filename sudah pasti telah dimuat.

    for file in files:
        if file.name == filename:
            file.data = new_table

# def findidx(array, colname):
#     # function findidx (colname : string) -> integer
#     # Mencari nomor indeks suatu kolom bernama colname pada array array
#     # KAMUS LOKAL
#     # i : integer
#     # ALGORITMA
#     for i in range (len(array[0])):
#         if (str(array[0][i]) == str(colname)):
#             return int(i)

# def finddata(array, colname, keyword):
#     #function finddata (array : array of array of string, colname : string, keyword : string) -> array of string
#     # Mencari data yang tersimpan dalam array
#     # KAMUS LOKAL
#     # i, colidx : integer
#     # datafound : array of string
#     # isFound : boolean
#     # ALGORITMA
#     for i in range (len(array[0])):
#         if (array[0][i] == colname):
#             colidx = int(i)
#     isFound = False
#     for i in range (len(array)):
#         if (array[i][colidx] == keyword):
#             datafound = array[i]
#             isFound = True
#     if (isFound == True):
#         return datafound
#     else:
#         datafound = []
#         return datafound

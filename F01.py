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

# File-file yang kita perlukan. bisa diganti nanti. Ini ditaruh di main.py
filedescs = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran"]
files = []

def main(filedescs):
    # procedure main (input filenames : array of string
    #                 output data : file)
    # I.S. file.data terdefinisi sembarang
    # F.S. ke-7 file .csv di-load ke files
    # KAMUS LOKAL
    # i : integer
    # reader : _csv.reader object
    # ALGORITMA
    
    file_amount = aux.length(filedescs)
    files = [Rekaman() for i in range(file_amount)] # Array berisi kamus data
    
    for i in range(file_amount):
        # Pemasukan nama file eksternal (csv) yang akan dimuat
        files[i].name = input("Masukkan nama file " + filedescs[i] + ": ")

        # Memuatkan <ext_file>.csv ke kamus data
        with open(os.path.dirname(__file__) + "\\" + files[i].name, 'r') as f:
            file_contents = list(csv.reader(f))

            files[i].columns = aux.length(file_contents[0])
            files[i].rows = aux.length(file_contents)

            files[i].data = file_contents
    
    print("\nFile-file telah dimuat.\n")

def get(filename):
    # function get (files : array of Rekaman, filename : string) -> array of array of string
    # Mengeluarkan tabel yang merupakan isi dari data yang telah dimuat.
    # Syarat: File bernama filename sudah pasti telah dimuat.

    # KAMUS LOKAL
    # found : boolean
    # file : Rekaman

    # ALGORITMA UTAMA
    found = False

    for file in files:
        if file.name == filename:
            found = True
            return file.data
    
    if not found:
        return None

def store(filename, new_table):
    # prosedur store_data(input filename : string, input/output files : array of Rekaman)
    # I.S. file belum diganti
    # F.S. file telah diganti user
    # Syarat: File bernama filename sudah pasti telah dimuat.

    for file in files:
        if file.name == filename:
            file.data = new_table
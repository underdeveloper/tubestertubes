# Program F01
# Me-load ke-7 file .csv ke sistem

import csv
import auxilliary as flib

# KAMUS
# Tipe bentukan kamus data yang akan dipakai.
# type Rekaman : < name : string
#                  columns : integer
#                  rows : integer
#                  data : array [0..rows-1] of array [0..columns-1] of string >
class Rekaman:
    def __init__(self, name = "", columns = 1, rows = 1):
        self.name = name
        self.columns = columns
        self.rows = rows
        self.data = [["*" for i in range(columns)] for j in range(rows)]
# constant filedescription : array [0..7] of string = ["File User", "File Daftar Wahana", "File Pembelian Tiket", "File Penggunaan Tiket", "File Kepemilikan Tiket", "File Refund Tiket", "File Kritik dan Saran", "File Laporan Kehilangan Tiket"]
filedescription = ("File User", "File Daftar Wahana", "File Pembelian Tiket", "File Penggunaan Tiket", "File Kepemilikan Tiket", "File Refund Tiket", "File Kritik dan Saran", "File Laporan Kehilangan Tiket")
# constant filecount : integer = flib.length(filedescription)
filecount = flib.length(filedescription)
# files : array [0..filecount-1] of Rekaman
# Saat modul ini dijalankan, data ke-8 file .csv akan disimpan ke dalam files
# files inilah yang kemudian akan diakses, diubah valuenya, dst. selama program dijalankan
# Modul lain akan akan mengurus penyimpanan kembali files ke 8 file .csv

# ALGORITMA PROGRAM UTAMA
files = [Rekaman() for i in range (filecount)]

# REALISASI FUNGSI/PROSEDUR

def main():
    # procedure main (output files : array [0..7] of Rekaman)
    # I.S. Rekaman ter-assign ke files
    # F.S. ke-8 file .csv di-load ke files
    # KAMUS LOKAL
    # filename : string
    # i, filerows, filecolumns : integer
    # reader : _csv.reader object
    # f : SEQFILE of
    #   (*) data : Rekaman.data
    #   (1) ""
    # ALGORITMA
    for i in range (filecount):
        # Masukkan <nama file> yang akan di-load
        filename = str(input("Masukkan nama " + filedescription[i] + ": "))
        # Load <nama file>.csv ke file.data
        with open(__file__[:-10] + "data\\" + str(filename), mode = 'r') as f:
            reader = list(csv.reader(f))
            filerows = flib.length(reader)
            filecolumns = flib.length(reader[0])
            files[i].__init__(filename, filerows, filecolumns)
            files[i].data = reader
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")

def main_auto():
    # procedure main_auto (output files : array [0..7] of Rekaman)
    # I.S. file.data terdefinisi sembarang
    # F.S. ke-8 file .csv di-load ke files
    # main_auto() merupakan prosedur sama dengan main(), tetapi diotomasikan.
    # Prosedur ini dipakai untuk masa testing program ini, dan akan dimatikan
    # saat program final dikeluarkan.
    # KAMUS LOKAL
    # filename : string
    # i, filerows, filecolumns : integer
    # reader : _csv.reader object
    # f : SEQFILE of
    #   (*) data : Rekaman.data
    #   (1) ""
    # actual_filenames : array [0..7] of string
    # ALGORITMA
    actual_filenames = ["user.csv", "wahana.csv", "pembelian.csv", 
    "penggunaan.csv", "tiket.csv", "refund.csv", "kritiksaran.csv", "hilang.csv"]
    for i in range(flib.length(actual_filenames)):
        filename = actual_filenames[i]
        with open(__file__[:-10] + "data\\" + actual_filenames[i], mode='r') as f:
            reader = list(csv.reader(f))
            filerows = flib.length(reader)
            filecolumns = flib.length(reader[0])
            files[i].__init__(filename, filerows, filecolumns)
            files[i].data = reader
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")

def use(filename):
    # function use (filename : string) -> Rekaman
    # Memberikan copy file yang diminta dari versi yang ada di files.name
    # KAMUS LOKAL
    # i, j, k : integer
    # isFound : boolean
    # filefound : Rekaman
    # ALGORITMA
    try:
        i = 0
        isFound = False
        while ((i < filecount) and (isFound == False)):
            if (str(files[i].name) == filename):
                isFound = True
                filefound = files[i]
            i = i + 1
        if (isFound == False):
            raise ValueError
        return filefound
    except ValueError:
        print("Galat: Filename salah.")
    # APLIKASI
    # (pada modul lain)
    # import F01 as load
    # load.use("user.csv")
    # >> files[0]

def store(filename, new_table):
    # procedure store (input filename : string, input new_table : Rekaman.data, output files[i] : Rekaman)
    # Meng-update (deep copy) salah satu elemen files yang sesuai dengan nama file yang di-input
    # KAMUS LOKAL
    # i, j, newrows, newcolumns : integer
    # isStored : boolean
    # newfile : Rekaman
    # ALGORITMA
    i = 0
    isStored = False
    try:
        while ((i < filecount) and (isStored == False)):
            if (files[i].name == filename):
                newrows = flib.length(new_table)
                newcolumns = flib.length(new_table[0])
                newfile = Rekaman()
                newfile.__init__(filename, newcolumns, newrows)
                for j in range (flib.length(new_table)):
                    newfile.data[j] = new_table[j][:]
                files[i] = newfile
                isStored = True
            i = i + 1
        if (isStored == False):
            raise ValueError
    except ValueError:
        print("GALAT: Filename salah.")
    # APLIKASI
    # (pada modul lain)
    # import F01 as load
    # A : array of array of string
    # load.store("user.csv", A)
    # >> files[0] <- A
# LIBRARY F01
# Me-load ke-7 file .csv ke sistem

import os
import csv

# KAMUS
class FileCSV:
    ''' class FileCSV merupakan tipe bentukan yang merupakan dictionary berisi data dari file CSV. '''
    def __init__(self):
        self.contents = {}
        ''' self.contents adalah Dictionary yang berisi data dari file CSV. 
        Key adalah judul kolom, value adalah list yang berisi isi file'''


class FileCollection:
    ''' class FileCollection merupakan tipe bentukan yang merupakan semua file yang dibutuhkan. '''
    def __init__(self, length=7):
        self.length = length
        self.filenames = ["*" for i in range(length)]
        self.files = [FileCSV() for i in range(length)]

# REALISASI FUNGSI/PROSEDUR
def main():
    # FUNGSI main () -> file

    # KAMUS LOKAL
    # descriptions : tuple
    # length : integer
    # i, j, k : integer
    # koleksi_file : FileCollection
    # filename : string
    # data : list

    # ALGORITMA
    descriptions = ("User", "Daftar Wahana", "Pembelian Tiket",
                    "Penggunaan Tiket", "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran")
    length = len(descriptions)
    koleksi_file = FileCollection(length)

    # Nama <nama_file>.csv dimasukkan ke koleksi_file.filenames
    koleksi_file.filenames = list(descriptions)

    for i in range(koleksi_file.length):
        # Masukkan <nama file> yang akan di-load
        filename = str(input("Masukkan nama file " + descriptions[i] + ": "))

        # Load <nama file>.csv ke koleksi_file.files
        with open(os.path.dirname(__file__) + "\\" + str(filename), mode='r') as f:
            data = list(csv.reader(f)) # Isi dari file csv yang dibuka
            for j in range(len(data[0])):  # Sesuai banyak kolom di file csv
                # Mengisi dictionary contents dengan isi dari file csv
                koleksi_file.files[i].contents.update(
                    {data[0][j]: [data[k][j] for k in range(1, len(data))]}
                )

    print("\nFile telah di-load.")
    return koleksi_file

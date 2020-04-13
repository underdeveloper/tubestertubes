# Fungsi-fungsi pembantu

import re

def arr_length(some_array):
    # FUNCTION length (some_array : array) -> integer
    # Mengeluarkan panjang efektif dari array.

    # KAMUS LOKAL
    # count : integer

    # ALGORITMA UTAMA
    count = 0
    for element in some_array:
        count = count + 1
    return count

def merge(table1, table2):
    # function merge (table1 : array of array of string, 
    #                 table2 : array of array of string) -> array of array of string
    # Menggabungkan 2 tabel. Urutan harus diperhatikan.
    # Syarat: table1 dan table2 harus memiliki banyak kolom yang sama.

    # KAMUS LOKAL
    # length1, length2, length3 : integer
    # columns, count : int
    # table3 : array of array of string

    # ALGORITMA
    length1 = arr_length(table1)
    length2 = arr_length(table2)
    length3 = length1 + length2
    
    columns = arr_length(table1[0])

    table3 = [["*" for i in range(columns)] for j in range(length3)]
    
    count = 0
    while count < length3:
        if count < length1:
            table3[count] = table1[count]
        else: # length >= length1
            table3[count] = table2[count-length1]
        count += 1

    return table3

file_wahana_data = [
    [], [], []
]

data_baru = [
    [], []
]


print ( merge(file_wahana_data, data_baru) )


def contains(arr_str, element):
    # FUNCTION contains (arr_str : list, element : string) -> boolean
    # Mengecek apabila string 'element' berada pada array of string 'arr_str;

    # KAMUS LOKAL
    #

    # ALGORTIMA UTAMA

    if element in arr_str:
        return True
    else:
        return False

def find_idx(arr_str, element):
    # FUNCTION find_idx (arr_str : list, element : string) -> integer
    # Mencari nomor indeks suatu elemen array 'elemen' pada array of string 'arr_str'

    # KAMUS LOKAL
    # i : integer

    # ALGORITMA UTAMA

    for i in range(len(arr_str)):
        if (str(arr_str[i]) == str(element)):
            return int(i)

def validate_date(date):
    # FUNCTION validate_date (date : string) -> boolean
    # Mengecek apabila string 'date' sesuai dengan format tanggal (DD/MM/YYYY)
    # dan sesuai kalender (apakah hari sesuai per bulan)

    # KAMUS LOKAL
    # day, month, year : integer

    # ALGORTIMA UTAMA

    # Pengecekan apabila 'date' sesuai format DD/MM/YYYY
    r = re.compile(r'\d\d/\d\d/\d\d\d\d')
    if r.fullmatch(date) is None:
        return False

    # Pengecekan apabila 'date' sesuai kalender
    try:
        day, month, year = map(int, date.split('/'))
        if (year < 1 or year > 9999): # Jika tahun salah
            return False
        elif (month in [1,3,5,7,8,10,12]) and (day >= 1 and day <= 31):
            return True
        elif (month in [4,6,9,11]) and (day >= 1 and day <= 30):
            return True
        elif (month == 2):
            if ((year % 4 == 0) and (not (year % 100 != 0)) or (year % 400 == 0)): # Jika tahun kabisat
                if (day >= 1 and day <= 29):
                    return True
            else: # Jika tahun bukan kabisat
                if (day >= 1 and day <= 28):
                    return True
        else:
            return False
    except:
        return False

def input_date():
    # PROCEDURE input_date (output date : string)
    # Prosedur untuk pemasukan tanggal, akan diulang sampai tanggal valid.

    # KAMUS LOKAL
    # date : string

    # ALGORITMA UTAMA
    date = ""
    while True:
        date = input()
        if validate_date(date):
            break
        print("Tanggal salah format (Format: DD/MM/YYYY) atau tidak sesuai kalender!")
    return date

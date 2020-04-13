# Fungsi-fungsi pembantu

import re

def length(some_array):
    # FUNCTION length (some_array : array) -> integer
    # Mengeluarkan panjang efektif dari array.

    # KAMUS LOKAL
    # count : integer

    # ALGORITMA UTAMA
    count = 0
    while (some_array[0:] != []):
        count += 1
        some_array = some_array[1:]
    return count

# print(length(['1','1','2']))

def konsdot(table1, table2):
    # function konsdot (table1 : array of array of string, 
    #                 table2 : array of array of string) -> array of array of string
    # Menggabungkan 2 tabel. Urutan harus diperhatikan.
    # Syarat: table1 dan table2 harus memiliki banyak kolom yang sama.

    # KAMUS LOKAL
    # length1, length2, length3 : integer
    # columns, count : int
    # table3 : array of array of string

    # ALGORITMA
    length1 = length(table1)
    length2 = length(table2)
    length3 = length1 + length2
    
    columns = length(table1[0])

    table3 = [["*" for i in range(columns)] for j in range(length3)]
    
    count = 0
    while count < length3:
        if count < length1:
            table3[count] = table1[count]
        else: # length >= length1
            table3[count] = table2[count-length1]
        count += 1

    return table3


def find_column_idx(table, column):
    # function find_column_idx (column : string) -> integer
    # Mencari nomor indeks suatu kolom bernama column dari array of array of string bernama table

    # KAMUS LOKAL
    # found : boolean
    # file : Rekaman

    # ALGORITMA UTAMA
    found = False

    for idx in range(length(table[0])):
        if table[0][idx] == column:
            found = True
            return idx

    if not found:
        return None


def find_baris_first(table, column, keyword, startidx=0):
    # function find_baris_first(table : array of array of string,
    #                         column : string, keyword : string) -> array of string
    # Mengeluarkan baris pertama yang memiliki nilai <keyword> pada kolom <column> dalam table <table>

    # KAMUS LOKAL
    # i, colidx : integer
    # first_row : array of string
    # isFound : boolean

    # ALGORITMA UTAMA
    if (startidx >= (length(table))):
        first_row = []

    else:  # (startidx < length(table))
        colidx = find_column_idx(table, column)

        isFound = False
        i = startidx

        while ((i < (length(table))) and (isFound == False)):
            if (table[i][colidx] == keyword):
                first_row = table[i]
                isFound = True
            i = i + 1
        if not isFound:
            first_row = []

    return first_row


def find_baris_all(table, column, keyword):
    # function find_baris_all(table : array of array of string,
    #                        column : string, keyword : string) -> array of array of string
    # Mengeluarkan semua baris yang memiliki nilai <keyword> pada kolom <column> dalam tabel <table>

    # KAMUS LOKAL
    # i, colidx : integer
    # all_rows : array of array of string

    # ALGORITMA
    colidx = find_column_idx(table, column)

    all_rows = []

    for i in range(length(table)):
        if (table[i][colidx] == keyword):
            all_rows = konsdot(all_rows, table[i])
    if all_rows == []:
        all_rows = [[]]

    return all_rows

def contains(array, element):
    # FUNCTION contains (arr_str : list, element : string) -> boolean
    # Mengecek apabila string 'element' berada pada array of string 'arr_str;

    # KAMUS LOKAL
    #

    # ALGORTIMA UTAMA

    if element in array:
        return True
    else:
        return False

def validate_date(date):
    # FUNCTION validate_date (date : string) -> boolean
    # Mengecek apabila string 'date' sesuai dengan format tanggal (DD/MM/YYYY)
    # dan sesuai kalender (apakah hari sesuai per bulan)

    # KAMUS LOKAL
    # day, month, year : integer

    # ALGORTIMA UTAMA

    # Pengecekan apabila 'date' sesuai kalender dan format tanggal (DD/MM/YYYY)
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

# Fungsi-fungsi pembantu

import re

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

def length(array):
    # function length (array : array of string) -> integer
    # Mencari panjang suatu array
    # KAMUS LOKAL
    # i, count : integer
    # ALGORITMA
    count = 0
    for i in array:
        count = count + 1
    return count

def konsDot(array, element):
    # function konsDot (array : array of array of string, element : array of string) -> array of array of string
    # Menambah 1 elemen ke dalam array
    # KAMUS LOKAL
    # a : array of array of string
    # a_length, i : integer
    # ALGORITMA
    a_length = (length(array)) + 1
    a = [[] for i in range (a_length)]
    for i in range (length(array)):
        a[i] = array[i]
    a[a_length - 1] = element
    return a

def find_idx(table, colname):
    # function find_idx (colname : string) -> integer
    # Mencari nomor indeks suatu kolom bernama colname pada array array
    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    for i in range (length(table[0])):
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
    if (startidx >= (length(table))):
        datafound = []
        return datafound
    else: # (startidx < length(table))
        colidx = find_idx(table, colname)
        isFound = False
        i = startidx
        while ((i < (length(table))) and (isFound == False)):
            if (table[i][colidx] == keyword):
                datafound = table[i]
                isFound = True
            i = i + 1
        if (isFound == False):
            datafound = []
        return datafound

def find_baris_all(table, colname, keyword):
    # function find_baris_all (array : array of array of string, colname : string, keyword : string) -> array of array of string
    # Mencari baris yang tersimpan dalam table
    # KAMUS LOKAL
    # i, colidx : integer
    # datafound : array of array of string
    # ALGORITMA
    colidx = find_idx(table, colname)
    datafound = []
    for i in range (length(table)):
        if (table[i][colidx] == keyword):
            datafound = konsDot(datafound, table[i])
    if ((length(datafound)) == 0):
        datafound = [[]]
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
    for i in range (length(table[0])):
        if (table[0][i] == colname):
            colidx = int(i)
            isFound = True
    if (isFound == True):
        kolom = ["*" for i in range (length(table))]
        for i in range (length(table)):
            kolom[i] = table[i][colidx]
        return kolom
    else: # (isFound == False)
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
    while ((i < (length(array))) and (isFound == False)):
        if (array[i] == keyword):
            cellfound = array[i]
            isFound = True
        i = i + 1
    if (isFound == True):
        return cellfound
    else: # (isFound == False)
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
# Fungsi-fungsi pembantu

#     FAIRLY STRAIGHTFORWARD
# Fungsi/prosedur di bawah ini merupakan fungsi yang mudah untuk dipahami dan dipakai.

def validate_date(date):
    # FUNCTION validate_date (date : string) -> boolean
    # Mengecek apabila string 'date' sesuai dengan format tanggal (DD/MM/YYYY)
    # dan sesuai kalender (apakah hari sesuai per bulan)

    # KAMUS LOKAL
    # day, month, year : integer

    # ALGORTIMA UTAMA

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
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # isValid = flib.validate_date(1/1/2000)
    # print(isValid)
    # >> True
    # isValid = flib.validate_date(1-1-2000)
    # print(isValid)
    # >> False

def input_date(input_msg=""):
    # PROCEDURE input_date (output date : string)
    # Prosedur untuk pemasukan tanggal, akan diulang sampai tanggal valid.

    # KAMUS LOKAL
    # date : string

    # ALGORITMA UTAMA
    date = ""
    while True:
        date = input(input_msg)
        if validate_date(date):
            break
        print("Tanggal salah format (Format: DD/MM/YYYY) atau tidak sesuai kalender!")
    return date

def years_since_then(date1, date2):
    # function years_since_then(date1 : string, date2 : string) -> integer
    # Mengeluarkan tahun yang telah berlalu sejak date1 ke date2.
    # Tahun yang dikeluarkan dibulatkan ke bawah (16.5 -> 16).
    # date1 dan date2 memiliki format "DD/MM/YY" yang sudah lolos validate_date().

    # KAMUS LOKAL
    # days1, months1, years1 : int
    # days2, months2, years2 : int
    # result_years : int

    # ALGORITMA
    # Memecahkan format menjadi integer yang diperlukan (hari, bulan, tahun)
    (days1, months1, years1) = tuple(map(int, date1.split('/')))
    (days2, months2, years2) = tuple(map(int, date2.split('/')))
    result_years = years2 - years1

    # 14 Juli 2001 - 13 Juli 2020 => Masih terhitung 18 tahun, walaupun sebenarnya 18.95 tahun.
    if (months1 > months2) or (months1 <= months2 and days1 > days2):
        result_years -= 1

    return result_years


#     PEMROSESAN ARRAY, AND ARRAY OF ARRAY
# Fungsi/prosedur di bawah digunakan untuk mengakses, memroses, dan mengubah array.

def contains(array, element):
    # FUNCTION contains (arr_str : array, element : string) -> boolean
    # Mengecek apabila string 'element' berada pada array of string 'arr_str;

    # KAMUS LOKAL

    # ALGORTIMA UTAMA

    if element in array:
        return True
    else:
        return False

def length(array):
    # function length (array : array) -> integer
    # Mencari panjang suatu array.
    # KAMUS LOKAL
    # i, count : integer
    # ALGORITMA
    count = 0
    for i in array:
        count = count + 1
    return count
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [1, 2, 3]
    # l = flib.length(A)
    # print(l)
    # >> 3

def find_baris_idx(table, row):
    # function find_baris_idx (table : array of array of string, row : array of string) -> integer
    # Mencari nomor indeks suatu baris pada table.
    # Syarat: row sudah pasti ada di table.

    # KAMUS LOKAL
    # i : integer

    # ALGORITMA
    for i in range(length(table)):
        if (table[i] == row):
            return int(i)

def konsDot(array, element):
    # function konsDot (array : array of array of string, element : array of string) -> array of array of string
    # Menambah 1 elemen ke dalam array
    # KAMUS LOKAL
    # a : array of array of string
    # a_length, i : integer
    # ALGORITMA
    a_length = length(array) + 1
    a = [[] for i in range (a_length)]
    for i in range (length(array)):
        a[i] = array[i]
    a[a_length - 1] = element
    return a
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [["ITB", "UNPAD"], ["UI"]]
    # B = ["ITS", "UNAIR"]
    # C = flib.konsDot(A, B)
    # print(C)
    # >> [["ITB", "UNPAD"], ["UI"], ["ITS", "UNAIR"]]

def merge(array1, array2):
    # function merge (array1 : array of array of string, array2 : array of array of string) -> array of array of string
    # Melakukan merge antara dua array of array of string.
    # KAMUS LOKAL
    # merged : array of array of string
    # merged_length, i : integer
    merged_length = length(array1) + length(array2)
    merged = [[] for i in range (merged_length)]
    merged[0:length(array1)] = array1
    merged[length(array1):] = array2

    return merged
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [["ITB", "UNPAD"], ["UI"]]
    # B = [["ITS", "UNAIR"], ["UNJ"]]
    # C = flib.merge(A, B)
    # print(C)
    # >> [["ITB", "UNPAD"], ["UI"], ["ITS", "UNAIR"], ["UNJ"]]

def find_idx(table, colname):
    # function find_idx (table : array of array of string, colname : string) -> integer
    # Mencari nomor indeks suatu kolom bernama colname pada array array
    # KAMUS LOKAL
    # i : integer
    # ALGORITMA
    for i in range (length(table[0])):
        if (str(table[0][i]) == str(colname)):
            return int(i)
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [["Nama", "Saldo"], ["Willy Wangky", "0"]]
    # i = flib.find_idx(A, "Saldo")
    # print(i)
    # >> 1

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
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [["Nama", "Saldo"], ["Willy Wangky", "0"], ["Willy Wangky", "1000"]]
    # F = flib.find_baris_first(A, "Nama", "Willy Wangky")
    # print(F)
    # >> ["Willy Wangky", "0"]
    # G = flib.find_baris_first(A, "Nama", "Willy Wangky", 1)
    # print(G)
    # >> ["Willy Wangky", "1000"]
    # Z = # F = flib.find_baris_first(A, "Nama", "Wangky Willy")
    # print(Z)
    # >> []

def find_baris_all(table, colname, keyword):
    # function find_baris_all (array : array of array of string, colname : string, keyword : string) -> array of array of string
    # Mencari semua baris dengan keyword tertentu yang tersimpan pada table
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
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [["Nama", "Saldo"], ["Willy Wangky", "0"], ["Willy Wangky", "1000"]]
    # F = flib.find_baris_first(A, "Nama", "Willy Wangky")
    # print(F)
    # >> [["Willy Wangky", "0"], ["Willy Wangky", "1000"]]
    # Z = flib.find_baris_first(A, "Nama", "Wangky Willy")
    # print(Z)
    # [[]]

def find_kolom(table, colname):
    # function find_kolom (table : array of array of string, colname : string) -> array of string
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
        kolom = ["*" for i in range (1, length(table))]
        for i in range (1, length(table)):
            kolom[i] = table[i][colidx]
        return kolom
    else: # (isFound == False)
        return []
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [["Nama", "Saldo"], ["Willy Wangky", "0"], ["Willy Wangky", "1000"]]
    # B = flib.find_kolom(A, "Saldo")
    # print(B)
    # >> ["0", "1000"]
    # Z = flib.find_kolom(A, "Tanggal_Lahir")
    # print(Z)
    # >> []

def validate_cell(array, keyword):
    # function validate_cell (array : array of string, keyword : string) -> boolean
    # Validasi keberadaan suatu cell yang tersimpan dalam suatu array 1 dimensi
    # KAMUS LOKAL
    # i : integer
    # isFound : boolean
    # ALGORITMA
    i = 0
    isFound = False
    while ((i < (length(array))) and (isFound == False)):
        if (array[i] == keyword):
            isFound = True
        i = i + 1
    return isFound
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # AA = ["Willy Wangky", "0"]
    # isValid = flib.validate_cell(AA, "0")
    # print(isValid)
    # >> True
    # isValid = flib.validate_cell(AA, "Admin")
    # print(isValid)
    # >> False

def search(table, result_column, from_column, from_data):
    # function search(table : array of array of string, result_column : string, from_column : string, from_data : string) -> string
    # SYARAT: result_column, from_column, from_data valid; from_data unik (hanya ada 1 dalam kolom tersebut)
    # KAMUS LOKAL
    # data : array of string
    # idx : integer
    # ALGORITMA
    data = find_baris_first(table, from_column, from_data)
    idx = find_idx(table, result_column)
    return data[idx]
    # APLIKASI
    # (pada modul lain)
    # import auxilliary as flib
    # A = [["Nama", "Saldo"], ["Willy Wangky", "0"], ["Willy Wangky", "1000"]]
    # B = flib.search(A, "Saldo", "Nama", "Willy Wangky")
    # print(B)
    # >> "0"

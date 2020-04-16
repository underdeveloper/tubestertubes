#Program F11
#Menampilkan kritik dan saran yang dimasukkan pemain, diurutkan berdasarkan ID Wahana secara alfabetis

#KAMUS

#ALGORITMA PROGAM UTAMA
import F01 as load
import auxilliary as aux

#REALISASI FUNGSI/PROSEDUR

def print_sorted(kritiksaran):
    # function print_sorted (kritiksaran : Rekaman) -> array of array of string
    # Mengeluarkan data kritiksaran yang sudah diurut berdasarkan sorting_key
    # KAMUS LOKAL
    # sorting_key : string
    # sorting_idx, i, j, minpos : int
    # temp : array of string

    sorting_key = "ID_Wahana"
    sorting_idx = aux.find_idx(kritiksaran.data, sorting_key) # Mencari indeks kolom <sorting_key>
    
    for i in range(1, aux.length(kritiksaran.data)):
        minpos = i
        for j in range(i, aux.length(kritiksaran.data)):
            if int(kritiksaran.data[j][sorting_idx]) < int(kritiksaran.data[minpos][sorting_idx]):
                minpos = j
        temp = kritiksaran.data[i]
        kritiksaran.data[i] = kritiksaran.data[minpos]
        kritiksaran.data[minpos] = temp
        
    print(kritiksaran.data)
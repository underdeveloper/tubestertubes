# PROGRAM F06

# Mencari wahana sesuai kriteria tinggi badan dan batasan umur

# Kriteria batasan umur (anak-anak/dewasa/semua umur)
# Kriteria tinggi badan (>170/tanpa batasan)


# ALGORITMA

# REALISASI FUNGSI/PROSEDUR

import auxilliary as aux
import F01 as load

def isBatasUmurTrue (umur) :
    # Menentukan apakah batas umur yang dimasukkan benar atau tidak

    if umur == 1 or umur == 2 or umur == 3 :
        return True
    else : #pilihan umur != 1 / 2 / 3
        return False
            
def isBatasTinggiTrue (tinggi) :
    # Menentukan apakah batas tinggi yang dimasukkan benar atau tidak

    if tinggi == 1 or tinggi == 2 :
        return True
    else : #pilihan umur != 1 / 2
        return False    

def main ():
    #Program utama F06
    wahana = load.use ("wahana.csv")

    print ("Jenis batasan umur: ")
    print ("1. Anak-anak (<17 tahun)")
    print ("2. Dewasa (>=17 tahun)")
    print ("3. Semua umur")
    print (" ")
    print ("Jenis batasan tinggi badan: ")
    print ("1. Lebih dari 170 cm")
    print ("2. Tanpa batasan")
    print (" ")
    while True:
        umur = int(input("Batasan umur pemain: "))
        if isBatasUmurTrue(umur):  # 1, 2, 3
            break
        else:  # selain 1, 2, 3
            print("Batasan umur tidak valid!")
            return

    while True:
        tinggi = int(input("Batasan tinggi pemain: "))
        if isBatasTinggiTrue(tinggi):  # 1, 2
            break
        else:  # selain 1, 2
            print("Batasan tinggi tidak valid!")
            return
        # data_wahana = load.use(wahanafile)
    
    if umur == 1 :
        if tinggi == 1:
            u = "anak-anak"
            t = ">170"
        elif tinggi == 2:
            u = "anak-anak"
            t = "tanpa batasan"
    elif umur == 2:
        if tinggi == 1:
            u = "dewasa"
            t = ">170"
        elif tinggi == 2:
            u = "dewasa"
            t = "tanpa batasan"
    elif umur == 3:
        if tinggi == 1:
            u = "semua umur"
            t = ">170"
        elif tinggi == 2:
            u = "semua umur"
            t = "tanpa batasan"
            
    umur_true = aux.merge([wahana.data[0]], aux.find_baris_all(wahana.data, "Batasan_Umur", u))

    if umur_true[1:] == []:
        print("Tidak ada wahana sesuai batasan yang dimasukkan.")
        return
    
    validasi = aux.find_baris_all(umur_true, "Batasan_Tinggi", t)

    if validasi == [[]]:
        print("Tidak ada wahana sesuai batasan yang dimasukkan.")
        return

    print("Hasil pencarian: ")
    for i in range(aux.length(validasi)):
        id_wahana = validasi[i][aux.find_idx(wahana.data, "ID_Wahana")]
        nama_wahana = validasi[i][aux.find_idx(wahana.data, "Nama_Wahana")]
        harga_tiket = validasi[i][aux.find_idx(wahana.data, "Harga_Tiket")]
        print (id_wahana, "|", nama_wahana, "|", harga_tiket)
    
    return

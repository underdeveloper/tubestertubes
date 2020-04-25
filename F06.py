# PROGRAM F06
# Desainer : Stefanny
# Coder : Stefanny, Sulthan
# Tester : Stefanny, Sulthan, Baskoro, Feral

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

    print("Hasil pencarian: ", end="\n")
    i = 0
    j = 0
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
            
    umur_true = aux.find_baris_all(wahana.data, "Batasan_Umur", u)
    validasi = aux.find_baris_all(umur_true, "Batasan_Tinggi", t)

    arr1 = [0 for i in range(len(validasi))]
    id_wahana = [0 for j in range(len(validasi))]
    nama_wahana = [0 for j in range(len(validasi))]
    harga_tiket = [0 for j in range(len(validasi))]

    for i in range(len(validasi)):
        arr1[i] = validasi[i]
        # print (D[i])
    for j in range(len(arr1[i])):
        # Z = arr1[j]
        # arr2 = Z[1]
        id_wahana = arr1[j][0]
        nama_wahana = arr1[j][1]
        harga_tiket =  arr1[j][2]

    if validasi == [] :
        print ("Tidak ada wahana yang sesuai dengan pencarian kamu.")
    else :
        #bila terdapat data dengan umur dan tinggi yang sesuai
        print (id_wahana, "|", nama_wahana, "|", harga_tiket )
    
    return
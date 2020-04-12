# PROGRAM F06
# Mencari wahana sesuai kriteria tinggi badan dan batasan umur

# Kriteria batasan umur (anak-anak/dewasa/semua umur)
# Kriteria tinggi badan (>170/tanpa batasan)

# KAMUS

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

def main (userfile):
    #Program utama F06

    print ("Jenis batasan umur: ")
    print ("1. Anak-anak (<17 tahun)")
    print ("2. Dewasa (>=17 tahun)")
    print ("3. Semua umur")
    print (" ")
    print ("Jenis batasan tinggi badan: ")
    print ("1. Lebih dari 170 cm")
    print ("2. Tanpa batasan")
    print (" ")
    umur = int(input("Batasan umur pemain: "))
    if isBatasUmurTrue(umur) == True :
        umur = umur
    else : #bila batas umur != 1 / 2 / 3 
        print("Batasan umur tidak valid!")
        while True:
            umur = int(input("Batasan umur pemain: "))
            if umur == 1:
                return False
            elif umur == 2:
                return False
            elif umur == 3:
                return False
            else: #bila batasan umur != 1 / 2 / 3
                print("Batasan umur tidak valid!")
                return True
    tinggi = int(input ("Batasan tinggi badan: "))
    if isBatasTinggiTrue(tinggi) :
        pass
    else:
        print("Batasan tinggi badan tidak valid!")
        while True:
            tinggi = int(input("Batasan tinggi badan: "))
            if tinggi == 1:
                return False
            elif tinggi == 2:
                return False
            elif tinggi == 3:
                return False
            else:
                print("Batasan tinggi badan tidak valid!")
                return True
                
    print ("Hasil pencarian: ")
    if umur == 1:
        if tinggi == 1:
            idxumur1 = aux.find_idx(userfile, "Batasan_Umur")
            idxtinggi1 = aux.find_idx(userfile, "Batasan_Tinggi")
            print ([ut11.loc["ID_Wahana"]], " | ", [ut11.loc["Nama_Wahana"]], " | ", [ut11.loc["Harga_Tiket"]])
        elif tinggi == 2:
            ut12 = df.loc[df["Batasan_Umur"]<17] & [df["Batasan Tinggi"]== "Tanpa Batasan"]
            print([ut12.loc["ID_Wahana"]], " | ", [ut12.loc["Nama_Wahana"]], " | ", [ut12.loc["Harga_Tiket"]])
    elif umur == 2:
        if tinggi == 1:
            ut21 = df.loc[df["Batasan_Umur"]>=17] & [df["Batasan_Tinggi"]>170]
            print([ut21.loc["ID_Wahana"]], " | ", [ut21.loc["Nama_Wahana"]], " | ", [ut21.loc["Harga_Tiket"]])
        elif tinggi == 2:
            ut22 = df.loc[df["Batasan_Umur"]>=17] & [df["Batasan_Tinggi"] == "Tanpa Batasan"]
            print([ut22.loc["ID_Wahana"]], " | ", [ut22.loc["Nama_Wahana"]], " | ", [ut22.loc["Harga_Tiket"]])
    elif umur == 3:
        ut31 = df.loc[df["Batasan_Umur"] == "Semua Umur"] & [df["Batasan_Tinggi"] > 170]
        if tinggi == 1:
            print ([ut31.loc["ID_Wahana"]], " | ", [ut31.loc["Nama_Wahana"]], " | ", [ut31.loc["Harga_Tiket"]])
        elif tinggi == 2:
            ut32 =df.loc[df["Batasan_Umur"] == "Semua Umur"] & [df["Batasan_Tinggi"] == "Tanpa Batasan"]
            print([ut32.loc["ID_Wahana"]], " | ", [ut32.loc["Nama_Wahana"]], " | ", [ut32.loc["Harga_Tiket"]])

# ON PROGRESS

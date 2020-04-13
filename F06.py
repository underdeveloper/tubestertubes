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

def main (wahanafile):
    # Program utama F06

    print ("Jenis batasan umur: ")
    print ("1. Anak-anak (<17 tahun)")
    print ("2. Dewasa (>=17 tahun)")
    print ("3. Semua umur")
    print (" ")
    print ("Jenis batasan tinggi badan: ")
    print ("1. Lebih dari 170 cm")
    print ("2. Tanpa batasan")
    print (" ")

    # Loop ini agak salah jadi gua ganti

    # umur = int(input("Batasan umur pemain: "))
    # if isBatasUmurTrue(umur) == True :
    #     umur = umur
    # else : #bila batas umur != 1 / 2 / 3 
    #     print("Batasan umur tidak valid!")
    #     while True:
    #         umur = int(input("Batasan umur pemain: "))
    #         if umur == 1:
    #             return False
    #         elif umur == 2:
    #             return False
    #         elif umur == 3:
    #             return False
    #         else: #bila batasan umur != 1 / 2 / 3
    #             print("Batasan umur tidak valid!")
    #             return True
    # 
    # tinggi = int(input("Batasan tinggi badan: "))
    # if isBatasTinggiTrue(tinggi):
    #     pass
    # else:
    #     print("Batasan tinggi badan tidak valid!")
    #     while True:
    #         tinggi = int(input("Batasan tinggi badan: "))
    #         if tinggi == 1:
    #             return False
    #         elif tinggi == 2:
    #             return False
    #         elif tinggi == 3:
    #             return False
    #         else:
    #             print("Batasan tinggi badan tidak valid!")
    #             return True

    while True:
        umur = int(input("Batasan umur pemain: "))
        if isBatasUmurTrue(umur): # 1, 2, 3
            break
        else: # selain 1, 2, 3
            print("Batasan umur tidak valid!")

    while True:
        tinggi = int(input("Batasan tinggi pemain: "))
        if isBatasTinggiTrue(tinggi):  # 1, 2
            break
        else:  # selain 1, 2
            print("Batasan tinggi tidak valid!")

    # data_wahana = load.use(wahanafile)
                
    print ("Hasil pencarian: ",end="\n")


# ON PROGRESS

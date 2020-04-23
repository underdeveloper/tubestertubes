#PROGRAM F15
#Menampilkan tiket yang dimiliki suatu user

#KAMUS

#ALGORITMA PROGRAM UTAMA
import auxilliary as aux

#REALISASI FUNGSI/PROSEDUR:
def check(tiket,wahana) :
    # PROCEDURE check (input tiket : array of array [0..2] of string, input wahana : array of array [0..4] of string)
    # I.S tiket dan wahana sudah terdefinisi
    # F.S ditampilkan ID Wahana, Nama Wahana, dan jumlah tiket suatu user (user yang dicari inputan dari admin)
    # KAMUS LOKAL
    # isUserValid = boolean
    # i, j = integer
    # name = string

    isUserValid = False
    while isUserValid == False :
        name = str(input("Masukkan username :"))
        finduser = aux.find_baris_all(tiket.data,"Username",name)
        if finduser != [] :
            print("Riwayat :")
            for i in range(aux.length(finduser)):
                    detect_ID = finduser[i][aux.find_idx(tiket.data,"ID_Wahana")]
                    print(detect_ID," | ",end='')
                    findwahana = aux.find_baris_first(wahana.data,"ID_Wahana",detect_ID)
                    print(findwahana[aux.find_idx(wahana.data,"Nama_Wahana")],' | ',end='')
                    print(finduser[i][aux.find_idx(tiket.data,"Jumlah_Tiket")],' ', end='')   
                    print()
            isUserValid = True
        else :
            print("User tidak ditemukan / user tidak memiliki tiket")
    return
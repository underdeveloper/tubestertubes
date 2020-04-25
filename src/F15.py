#PROGRAM F15
#Menampilkan tiket yang dimiliki suatu user

#ALGORITMA PROGRAM UTAMA
import auxilliary as aux
import F01 as load

#REALISASI FUNGSI/PROSEDUR:
def main () :
    # PROCEDURE main ()
    # I.S tiket dan wahana sudah terdefinisi
    # F.S ditampilkan ID Wahana, Nama Wahana, dan jumlah tiket suatu user (user yang dicari inputan dari admin)
    # KAMUS LOKAL
    # isUserValid = boolean
    # i, j = integer
    # name = string
    wahana = load.use("wahana.csv")
    tiket = load.use("tiket.csv")

    isUserValid = False
    while isUserValid == False :
        name = str(input("Masukkan username: "))
        finduser = aux.find_baris_all(tiket.data,"Username",name)
        if finduser != [] :
            print("Kepemilikan tiket pemain: ")
            for i in range(aux.length(finduser)):
                    detect_ID = finduser[i][aux.find_idx(tiket.data,"ID_Wahana")]
                    print(str(detect_ID) + " | ",end='')
                    findwahana = aux.find_baris_first(wahana.data,"ID_Wahana",detect_ID)
                    print(str(findwahana[aux.find_idx(wahana.data,"Nama_Wahana")]) + ' | ',end='')
                    print(str(finduser[i][aux.find_idx(tiket.data,"Jumlah_Tiket")]))
            isUserValid = True
        else :
            print("User " + name + " tidak ditemukan, atau tidak memiliki tiket.")

    return
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
    # userfile, wahana, tiket = Rekaman
    # name = string
    # finduser, user_in_db = Rekaman.data
    # i = integer
    # name = string
    userfile = load.use("user.csv")
    wahana = load.use("wahana.csv")
    tiket = load.use("tiket.csv")

    name = str(input("Masukkan username: "))

    finduser = aux.find_baris_all(tiket.data, "Username", name)
    user_in_db = aux.find_baris_first(userfile.data, "Username", name)    

    if user_in_db == []:
        print("Tidak ditemukan pengguna dengan username \"" + name + "\".")
    elif finduser == [[]]:
        print(name + " tidak memiliki tiket satupun.")
    else:
        print("Kepemilikan tiket pemain: ")
        for i in range(aux.length(finduser)):
            detect_ID = finduser[i][aux.find_idx(tiket.data,"ID_Wahana")]
            print(str(detect_ID) + " | ",end='')
            findwahana = aux.find_baris_first(wahana.data,"ID_Wahana",detect_ID)
            print(str(findwahana[aux.find_idx(wahana.data,"Nama_Wahana")]) + ' | ',end='')
            print(str(finduser[i][aux.find_idx(tiket.data,"Jumlah_Tiket")]))

    return

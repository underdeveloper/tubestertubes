# PROGRAM F14
# Melihat riwayat penggunaan wahana dilakukan oleh admin
# Desainer : Stefanny
# Coder : Stefanny


# ALGORITMA

import auxilliary as aux
import F01 as load

# REALISASI FUNGSI/PROSEDUR


def main(userfile):
    # Program utama F14
    # Admin memasukkan ID Wahana
    wahana = load.use ("wahana.csv")
    user = load.use ("penggunaan.csv")

    id_wahana = str(input("Masukkan ID Wahana: "))
    id_wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)

    while id_wahana_found == [] :
        id_wahana = input("Tidak ditemukan wahana dengan ID \"" + id_wahana + '\". Mohon diulang: ')
        id_wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)

    print("Riwayat: ")
    print (" ")
    if id_wahana_found != [] :
        search = aux.find_baris_all(user.data, "ID_Wahana", id_wahana)
        tanggal = aux.find_kolom(search, "Tanggal_Penggunaan")
        username = aux.find_kolom(search, "Username")
        jmltiket = aux.find_kolom(search, "Jumlah_Tiket")
        print (tanggal, "| ", username, "| ", jmltiket)



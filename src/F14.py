# PROGRAM F14
# Melihat riwayat penggunaan wahana dilakukan oleh admin

# ALGORITMA

import auxilliary as aux
import F01 as load

# REALISASI FUNGSI/PROSEDUR

def main():
    # Program utama F14
    # Admin memasukkan ID Wahana dan dikeluarkan riwayat penggunaan wahana tersebut.
    wahana = load.use ("wahana.csv")
    penggunaan = load.use ("penggunaan.csv")

    id_wahana = str(input("Masukkan ID Wahana: "))
    wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)

    while wahana_found == [] :
        id_wahana = input("Tidak ditemukan wahana dengan ID \"" + id_wahana + '\". Mohon diulang: ')
        wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)

    riwayat = []

    for i in range(1, aux.length(penggunaan.data)):
        if str(penggunaan.data[i][aux.find_idx(penggunaan.data, "ID_Wahana")]) == id_wahana:
            tanggal_guna = penggunaan.data[i][aux.find_idx(penggunaan.data, "Tanggal_Penggunaan")]
            username = penggunaan.data[i][aux.find_idx(penggunaan.data, "Username")]
            tiket = penggunaan.data[i][aux.find_idx(penggunaan.data, "Jumlah_Tiket")]
            riwayat_baru = (tanggal_guna, username, tiket)
            riwayat = aux.konsDot(riwayat, riwayat_baru)

    print("Riwayat penggunaan " + str(wahana_found[aux.find_idx(wahana.data, "Nama_Wahana")]) + ": ")
    for i in range(aux.length(riwayat)):
        print(str(riwayat[i][0]) + " | " + str(riwayat[i][1]) + " | " + str(riwayat[i][2]))

    return

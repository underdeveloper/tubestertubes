# PROGRAM F14
# Melihat riwayat penggunaan wahana dilakukan oleh admin
# Desainer : Stefanny
# Coder : Stefanny


# ALGORITMA

import auxilliary as aux
import F01 as load

# REALISASI FUNGSI/PROSEDUR


def main():
    # Program utama F14
    # Admin memasukkan ID Wahana
    user = load.use ("wahana.csv")

    id_wahana = str(input("Masukkan ID Wahana: "))
    id_wahana_found = aux.find_baris_all(user.data, "ID_Wahana", id_wahana)

    while id_wahana_found == [] :
        id_wahana = input("Tidak ditemukan wahana dengan ID \"" + id_wahana + '\". Mohon diulang: ')
        id_wahana_found = aux.find_baris_all(user.data, "ID_Wahana", id_wahana)

    print("Riwayat: ")
    print (" ")
    # if id_wahana_found != [] : <<tidak perlu, sudah divalidasi>>
    j = 0
    i = 0
    arr1 = [0 for i in range(len(id_wahana_found))]
    username = [0 for j in range(len(id_wahana_found))]
    tanggal_pakai = [0 for j in range(len(id_wahana_found))]
    jumlah_tiket = [0 for j in range(len(id_wahana_found))]

    for i in range(len(id_wahana_found)):
        arr1[i] = id_wahana_found[i]
    for j in range(len(arr1[i])):
        username = arr1[j][0]
        tanggal_pakai = arr1[j][1]
        jumlah_tiket =  arr1[j][3]
        print(tanggal_pakai, "|", username, "|", jumlah_tiket)

    return

# F08 - MENGGUNAKAN TIKET

import F01 as load
import auxilliary as aux

def main(pengguna):
    # PROCEDURE main (input pengguna : array [0..1] of array [0..6] of string,
    #                 output tiket : Rekaman, output penggunaan : Rekaman)
    # I.S. tiket dan penggunaan abstrak
    # F.S. Jika input lolos ujian, tiket dan penggunaan akan diupdate.
    # KAMUS LOKAL
    # wahana, tiket, penggunaan: Rekaman
    # username : string
    # height, balance : integer
    # id_wahana : string
    # wahana_found : array[0..4] of string
    # date_now : string
    # tickets, owned_tickets: integer
    # cancel_use : character
    # data_penggunaan : array [0..3] of string
    # new_penggunaan, previously_bought : Rekaman.data
    # ALGORITMA
    wahana = load.use("wahana.csv")
    tiket = load.use("tiket.csv")
    penggunaan = load.use("penggunaan.csv")

    username = str(pengguna[1][aux.find_idx(pengguna, "Username")])

    # Input dan validasi ID Wahana:
    id_wahana = input("Masukkan ID wahana: ")
    wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)
    if wahana_found == []:
        print("Tidak ditemukan wahana dengan ID \"" + id_wahana + '\".')
        return
    wahana_name = wahana_found[aux.find_idx(wahana.data, "Nama_Wahana")]

    # Input dan validasi tanggal hari ini
    date_now = aux.input_date("Masukkan tanggal hari ini: ")

    # Input dan validasi jumlah tiket yang ingin digunakan
    tickets = int(input("Jumlah tiket yang digunakan: "))
    while tickets <= 0:
        if tickets == 0:
            cancel_use = input("Batalkan menggunakan tiket? [Y/N] ")
            while cancel_use.upper() != 'Y' or cancel_use.upper() != 'N':
                cancel_use = input(
                    "Masukan salah. Batalkan menggunakan tiket? [Y/N] ")
            if cancel_use == 'Y':
                return
            else:  # cancel_use == 'N'
                tickets = int(input("Jumlah tiket yang digunakan: "))
        else:
            tickets = int(input("Jumlah tiket harusnya bukan negatif. Mohon diulang: "))
    
    # Mengecek apakah pengguna sudah membeli tiket pada wahana

    previously_bought = aux.merge([tiket.data[0]], aux.find_baris_all(tiket.data, "Username", username))
    
    ticket_id_wahana = aux.find_baris_first(previously_bought, "ID_Wahana", id_wahana)
    
    if ticket_id_wahana == []:
        # Jika pengguna belum pernah membeli tiket di id_wahana, pengguna tidak diperbolehkan memakai tiket.
        print("Anda belum pernah membeli tiket terkait.")
        print("Alasan: Belum membeli tiket pada wahana " + wahana_name + ".")
        return

    owned_tickets = int(ticket_id_wahana[aux.find_idx(tiket.data, "Jumlah_Tiket")])

    if int(owned_tickets) < tickets:
        # Jika pengguna meminta tiket lebih banyak daripada yang sebenarnya ia punya, pengguna tidak diperbolehkan memakai tiket.
        print("Anda belum pernah membeli tiket terkait.")
        print("Alasan: Anda hanya memiliki " + str(owned_tickets) + " tiket pada wahana " + wahana_name + ".")
    else:
        # Jika pengguna memiliki tiket yang cukup pada wahana, pengguna menggunakan tiket tersebut.
        
        # File penggunaan tiket diupdate, sesuai banyak tiket yang dipakai.
        data_penggunaan = [username, date_now, id_wahana, tickets]
        new_penggunaan = aux.konsDot(penggunaan.data, data_penggunaan)
        load.store("penggunaan.csv", new_penggunaan)

        # File kepemilikan tiket diupdate, banyak tiket yang dimiliki pengguna dikurangi banyak tiket yang dipakai.
        if owned_tickets == tickets:
            # Jika pengguna kehabisan tiket pada wahana tersebut, baris tersebut dihapus.
            row_to_be_changed = aux.find_baris_idx(tiket.data, ticket_id_wahana) # Baris tiket yang ingin dihapus
            new_tiket = aux.merge(tiket.data[:row_to_be_changed], tiket.data[row_to_be_changed+1:]) # Penghapusan baris
        else:
            # Baris kepemilikan tiket pengguna diganti dengan banyak tiket baru.
            row_to_be_changed = aux.find_baris_idx(tiket.data, ticket_id_wahana) # Baris tiket yang ingin diganti
            idx_col_jml_tiket = aux.find_idx(tiket.data, "Jumlah_Tiket")
            new_tiket = tiket.data
            new_tiket[row_to_be_changed][idx_col_jml_tiket] = str(int(owned_tickets) - int(tickets)) # Penggantian baris
        load.store("tiket.csv", new_tiket)

        print("Terima kasih telah bermain.")
        print("Selamat bersenang-senang di " + wahana_name + "!")

        return

# B04 - Laporan Kehilangan Tiket
# Module B04 merupakan file berisi fungsi untuk melaporkan kehilangan tiket. 

import F01 as load
import auxilliary as aux

def main(pengguna):
    # PROCEDURE main (input pengguna)
    # I.S. kehilangan dan tiket abstrak
    # F.S. Jika input lolos ujian, tiket dan kehilangan akan diupdate.
    # KAMUS LOKAL

    # ALGORITMA
    user = load.use("user.csv")
    wahana = load.use("wahana.csv")
    kehilangan = load.use("hilang.csv")
    tiket = load.use("tiket.csv")

    username_typing = str(pengguna[1][aux.find_idx(pengguna, "Username")])
    are_they_an_admin = (str(pengguna[1][aux.find_idx(pengguna, "Role")]) == "Admin") # Mengecek apakah pengguna admin
    
    # Input dan validasi username
    username_lost_tickets = str(input("Masukkan username: "))
    if (not are_they_an_admin) and (username_lost_tickets != username_typing):
        # Jika pengguna bukan admin dan mencoba melaporkan kehilangan tiket untuk pengguna lain, tidak diperbolehkan.
        print("Jika Anda bukan admin, Anda tidak bisa melaporkan kehilangan tiket untuk pengguna lain.")
        username_lost_tickets = str(input("Masukkan username Anda: "))
        while username_lost_tickets != username_typing:
            print("Jika Anda bukan admin, Anda tidak bisa melaporkan kehilangan tiket untuk pengguna lain.")
            username_lost_tickets = str(input("Masukkan username *Anda*: "))
    else:
        # Admin boleh melaporkan kehilangan tiket untuk pengguna lain.
        user_found = aux.find_baris_first(user.data, "Username", username_lost_tickets)
        while user_found == []:
            username_lost_tickets = input("Tidak ditemukan user dengan username \"" + username_lost_tickets + '\". Mohon diulang: ')
            user_found = aux.find_baris_first(user.data, "Username", username_lost_tickets)
    
    # Input dan validasi tanggal hari ini
    date_now = aux.input_date("Masukkan tanggal hari ini: ")

    # Input dan validasi ID Wahana
    id_wahana = input("Masukkan ID wahana: ")
    wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)
    while wahana_found == []:
        id_wahana = input("Tidak ditemukan wahana dengan ID \"" + id_wahana + '\". Mohon diulang: ')
        wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)
    wahana_name = wahana_found[aux.find_idx(wahana.data, "Nama_Wahana")]

    # Input dan validasi jumlah tiket yang hilang
    tickets = int(input("Jumlah tiket yang dihilangkan: "))
    while tickets <= 0:
        if tickets == 0:
            cancel_buy = input("Batalkan melapor kehilangan? [Y/N] ")
            while cancel_buy.upper() != 'Y' or cancel_buy.upper() != 'N':
                cancel_buy = input(
                    "Masukan salah. Batalkan melapor kehilangan? [Y/N] ")
            if cancel_buy == 'Y':
                return
            else:  # cancel_buy == 'N'
                tickets = int(input("Jumlah tiket yang dihilangkan: "))
        else:
            tickets = int(input("Jumlah tiket harusnya bukan negatif. Mohon diulang: "))

    # Mengecek apakah pengguna sudah pernah membeli tiket di wahana yang dimasukkan
    previously_bought = aux.merge([tiket.data[0]], aux.find_baris_all(tiket.data, "Username", username_lost_tickets))

    ticket_id_wahana = aux.find_baris_first(previously_bought, "ID_Wahana", id_wahana)

    if ticket_id_wahana == []:
        # Jika pengguna belum pernah membeli tiket di id_wahana, pengguna tidak diperbolehkan memakai tiket.
        print("Tiket Anda tidak valid dalam sistem kami.")
        print("Alasan: Belum membeli tiket pada wahana " + wahana_name + ".\n")
        return

    owned_tickets = str(ticket_id_wahana[aux.find_idx(tiket.data, "Jumlah_Tiket")])

    if int(owned_tickets) < tickets:
        # Jika pengguna meminta tiket lebih banyak daripada yang sebenarnya ia punya, pengguna tidak bisa melaporkan kehilangan tiket.
        print("Tiket Anda tidak valid dalam sistem kami.")
        print("Alasan: Anda hanya memiliki " + owned_tickets + " tiket pada wahana " + wahana_name + ".\n")

    else:
        # Jika pengguna memiliki tiket yang cukup pada wahana, laporan kehilangan berlanjut.

        # File kehilangan tiket diupdate, sesuai banyak tiket yang dipakai.
        data_lost = [username_lost_tickets, date_now, id_wahana, tickets]
        new_lost = aux.konsDot(kehilangan.data, data_lost)
        load.store("hilang.csv", new_lost)

        # File kehilangan tiket diupdate, banyak tiket yang dimiliki pengguna dikurangi banyak tiket yang hilang.
        if int(owned_tickets) == tickets:
            # Jika pengguna kehabisan tiket pada wahana tersebut, baris tersebut dihapus.
            row_to_be_changed = aux.find_baris_idx(tiket.data, ticket_id_wahana)  # Baris tiket yang ingin dihapus
            new_tiket = aux.merge(tiket.data[:row_to_be_changed], tiket.data[row_to_be_changed+1:])  # Penghapusan baris
        else:
            # Baris kepemilikan tiket pengguna diganti dengan banyak tiket baru.
            row_to_be_changed = aux.find_baris_idx(tiket.data, ticket_id_wahana)  # Baris tiket yang ingin diganti
            idx_col_jml_tiket = aux.find_idx(tiket.data, "Jumlah_Tiket")
            new_tiket = tiket.data
            new_tiket[row_to_be_changed][idx_col_jml_tiket] = str(int(owned_tickets) - int(tickets))  # Penggantian baris
        load.store("tiket.csv", new_tiket)

        print("Laporan kehilangan tiket Anda telah direkam.\n\n")
    
    return
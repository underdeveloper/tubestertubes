# F09 - REFUND TIKET
# Desainer: Sulthan
# Coder: Sulthan
# Tester: Sulthan

import F01 as load
import auxilliary as aux

def main(pengguna):
    # PROCEDURE main (input/output pengguna)
    # I.S. tiket dan refund abstrak
    # F.S. Jika input lolos ujian, tiken dan refund akan diupdate.
    # KAMUS LOKAL

    # ALGORITMA
    wahana = load.use("wahana.csv")
    tiket = load.use("tiket.csv")
    refund = load.use("refund.csv")

    username = str(pengguna[1][aux.find_idx(pengguna, "Username")])
    balance = int(pengguna[1][aux.find_idx(pengguna, "Saldo")])

    # Input dan validasi ID Wahana:
    id_wahana = input("Masukkan ID wahana: ")
    wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)
    while wahana_found == []:
        id_wahana = input("Tidak ditemukan wahana dengan ID \"" + id_wahana + '\". Mohon diulang: ')
        wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)
    wahana_name = wahana_found[aux.find_idx(wahana.data, "Nama_Wahana")]

    # Input dan validasi tanggal hari ini
    date_now = aux.input_date("Masukkan tanggal hari ini: ")

    # Input dan validasi jumlah tiket yang ingin digunakan
    tickets = int(input("Jumlah tiket yang di-refund: "))
    while tickets <= 0:
        if tickets == 0:
            cancel_refund = input("Batalkan refund tiket? [Y/N] ")
            while cancel_refund.upper() != 'Y' or cancel_refund.upper() != 'N':
                cancel_refund = input("Masukan salah. Batalkan refund tiket? [Y/N] ")
            if cancel_refund == 'Y':
                return
            else:  # cancel_refund == 'N'
                tickets = int(input("Jumlah refund yang digunakan: "))
        else:
            tickets = int(input("Jumlah tiket harusnya bukan negatif. Mohon diulang: "))

    # Mengecek apakah pengguna sudah membeli tiket pada wahana

    previously_bought = aux.merge(
        [tiket.data[0]], aux.find_baris_all(tiket.data, "Username", username))

    ticket_id_wahana = aux.find_baris_first(previously_bought, "ID_Wahana", id_wahana)
    owned_tickets = str(ticket_id_wahana[aux.find_idx(tiket.data, "Jumlah_Tiket")])

    if ticket_id_wahana == []:
        # Jika pengguna belum pernah membeli tiket di id_wahana, pengguna tidak diperbolehkan memakai tiket.
        print("Tiket Anda tidak valid dalam sistem kami.")
        print("Alasan: Belum membeli tiket pada wahana " + wahana_name + ".\n")
        return
    
    owned_tickets = str(ticket_id_wahana[aux.find_idx(tiket.data, "Jumlah_Tiket")])

    if int(owned_tickets) < tickets:
        # Jika pengguna meminta tiket lebih banyak daripada yang sebenarnya ia punya, pengguna tidak diperbolehkan me-refund tiket.
        print("Tiket Anda tidak valid dalam sistem kami.")
        print("Alasan: Anda hanya memiliki " + owned_tickets + " tiket pada wahana " + wahana_name + ".\n")
    else:
        # Jika pengguna memiliki tiket yang cukup pada wahana, pengguna boleh me-refund tiket.

        # File refund tiket diupdate, sesuai banyak tiket yang dipakai.
        data_refund = [username, date_now, id_wahana, tickets]
        new_refund = aux.konsDot(refund.data, data_refund)
        load.store("refund.csv", new_refund)

        # File refund tiket diupdate, banyak tiket yang dimiliki pengguna dikurangi banyak tiket yang di-refund
        if owned_tickets == tickets:
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

        # Memberi refund ke saldo akun pengguna
        single_ticket_price = int(wahana_found[aux.find_idx(wahana.data, "Harga_Tiket")])
        refund_percentage = 0.8 # Konstanta persentase dari harga tiket
        refund_amount = int(tickets * refund_percentage *  single_ticket_price)
        pengguna[1][aux.find_idx(pengguna, "Saldo")] = str(balance + refund_amount)

        print("Uang refund sudah kami berikan pada akun Anda.\n\n")

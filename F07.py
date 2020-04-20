# F07 - PEMBELIAN TIKET
# Desainer: Sulthan
# Coder: Sulthan
# Tester: Sulthan 

import F01 as load
import auxilliary as aux

def main(pengguna):
    # PROCEDURE main (input pengguna)
    # I.S. pembelian dan tiket abstrak
    # F.S. Jika input lolos ujian, tiket dan pembelian akan diupdate.
    # KAMUS LOKAL

    # ALGORITMA
    wahana = load.use("wahana.csv")
    pembelian = load.use("pembelian.csv")
    tiket = load.use("tiket.csv")

    username = str(pengguna[1][aux.find_idx(pengguna, "Username")])
    date_of_birth = str(pengguna[1][aux.find_idx(pengguna, "Tanggal_Lahir")])
    height = int(pengguna[1][aux.find_idx(pengguna, "Tinggi_Badan")])
    balance = int(pengguna[1][aux.find_idx(pengguna, "Saldo")])
    
    # Input dan validasi ID Wahana
    id_wahana = input("Masukkan ID wahana: ")
    wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)
    while wahana_found == []:
        id_wahana = input("Tidak ditemukan wahana dengan ID \"" + id_wahana + '\". Mohon diulang: ')
        wahana_found = aux.find_baris_first(wahana.data, "ID_Wahana", id_wahana)
    
    # Input dan validasi tanggal hari ini
    date_now = aux.input_date("Masukkan tanggal hari ini: ")
    age = aux.years_since_then(date_of_birth, date_now) # Menentukan umur dari pengguna

    # Input dan validasi jumlah tiket yang ingin dibeli
    tickets = int(input("Jumlah tiket yang dibeli: "))
    while tickets <= 0:
        if tickets == 0:
            cancel_buy = input("Batalkan pembelian tiket? [Y/N] ")
            while cancel_buy.upper() != 'Y' and cancel_buy.upper() != 'N':
                cancel_buy = input("Masukan salah. Batalkan pembelian tiket? [Y/N] ")
            if cancel_buy == 'Y':
                return
            else: # cancel_buy == 'N'
                tickets = int(input("Jumlah tiket yang dibeli: "))
        else:
            tickets = int(input("Jumlah tiket harusnya bukan negatif. Mohon diulang: "))

    # Mengecek apakah umur pengguna sudah memenuhi batasan umur wahana.
    wahana_age_group = wahana_found[aux.find_idx(wahana.data, "Batasan_Umur")]
    # Wahana untuk anak-anak, tetapi pengguna dewasa
    if wahana_age_group == "anak-anak" and age >= 17:
        print("Batasan umur: Anak-anak (< 17 tahun)")
        print("Umur Anda: " + str(age))
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini."
              + "\nSilakan menggunakan wahana lain yang tersedia.")
        return
    # Wahana untuk dewasa, tetapi pengguna anak-anak
    elif wahana_age_group == "dewasa" and age < 17:
        print("Batasan umur: Dewasa (>= 17 tahun)")
        print("Umur Anda: " + str(age))
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini."
              + "\nSilakan menggunakan wahana lain yang tersedia.")
        return
    
    # Mengecek apakah tinggi pengguna sudah memenuhi batasan tinggi wahana.
    wahana_height_group = wahana_found[aux.find_idx(wahana.data, "Batasan_Tinggi")]
    # Wahana untuk pemain >170cm, tetapi pengguna <=170cm. 
    if wahana_height_group == ">170" and height <= 170:
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini."
              + "\nSilakan menggunakan wahana lain yang tersedia.")
        return

    # Mengecek apakah pengguna memiliki saldo yang cukup.
    tickets_price = tickets * int(wahana_found[aux.find_idx(wahana.data, "Harga_Tiket")])
        # Saldo pengguna tidak cukup untuk membeli tiket
    if tickets_price > balance: 
        print("Harga tiket total: " + str(tickets_price))
        print("Saldo: " + str(balance))
        print("Saldo anda tidak cukup.")
        print("Silakan mengisi saldo Anda.")
        return


    # Jika lolos semua pengecekan, akan dimulai proses penyetoran data pembelian tiket.

    # Menuliskan pembelian baru ke rekaman pembelian.csv

    data_pembelian = [username, date_now, id_wahana, tickets]
    new_pembelian = aux.konsDot(pembelian.data, data_pembelian)
    load.store("pembelian.csv", new_pembelian)

    # Menambahkan kepemilikan tiket ke rekaman tiket.csv

    previously_bought = aux.merge([tiket.data[0]], aux.find_baris_all(tiket.data, "Username", username))

    if previously_bought[1:] == [[]]:
        # Jika pengguna belum pernah membeli tiket sama sekali, ditambahkan entry baru.
        data_tiket = [username, id_wahana, tickets]
        new_tiket = aux.konsDot(tiket.data, data_tiket)
    
    else:  # Pengguna sudah pernah membeli tiket sebelumnya.
        ticket_id_wahana = aux.find_baris_first(previously_bought, "ID_Wahana", id_wahana)

        if ticket_id_wahana == []:
            # Jika pengguna belum pernah membeli tiket di id_wahana yang sama sebelumnya, ditambahkan entry baru.
            data_tiket = [username, id_wahana, tickets]
            new_tiket = aux.konsDot(tiket.data, data_tiket)
        else:
            # Jika pengguna pernah membeli tiket di id_wahana yang sama sebelumnya, baris tersebut diperbarukan.
            new_tiket = tiket.data
            row_to_be_changed = aux.find_baris_idx(new_tiket, ticket_id_wahana) # Baris tiket yang ingin diganti
            idx_col_jml_tiket = aux.find_idx(new_tiket, "Jumlah_Tiket")
            new_tiket[row_to_be_changed][idx_col_jml_tiket] = str(int(new_tiket[row_to_be_changed][idx_col_jml_tiket]) + tickets)

    load.store("tiket.csv", new_tiket)

    # Mengurangi saldo pengguna dengan harga tiket yang dibayar.
    pengguna[1][aux.find_idx(pengguna, "Saldo")] = str(balance - tickets_price)

    print("Prosedur pembelian tiket telah selesai."
           + "\nSelamat bersenang-senang di " + wahana_found[aux.find_idx(wahana.data, "Nama_Wahana")] + "!\n\n")
    
    return
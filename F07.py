# F07 - PEMBELIAN TIKET
# 
import F01 as load
import auxilliary as aux

def main(pengguna, wahana, pembelian, tiket):
    # PROCEDURE beli_tiket (input pengguna, input wahana : Rekaman
    #                      input/output : pembelian, input/output : tiket)
    # I.S. pembelian_tiket abstrak, username sudah pasti ada di database user
    # F.S. Jika input lolos ujian, pembelian_tiket akan ditambah sesuai pembelian tiket yang dilakukan pengguna.
    # KAMUS LOKAL

    # ALGORITMA
    username = pengguna[1][aux.find_idx(pengguna, "Username")]
    date_of_birth = pengguna[1][aux.find_idx(pengguna, "Tanggal_Lahir")]
    
    id_wahana = input("Masukkan ID wahana: ")
    date_now = input("Masukkan tanggal hari ini: ")
    tickets = input("Jumlah tiket yang dibeli: ")

    age = aux.years_since_then(date_of_birth, date_now)

    # Menuliskan pembelian baru ke rekaman pembelian.csv
    data_pembelian = [username, date_now, id_wahana, tickets]
    new_pembelian = aux.konsDot(pembelian.data, data_pembelian)
    load.store("pembelian.csv", new_pembelian)

    # Menambahkan kepemilikan tiket ke rekaman tiket.csv
    if aux.find_baris_first(tiket.data, "Username", username) == []: 
        # Jika pengguna belum pernah membeli tiket sama sekali, ditambahkan entry baru.
        data_tiket = [username, id_wahana, tickets]
        new_tiket = aux.konsDot(tiket.data, data_tiket)
    
    else:  # Pengguna sudah pernah membeli tiket sebelumnya.
        
        previously_bought = aux.find_baris_all(tiket.data, "Username", username)
        if aux.find_baris_first(previously_bought, "ID_Wahana", id_wahana) == []:
            # Jika pengguna belum pernah membeli tiket di id_wahana yang sama sebelumnya, ditambahkan entry baru.
            data_tiket = [username, id_wahana, tickets]
            new_tiket = aux.konsDot(tiket.data, data_tiket)
        else:
            # Jika pengguna pernah membeli tiket di id_wahana yang sama sebelumnya, baris tersebut diperbarukan.
            
            # !!!
            # BELUM DIIMPLEMENTASIKAN
            # !!!
            
            new_tiket = tiket.data # Sementara
    load.store("tiket.csv", new_tiket)

    print("Prosedur pembelian tiket telah selesai.", end="\n\n")

    # 1. Meminta input berikut: ID wahana, tanggal hari ini, jumlah tiket yang dibeli - sudah
    # 2. Validasi input! - belum
    # 3. Mengecek apabila pengguna memenuhi persyaratan wahana - belum
    # 4. Mengecek apabila saldo pengguna sudah cukup - belum
    # 5. Jika lolos semua pengecekan, ditulis data pembelian ke pembelian_tiket - penulisan sudah
    #    dan tambahkan tiket ke kepemilikan_tiket

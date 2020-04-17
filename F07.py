# F07 - PEMBELIAN TIKET
# 
import auxilliary as aux

def beli_tiket(pengguna, user, wahana, pembelian_tiket, kepemilikan_tiket):
    # PROCEDURE beli_tiket (input user : string, input user : FileCSV, input wahana : FileCSV
    #                      input/output : pembelian_tiket, input/output : kepemilikan_tiket)
    # I.S. pembelian_tiket abstrak, username sudah pasti ada di database user
    # F.S. Jika input lolos ujian, pembelian_tiket akan ditambah sesuai pembelian tiket yang dilakukan pengguna.
    # KAMUS LOKAL

    # ALGORITMA
    username = pengguna[1][aux.find_idx(pengguna, "Username")]
    date_of_birth = pengguna[1][aux.find_idx(pengguna, "Tanggal_Lahir")]
    
    idwahana = input("Masukkan ID wahana: ")
    date_now = input("Masukkan tanggal hari ini: ")
    tickets = input("Jumlah tiket yang dibeli: ")

    


    return
    
    # 1. Meminta input berikut: ID wahana, tanggal hari ini, jumlah tiket yang dibeli
    # 2. Validasi input!
    # 3. Mengecek apabila pengguna memenuhi persyaratan wahana
    # 4. Mengecek apabila saldo pengguna sudah cukup
    # 5. Jika lolos semua pengecekan, ditulis data pembelian ke pembelian_tiket
    #    dan tambahkan tiket ke kepemilikan_tiket

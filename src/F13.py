# F13 - TOP UP SALDO

import F01 as load
import auxilliary as aux

def main():
    # procedure main(input/output user : Rekaman)
    # I.S. user abstrak
    # F.S. Jika top-up berjalan, user akan diupdate.
    # KAMUS LOKAL
    # user : Rekaman
    # username : string
    # user_found : array [0..6] of string
    # balance, topup, new_balance : integer 
    # ALGORITMA
    user = load.use("user.csv")

    # Input dan validasi Username:
    username = input("Masukkan username: ")
    user_found = aux.find_baris_first(user.data, "Username", username)
    while user_found == []:
        username = input("Tidak ditemukan pengguna dengan username \"" + username + '\". Mohon diulang: ')
        user_found = aux.find_baris_first(user.data, "Username", username)
    user_real_name = str(user_found[aux.find_idx(user.data, "Nama")])
    balance = int(user_found[aux.find_idx(user.data, "Saldo")])

    # Input dan validasi penambahan saldo
    topup = int(input("Jumlah saldo yang di-top up: "))
    while topup <= 0:
        if topup == 0:
            cancel_topup = input("Batalkan top up? [Y/N] ")
            while cancel_topup.upper() != 'Y' or cancel_topup.upper() != 'N':
                cancel_topup = input("Masukan salah. Batalkan top up? [Y/N] ")
            if cancel_topup == 'Y':
                return
            else:  # cancel_topup == 'N'
                topup = int(input("Jumlah saldo yang di-top up: "))
        else:
            topup = int(input("Jumlah saldo harusnya bukan negatif. Mohon diulang: "))
    
    new_balance = balance + topup

    # Baris kepemilikan tiket pengguna diganti dengan banyak tiket baru.
    row_to_be_changed = aux.find_baris_idx(user.data, user_found)  # Baris user yang ingin diganti
    idx_col_saldo = aux.find_idx(user.data, "Saldo")
    new_user = user.data
    new_user[row_to_be_changed][idx_col_saldo] = str(new_balance)  # Penggantian baris
    load.store("user.csv", new_user)

    print("Top up berhasil. Saldo " + user_real_name + " bertambah menjadi " + str(new_balance) + ".")

    return

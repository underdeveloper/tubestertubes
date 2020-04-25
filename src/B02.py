# B02 - Golden Account
# Module B02 merupakan file berisi fungsi untuk melakukan upgrade akun pemain
# menjadi golden account, dengan harga-harga tiket jadi setengah.
# Module ini hanya bisa diakses oleh admin.

import F01 as load
import auxilliary as aux

def main():
    # PROCEDURE main (output user : Rekaman)
    # I.S. user abstrak
    # F.S. user diganti satu barisnya sehingga kolom "Role" berisi "Gold"
    # KAMUS LOKAL
    # username_upgraded : string
    # user_found : array[0..1] of array[0..6] of string
    # new_user : Rekaman.data
    # row_to_be_changed : array[0..6] of string
    # idx_col_role : integer
    # ALGORITMA
    user = load.use("user.csv")

    username_upgraded = input("Masukkan username yang ingin di-upgrade: ")
    user_found = aux.find_baris_first(user.data, "Username", username_upgraded)
    while user_found == []:
        username_upgraded = input("Tidak ditemukan user dengan username \"" + username_upgraded + '\". Mohon diulang: ')
        user_found = aux.find_baris_first(user.data, "Username", username_upgraded)

    if user_found[aux.find_idx(user.data, "Role")] == "Gold":
        print("Pemain " + username_upgraded + " sudah memiliki akun Gold.")
    elif user_found[aux.find_idx(user.data, "Role")] == "Admin":
        print("Admin tidak bisa menjadi akun Gold.")
    else:
        # Meng-update file user.csv sesuai upgrade akun pemain.
        new_user = user.data
        row_to_be_changed = aux.find_baris_idx(new_user, user_found) # Baris user yang ingin diganti
        idx_col_role = aux.find_idx(new_user, "Role")
        new_user[row_to_be_changed][idx_col_role] = "Gold"
        load.store("user.csv", new_user)

        print("Akun pemain " + username_upgraded + " telah di-upgrade.")

    return

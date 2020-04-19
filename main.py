# KAMUS
# exit_flag, isGonnaSave : boolean

# import f01, f02, f03, f04... dll
import F01 as load
import F02 as save
import F03 as signup
import F04 as login
import F06 as cari_wahana
import F07 as beli_tiket
import F16 as exit
import auxilliary as flib
# Petunjuk penggunaan fungsi/prosedur tiap-tiap modul ada pada masing-masing file modul

# Memuat file-filenya (F01 - Load file)

# load.main() # Manually load semua file.
load.main_auto() # Automatically load semua file. Mohon diganti jadi yang manual jika sudah selesai.

# Data semua file .csv telah di-load ke dalam suatu array bernama load.file.data
# Untuk memanggil salah satu file pada array bisa dengan load.use(<Nama File>.csv)
# Untuk mengesave salah satu file ke array bisa dengan load.store(<Nama File>.csv)
# contoh: signup.main(load.use("user.csv")) akan memanggil prosedur signup.main yang membutuhkan file user.csv sebagai input
# Jangan coba-coba memanggil array secara paksa dengan load.file.data[<Nama File>.csv]
# Perubahan pada array tidak akan di-save ke file .csv asli sampai ada pemanggilan modul save.

# Login oleh user (F04 - Login user)
# Login sebagai admin:
# Username: wangkypro
# Password: coklatenaknol
whoami = login.main(load.use("user.csv"))

# Dideklarasi exit_flag (boolean) yang menandakan apabila user sudah mau keluar dari program
# Awalnya exit_flag = False
if (whoami != []):
    exit_flag = False

# Looping

# Loop pemain
while ((exit_flag == False) and (flib.find_baris_first(whoami, "Role", "Pemain") != [])):
    print("Anda ter-logged in sebagai " + whoami[1][flib.find_idx(whoami, "Username")])
    print("Anda adalah seorang Pemain.")
    print("Apa yang mau anda lakukan?")
    print("[2] Menyimpan semua perubahan yang sudah dilakukan.")
    print("[6] Mencari wahana sesuai pembatasan user.")
    print("[7] Membeli tiket.")
    print("[16] Log-out.")
    x = input("Masukkan nomor aksi yang ingin anda lakukan: ")
    if (x == "2"):
        save.main(load.files)
    elif (x == "6"):
        cari_wahana.main('wahana.csv')
    elif (x == "7"):
        beli_tiket.main(whoami, load.use("wahana.csv"), load.use("pembelian.csv"), load.use("tiket.csv"))
    elif (x == "16"):
        exit_flag = True
    else:
        print("ERROR: Unknown command.")
        print("")

# Loop admin
while ((exit_flag == False) and (flib.find_baris_first(whoami, "Role", "Admin") != [])):
    print("Anda ter-logged in sebagai " + whoami[1][flib.find_idx(whoami, "Username")])
    print("Anda adalah seorang Admin.")
    print("Apa yang mau anda lakukan?")
    print("[2] Menyimpan semua perubahan yang sudah dilakukan.")
    print("[3] Mendaftarkan pemain baru.")
    print("[16] Log-out.")
    x = input("Masukkan nomor aksi yang ingin anda lakukan: ")
    if (x == "2"):
        save.main(load.files)
    elif (x == "3"):
        userfile = signup.main(load.use("user.csv"))
        load.files[0] = userfile
    elif (x == "16"):
        exit_flag = True
    else:
        print("ERROR: Unknown command.")
        print("")

# Setelah looping selesai, program selesai
if (exit_flag == True):
    isGonnaSave = exit.main()
    if (isGonnaSave == True):
        # save.main(load.files) # Manually save semua file.
        save.main_auto(load.files) # Automatically save semua file. Mohon diganti jadi yang manual jika sudah selesai.

        raise SystemExit

    else:
        raise SystemExit
else:
    print("ERROR: Unexpected exit from user/admin loop. Changes will not be saved.")
# KAMUS
# exit_flag, isGonnaSave : boolean

# import f01, f02, f03, f04... dll
import F01 as load
import F02 as save
import F03 as signup
import F04 as login
import F16 as exit

# Memuat file-filenya (F01 - Load file)
load.main()
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
while ((exit_flag == False) and (load.find_baris(whoami, "Role", "Pemain") != [])):
    print("Anda ter-logged in sebagai " + whoami[1][load.find_idx(whoami, "Username")])
    print("Anda adalah seorang Pemain.")
    print("Apa yang mau anda lakukan?")
    print("[2] Menyimpan semua perubahan yang sudah dilakukan.")
    print("[16] Log-out.")
    x = str(input("Masukkan nomor aksi yang ingin anda lakukan: "))
    if (str(x) == "2"):
        save.main(load.file.data)
        print("")
    elif (str(x) == "16"):
        exit_flag = True
    else:
        print("ERROR: Unknown command.")
        print("")

# Loop admin
while ((exit_flag == False) and (load.find_baris(whoami, "Role", "Admin") != [])):
    print("Anda ter-logged in sebagai " + whoami[1][load.find_idx(whoami, "Username")])
    print("Anda adalah seorang Admin.")
    print("Apa yang mau anda lakukan?")
    print("[2] Menyimpan semua perubahan yang sudah dilakukan.")
    print("[3] Mendaftarkan pemain baru.")
    print("[16] Log-out.")
    x = str(input("Masukkan nomor aksi yang ingin anda lakukan: "))
    if (str(x) == "2"):
        save.main(load.file.data)
        print("")
    elif (str(x) == "3"):
        signup.main(load.use("user.csv"))
        print("")
    elif (str(x) == "16"):
        exit_flag = True
    else:
        print("ERROR: Unknown command.")
        print("")

# Setelah looping selesai, program selesai
if (exit_flag == True):
    isGonnaSave = exit.main()
    if (isGonnaSave == True):
        save.main(load.file.data)
        raise SystemExit
    else:
        raise SystemExit
else:
    print("ERROR: Unexpected exit from user/admin loop. Changes will not be saved")
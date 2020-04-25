# KAMUS
# exit_flag, isGonnaSave : boolean

# import f01, f02, f03, f04... dll
import F01 as load
import F02 as save
import F03 as signup
import F04 as login
import F05 as cari_pemain
import F06 as cari_wahana
import F07 as beli_tiket
import F08 as pakai_tiket
import F09 as refund
import F10 as input_kritik_saran
import F11 as output_kritik_saran
import F12 as tambah_wahana
import F13 as topup
import F14 as riwayat_wahana
import F15 as tiket_user
import F16 as exit_program
import B02 as gold_upgrade
import B03 as best_wahana
import B04 as hilang_tiket
import auxilliary as flib
# Petunjuk penggunaan fungsi/prosedur tiap-tiap modul ada pada masing-masing file modul

# Memuat file-filenya (F01 - Load file)

# load.main()
load.main_auto() # Ganti jadi yang manual kalo testing sudah selesai.

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
while exit_flag == False and (whoami[1][flib.find_idx(whoami, "Role")] == "Pemain" or whoami[1][flib.find_idx(whoami, "Role")] == "Gold"):
    print("Anda ter-logged in sebagai " + whoami[1][flib.find_idx(whoami, "Username")])
    print("Anda adalah seorang Pemain.")
    print("Apa yang mau anda lakukan? (Ketik \"list\" untuk melihat daftar command)")
    command = input("$ ")
    print("")
    if (command == "list"):
        flib.command_pemain()
    elif (command == "save"):
        # save.main(load.files)
        save.main_auto(load.files) # tolong ganti ya :)
    elif (command == "cari wahana"):
        cari_wahana.main()
    elif (command == "beli"):
        beli_tiket.main(whoami)
    elif (command == "main"):
        pakai_tiket.main(whoami)
    elif (command == "hilang"):
        hilang_tiket.main(whoami)
    elif (command == "refund"):
        refund.main(whoami)
    elif (command == "beri kritik saran"):
        input_kritik_saran.main(whoami)
    elif (command == "exit"):
        exit_flag = True
    else:
        print("ERROR: Unknown command.")
    print("")

# Loop admin
while exit_flag == False and whoami[1][flib.find_idx(whoami, "Role")] == "Admin":
    print("Anda ter-logged in sebagai " + whoami[1][flib.find_idx(whoami, "Username")])
    print("Anda adalah seorang Admin.")
    print("Apa yang mau anda lakukan? (Ketik \"list\" untuk melihat daftar command)")
    command = input("$ ")
    print("")
    if (command == "list"):
        flib.command_admin()
    elif (command == "save"):
        # save.main(load.files) 
        save.main_auto(load.files) # diganti lagi jadi manual kalo udah :)
    elif (command == "signup"):
        userfile = signup.main(load.use("user.csv"))
        load.files[0] = userfile
    elif (command == "cari pemain"):
        cari_pemain.main(load.use("user.csv"))
    elif (command == "topup"):
        topup.main()
    elif (command == "hilang"):
        hilang_tiket.main(whoami)
    elif (command == "upgrade"):
        gold_upgrade.main()
    elif (command == "lihat kritik saran"):
        output_kritik_saran.print_sorted()
    elif (command == "tambah wahana"):
        tambah_wahana.main()
    elif (command == "riwayat wahana"):
        riwayat_wahana.main()
    elif (command == "best"):
        best_wahana.main()
    elif (command == "exit"):
        exit_flag = True
    else:
        print("ERROR: Unknown command.")
    print("")

# Setelah looping selesai, program selesai
if (exit_flag == True):
    isGonnaSave = exit_program.main()
    if (isGonnaSave == True):
        # save.main(load.files)
        save.main_auto(load.files) # Ganti jadi yang manual kalo testing sudah selesai.
        raise SystemExit
    else:
        raise SystemExit
else:
    print("ERROR: Unexpected exit from user/admin loop. Changes will not be saved.")

# import f01, f02, f03, f04... dll
import F01 as load
import F02 as save
import F03 as signup
import F04 as login

# Memuat file-filenya (F01 - Load file)
load.main()
# Data semua file .csv telah di-load ke dalam suatu array bernama load.file.data
# Untuk memanggil salah satu file pada array bisa dengan load.use(<Nama File>.csv)
# Untuk mengesave salah satu file ke array bisa dengan load.store(<Nama File>.csv)
# contoh: signup.main(load.use("user.csv")) akan memanggil prosedur signup.main yang membutuhkan file user.csv sebagai input
# Jangan coba-coba memanggil array secara paksa dengan load.file.data[<Nama File>.csv]
# Perubahan pada array tidak akan di-save ke file .csv asli sampai ada pemanggilan modul save.

#signup.main(load.use("user.csv"))
#print(load.use("user.csv"))
#save.main(load.file.data)

# Login oleh user (F04 - Login user)
# whoami = login.main(load.use("user.csv"))
# print(whoami)

user = load.use("user.csv")


x = load.search(user, "Username", "Nama", "Willy Wangky")
print("Username hasil search adalah: " + x)

# Dideklarasi exit_flag (boolean) yang menandakan apabila user sudah mau keluar dari program
# Awalnya exit_flag = False

# Looping
''' 
    Dilakukan looping pake while (not exit_flag)
    User bisa menggunakan fitur-fitur di sini sebanyak mungkin

    Looping akan di break ketika exit_flag == True (dilakukan oleh F16 - Exit)
'''

# Setelah looping selesai, program selesai
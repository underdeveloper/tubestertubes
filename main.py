# import f01, f02, f03, f04... dll
import F01 as load

# Memuat file-filenya (F01 - Load file)
filedescs = ["User", "Daftar Wahana", "Pembelian Tiket", "Penggunaan Tiket",
             "Kepemilikan Tiket", "Refund Tiket", "Kritik dan Saran"]

# Variabel files berisi semua rekaman-rekaman dari file yang telah dimuat.
load.main(filedescs)
# Sekarang semua file udah kemuat di <load.files>

# Cara mengeluarkan tabel dari suatu file:
# Misalnya kita mau ngambil tabel dari wahana.csv, gunakan F01.get_data():
tabel_wahana = load.get("wahana.csv")
# Ini merupakan tabel berisi data wahana, yang bisa diakses oleh modul lain.
print(tabel_wahana)










# Login oleh user (F04 - Login user)

# Dideklarasi exit_flag (boolean) yang menandakan apabila user sudah mau keluar dari program
# Awalnya exit_flag = False

# Looping
''' 
    Dilakukan looping pake while (not exit_flag)
    User bisa menggunakan fitur-fitur di sini sebanyak mungkin

    Looping akan di break ketika exit_flag == True (dilakukan oleh F16 - Exit)
'''
# exit_flag = False
# while (not exit_flag):
#     command = input("> ")
#     if command == "cari":
#         F06.pencarian_wahana(wahana)
#         exit_flag = True
#     else:
#         print("Salah command!")
    

# Setelah looping selesai, program selesai

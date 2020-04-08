# import f01, f02, f03, f04... dll
import F01

# Memuat file-filenya (F01 - Load file)
koleksi_file = F01.main()

user = koleksi_file.files[0] # Data dari user.csv
print(user.contents) # Mengoutput isi dari variabel user

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

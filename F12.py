# PROGRAM F12
# Menambahkan wahana baru bila user adalah admin

# Desainer : Stefanny
# Coder : Stefanny


# KAMUS
class user :
    datacount = 5
    datadesc = ("ID_Wahana", "Nama_Wahana", "Harga_Tiket",
                "Batasan_Umur", "Batasan_Tinggi")
    data = ["*" for i in range (datacount)]

# ALGORITMA


# REALISASI FUNGSI/PROSEDUR
def main(userfile):
    # Fungsi utama F12
    # Semua masukkan diasumsikan valid

    print ("Masukkan Informasi Wahana yang ditambahkan: ", end = " ")
    for i in range (user.datacount):
        if (user.datadesc[i] == "ID_Wahana") :
            user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
        elif (user.datadesc[i] == "Nama_Wahana") :
            user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
        elif (user.datadesc[i] == "Harga_Tiket"):
            user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
        elif (user.datadesc[i] == "Batasan_Umur"):
            user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))
        elif (user.datadesc[i] == "Batasan_Tinggi"):
            user.data[i] = str(input("Masukkan " + user.datadesc[i] + ": "))

    userfile.dat = user.data
    print ("")
    print ("Info wahana telah ditambahkan!")
    print ("")
    return userfile

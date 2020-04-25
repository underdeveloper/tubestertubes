# PROGRAM F12
# Menambahkan wahana baru bila user adalah admin

# Desainer : Stefanny
# Coder : Stefanny

# ALGORITMA
import auxilliary as aux
import F01 as load

# REALISASI FUNGSI/PROSEDUR
def main():
    # Fungsi utama F12
    # Semua masukkan diasumsikan valid
    wahana = load.use("wahana.csv")
    array_wahana_baru = ["ID_Wahana" , "Nama_Wahana" , "Harga_Tiket" 
    , "Batasan_Umur" , "Batasan_Tinggi"]
    
    print ("Masukkan Informasi Wahana yang ditambahkan: ", end = " ")
    
    for i in range (aux.length(array_wahana_baru)):
        if (array_wahana_baru[i] == "ID_Wahana") :
            array_wahana_baru[i] = str(input("Masukkan " + array_wahana_baru[i] + ": "))
        elif (array_wahana_baru[i] == "Nama_Wahana") :
            array_wahana_baru[i] = str(input("Masukkan " + array_wahana_baru[i] + ": "))
        elif (array_wahana_baru[i] == "Harga_Tiket"):
            array_wahana_baru[i] = str(input("Masukkan " + array_wahana_baru[i] + ": "))
        elif (array_wahana_baru[i] == "Batasan_Umur"):
            array_wahana_baru[i] = str(input("Masukkan " + array_wahana_baru[i] + ": "))
        elif (array_wahana_baru[i] == "Batasan_Tinggi"):
            array_wahana_baru[i] = str(input("Masukkan " + array_wahana_baru[i] + ": "))

    wahana_baru_added = aux.konsDot(wahana.data,array_wahana_baru)
    wahana.data = wahana_baru_added
    print ("")
    print ("Info wahana telah ditambahkan!")
    print ("")
    return 

def pencarian_pemain (x):
    import pandas as pd
    df = pd.read_csv("wahana.csv")
    print ("Jenis batasan umur: ")
    print ("1. Anak-anak (<17 tahun)")
    print ("2. Dewasa (>=17 tahun)")
    print ("3. Semua umur")
    print (" ")
    print ("Jenis batasan tinggi badan: ")
    print ("1. Lebih dari 170 cm")
    print ("2. Tanpa batasan")
    print (" ")
    umur_pemain = int(input("Batasan umur pemain: "))
    if umur_pemain == 1 or umur_pemain == 2 or umur_pemain == 3:
        umur_pemain = umur_pemain
    else:
        print("Batasan umur tidak valid!")
        T = True
        while T:
            umur_pemain = int(input("Batasan umur pemain: "))
            if umur_pemain == 1:
                T = False
            elif umur_pemain == 2:
                T = False
            elif umur_pemain == 3:
                T = False
            else:
                T = True
                print("Batasan umur tidak valid!")
    tinggi_badan = int(input ("Batasan tinggi badan: "))
    if tinggi_badan == 1 or tinggi_badan == 2 or tinggi_badan == 3:
        tinggi_badan = tinggi_badan
    else:
        print("Batasan tinggi badan tidak valid!")
        T = True
        while T:
            tinggi_badan = int(input("Batasan tinggi badan: "))
            if tinggi_badan == 1:
                T = False
            elif tinggi_badan == 2:
                T = False
            elif tinggi_badan == 3:
                T = False
            else:
                T = True
                print("Batasan tinggi badan tidak valid!")
    if umur_pemain == 1:
        if tinggi_badan == 1:
            ut11 = df.loc[df["Batasan_Umur"]<17] & [df["Batasan_Tinggi"]>170]
            print ([ut11.loc["ID_Wahana"]], " | ", [ut11.loc["Nama_Wahana"]], " | ", [ut11.loc["Harga_Tiket"]])
        elif tinggi_badan == 2:
            ut12 = df.loc[df["Batasan_Umur"]<17] & [df["Batasan Tinggi"]== "Tanpa Batasan"]
            print([ut12.loc["ID_Wahana"]], " | ", [ut12.loc["Nama_Wahana"]], " | ", [ut12.loc["Harga_Tiket"]])
    elif umur_pemain == 2:
        if tinggi_badan == 1:
            ut21 = df.loc[df["Batasan_Umur"]>=17] & [df["Batasan_Tinggi"]>170]
            print([ut21.loc["ID_Wahana"]], " | ", [ut21.loc["Nama_Wahana"]], " | ", [ut21.loc["Harga_Tiket"]])
        elif tinggi_badan == 2:
            ut22 = df.loc[df["Batasan_Umur"]>=17] & [df["Batasan_Tinggi"] == "Tanpa Batasan"]
            print([ut22.loc["ID_Wahana"]], " | ", [ut22.loc["Nama_Wahana"]], " | ", [ut22.loc["Harga_Tiket"]])
    elif umur_pemain == 3:
        ut31 = df.loc[df["Batasan_Umur"] == "Semua Umur"] & [df["Batasan_Tinggi"] > 170]
        if tinggi_badan == 1:
            print ([ut31.loc["ID_Wahana"]], " | ", [ut31.loc["Nama_Wahana"]], " | ", [ut31.loc["Harga_Tiket"]])
        elif tinggi_badan == 2:
            ut32 =df.loc[df["Batasan_Umur"] == "Semua Umur"] & [df["Batasan_Tinggi"] == "Tanpa Batasan"]
            print([ut32.loc["ID_Wahana"]], " | ", [ut32.loc["Nama_Wahana"]], " | ", [ut32.loc["Harga_Tiket"]])

x = input()
pencarian_pemain(x)
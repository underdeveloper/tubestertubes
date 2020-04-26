# Program F16
# Memulai proses exit program, dan menanyakan apakah perubahan mau disimpan atau tidak

# KAMUS

# ALGORITMA PROGRAM UTAMA

# REALISASI FUNGSI/PROSEDUR

def main():
    # function main () -> boolean
    # Mencari tahu apakah user mau melakukan save sebelum meng-exit program
    # KAMUS LOKAL
    # isGonnaSave, isValid : boolean
    # x : string
    # ALGORITMA
    isValid = False
    while (isValid == False):
        x = str(input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan? (Y/N) "))
        if (x.upper() == "Y"):
            isGonnaSave = True
            isValid = True
        elif (x.upper() == "N"):
            isGonnaSave = False
            isValid = True
        else:
            print("Input tidak dimengerti. Silakan ulangi.")
    if (isGonnaSave == True):
        return True
    else: #(isGonnaSave == False)
        return False
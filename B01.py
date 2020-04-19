# B01 - Penyimpanan Password
# Module B01 merupakan file yang digunakan untuk melakukan hashing password pengguna.
# Ini dilakukan supaya penyimpanan password lebih aman, karena tidak hanya
# sebagai plaintext, melainkan dengan hasil hash.

# PESAN KE FERAL ( MOHON INI DIHAPUS KALAU UDAH SELESAI! )
# Ini proses hashnya ya, mohon dipakai untuk bagian signup dan login
# Hasil hash_pass() adalah yang disimpan di kolom "Password" di user.csv
# Makasih

import os
import hashlib
import secrets

def hash_pass(pw, salt=b''):
    # function hash_pass (pw : string, salt : bytes (128)) -> string
    # Melakukan hashing terhadap password.
    # KAMUS LOKAL
    # salt : bytes (128)
    # hash_name : string
    # password : bytes
    # iterations, dklen : int
    # salted_pass : string
    # ALGORITMA
    if salt == b'': # Jika parameter salt tidak diisi, di-generate salt baru
        salt = hashlib.sha256(os.urandom(32)).hexdigest().encode('utf-8') + secrets.token_bytes(32).hex().encode('utf-8')

    key = hashlib.pbkdf2_hmac(
        hash_name='sha512', # Algoritma digest hash
        password=pw.encode('utf-8'), # Password yang akan dihash dijadikan utf-8
        salt=salt, # Salt ditentukan oleh input / dirandomise
        iterations=120000, # Di-hash sebanyak 120000 kali
        dklen=64 # Dengan hasil key berpanjang 128
    ).hex().encode('utf-8')

    salted_pass = (salt + key).decode('utf-8') # Salt dan key disimpan bersama

    return salted_pass 

def verify(stored_hash, given):
    # function verify (stored_hash : string, given : string) -> boolean
    # Mengecek apakah password yang diberikan pengguna 
    # sama dengan password yang disimpan program.
    # KAMUS LOKAL
    # salt : bytes (64)
    # stored_key : bytes (64)
    # given_key : bytes (64)
    # ALGORITMA
    salt = stored_hash[:128].encode('utf-8') # Mendapatkan salt dari hash yang tersimpan
    stored_key = stored_hash[128:] # Mendapatkan key dari hash yang tersimpan

    # Lalu akan dilakukan hash pada <given> dengan salt bernilai <salt>
    given_key = hash_pass(given, salt)[128:] # Mendapatkan key dari hasil hash password yang diberikan.

    return given_key == stored_key


# Kode di bawah untuk mengecek apakah algoritma hash benar.

# this_pass = hash_pass(input("Masukkan password: "))
# print("Password telah disimpan.")

# check_pass = input("Coba lagi masukkan password tersebut: ")
# while not verify(this_pass, check_pass):
#     check_pass = input("Ups, password salah. Coba ulang lagi: ")

# print("Selamat, password benar.")

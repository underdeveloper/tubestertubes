Program ini dibuat dengan tujuan menjadi hasil kerja akhir tugas besar 
kelas K-09 IF1210 (Dasar Pemrograman) STEI 2019. Program ini merupakan 
kerja sepenuhnya dari Kelompok 6 K-09.

CARA MENJALANKAN PROGRAM
1. Buka /src.
2. Interpret file <main.py> dengan python.

DESKRIPSI DIREKTORI DAN FILE

/src  : direktori berisi semua source code yang diperlukan agar program
        berjalan dengan benar.
    ../FXX.py : file python berisi implementasi fitur utama, sesuai 
                spesifikasi.
    ../BXX.py : file python berisi implementasi fitur bonus, sesuai
                spesifikasi.
    ../auxilliary.py : file python berisi fungsi-fungsi pelengkap yang
                       digunakan untuk jalannya program.
    ../main.py : file python berisi algoritma utama dari program.
                 file inilah yang harus di-interpret dengan python
                 untuk menjalankan program.
/data : direktori berisi semua database yang diperlukan agar program
        berjalan dengan benar.

PENJELASAN FUNGSI BONUS
B01.py : Digunakan untuk melakukan hash dengan SHA-512. Salt yang dipakai
         untuk hash didapatkan dengan CSPRNG (Cryptographically Secure
         Pseudo-Random Number Generator), dan password disimpan pada
         database dalam bentuk salt+key (dikonkatenasi).
B02.py : Digunakan oleh admin untuk melakukan upgrade akun pemain menjadi
         golden account. Pemain dengan golden account ditandai dengan
         nilai "Gold" pada kolom "Role" di user.csv, dan mendapat
         diskon 50% untuk semua pembelian tiket.
B03.py : Digunakan oleh admin untuk melihat wahana terbaik. Kebaikan wahana
         diukur dengan melihat banyaknya tiket yang terjual. Tiket yang di-
         refund termasuk terjual.
B04.py : Digunakan oleh pemain dan admin untuk melaporkan kehilangan tiket.
         Pemain hanya dapat melaporkan kehilangan tiket mereka sendiri,
         melainkan admin dapat melaporkan kehilangan tiket untuk pemain.
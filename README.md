Program ini dibuat dengan tujuan menjadi hasil kerja akhir tugas besar <br/>
kelas K-09 IF1210 (Dasar Pemrograman) STEI 2019. Program ini merupakan <br/>
kerja sepenuhnya dari Kelompok 6 K-09.<br/>
<br/>
CARA MENJALANKAN PROGRAM<br/>
1. Buka /src.
2. Interpret file <main.py> dengan python.
<br/>
LOGIN BEBERAPA USER<br/>
Inilah detail login beberapa user, sehingga Anda bisa mengakses program.<br/>
<br/>
username | password<br/>
<br/>
 - ADMIN <br/>
wangkypro | coklatenaknol<br/>
 - PEMAIN / PEMAIN GOLD<br/>
theredshirtedbloke | linguistics<br/>
akumasihkecil | belumjadibesar<br/>
yoels | ilovekermit<br/>
<br/>
DESKRIPSI DIREKTORI DAN FILE<br/>
<br/>
/src  : direktori berisi semua source code yang diperlukan agar program berjalan dengan benar.<br/>
    ../FXX.py : file python berisi implementasi fitur utama, sesuai spesifikasi.<br/>
    ../BXX.py : file python berisi implementasi fitur bonus, sesuai spesifikasi.<br/>
    ../auxilliary.py : file python berisi fungsi-fungsi pelengkap yang digunakan untuk jalannya program.<br/>
    ../main.py : file python berisi algoritma utama dari program. file inilah yang harus di-interpret dengan python untuk menjalankan program.<br/>
/data : direktori berisi semua database yang diperlukan agar program berjalan dengan benar.<br/>
<br/>
PENJELASAN FUNGSI BONUS<br/>
B01.py : Digunakan untuk melakukan hash dengan SHA-512. Salt yang dipakai untuk hash didapatkan dengan CSPRNG (Cryptographically Secure Pseudo-Random Number Generator), dan password disimpan pada database dalam bentuk salt+key (dikonkatenasi).<br/>
B02.py : Digunakan oleh admin untuk melakukan upgrade akun pemain menjadi golden account. Pemain dengan golden account ditandai dengan nilai "Gold" pada kolom "Role" di user.csv, dan mendapat diskon 50% untuk semua pembelian tiket.<br/>
B03.py : Digunakan oleh admin untuk melihat wahana terbaik. Kebaikan wahana diukur dengan melihat banyaknya tiket yang terjual. Tiket yang di-refund termasuk terjual.<br/>
B04.py : Digunakan oleh pemain dan admin untuk melaporkan kehilangan tiket. Pemain hanya dapat melaporkan kehilangan tiket mereka sendiri, melainkan admin dapat melaporkan kehilangan tiket untuk pemain.<br/>
# B03 - Best Wahana
# Module B04 merupakan file berisi prosedur untuk melihat wahana terbaik.

import F01 as load
import auxilliary as aux

def total_sold_tickets(wahana_id):
    # function total_sold_tickets (wahana_id : string) -> integer
    # Menghasilkan total tiket wahana yang telah terjual.
    # KAMUS LOKAL
    # pembelian : Rekaman
    # tickets_sold, i : integer
    # ALGORITMA
    pembelian = load.use("pembelian.csv")
    tickets_sold = 0

    for i in range(1, aux.length(pembelian.data)):
        if str(pembelian.data[i][aux.find_idx(pembelian.data, "ID_Wahana")]) == wahana_id:
            tickets_sold += int(pembelian.data[i][aux.find_idx(pembelian.data, "Jumlah_Tiket")])

    return tickets_sold

def main():
    # procedure main ()
    # I.S. Abstrak
    # F.S. Dikeluarkan tiga wahana 'terbaik' (diurut sesuai jumlah tiket terjual)
    # Syarat: Pasti sudah ada wahana sebanyak >= N_best pada wahana.csv
    # KAMUS LOKAL
    # wahana : Rekaman
    # wahana_ticket_data : array of tuple (string, string, integer)
    # constant N_best : integer = 3
    # i, j, maks_idx : integer
    # wahana_id, wahana_name : string
    # wahana_tickets : integer
    # ALGORITMA
    wahana = load.use("wahana.csv")
    wahana_ticket_data = [("", "", 0) for i in range(1, aux.length(wahana.data))]

    for i in range(1, aux.length(wahana.data)):
        wahana_id = wahana.data[i][aux.find_idx(wahana.data, "ID_Wahana")]
        wahana_name = wahana.data[i][aux.find_idx(wahana.data, "Nama_Wahana")]
        wahana_tickets = total_sold_tickets(wahana_id)
        wahana_ticket_data[i-1] = (wahana_id, wahana_name, wahana_tickets)
    
    # Sorting sesuai jumlah tiket yang terjual
    for i in range(0, aux.length(wahana_ticket_data)):
        maks_idx = i
        for j in range(i, aux.length(wahana_ticket_data)):
            if wahana_ticket_data[maks_idx][2] < wahana_ticket_data[j][2]:
                maks_idx = j
        temp = wahana_ticket_data[i]
        wahana_ticket_data[i] = wahana_ticket_data[maks_idx]
        wahana_ticket_data[maks_idx] = temp
    
    # Output terbaik
    N_best = 3 # konstanta, menyatakan berapa wahana terbaik yang dikeluarkan ke layar.
    for i in range(0,N_best):
        # Yang dikeluarkan ke layar: "Urutan | ID Wahana | Nama Wahana | Jumlah Tiket"
        print(i+1, end=' | ') # Urutan
        print(wahana_ticket_data[i][0], end=' | ') # ID Wahana
        print(wahana_ticket_data[i][1], end=' | ')  # Nama Wahana
        print(wahana_ticket_data[i][2]) # Jumlah Tiket

    return

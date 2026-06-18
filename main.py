from modules.crud import *
from modules.csv_handler import *
from modules.searching import *
from modules.sorting import *
from modules.queue_pinjam import *

FILE_BUKU = "buku.csv"
FILE_PINJAM = "peminjaman.csv"


def menu_cari():

    data = baca_csv(FILE_BUKU)

    keyword = input("Masukkan judul buku : ")

    hasil = cari_buku(data, keyword)

    if len(hasil) == 0:
        print("Buku tidak ditemukan")

    else:
        for buku in hasil:
            print(
                buku["id_buku"],
                buku["judul"],
                buku["penulis"],
                buku["stok"]
            )


def menu_sort():

    data = baca_csv(FILE_BUKU)

    hasil = bubble_sort_judul(data)

    print("\nDATA SETELAH SORTING")
    print("-" * 60)

    for buku in hasil:
        print(
            buku["id_buku"],
            buku["judul"],
            buku["penulis"],
            buku["stok"]
        )


def pinjam_buku():

    data_buku = baca_csv(FILE_BUKU)
    data_pinjam = baca_csv(FILE_PINJAM)

    nama = input("Nama Peminjam : ")
    id_buku = input("ID Buku : ")

    ditemukan = False

    for buku in data_buku:

        if buku["id_buku"] == id_buku:

            if int(buku["stok"]) > 0:

                buku["stok"] = str(
                    int(buku["stok"]) - 1
                )

                tambah_antrian(nama)

                data_pinjam.append({
                    "id_pinjam": f"P{len(data_pinjam)+1:03}",
                    "nama": nama,
                    "id_buku": id_buku
                })

                ditemukan = True

            break

    if ditemukan:

        tulis_csv(
            FILE_BUKU,
            ["id_buku", "judul", "penulis", "stok"],
            data_buku
        )

        tulis_csv(
            FILE_PINJAM,
            ["id_pinjam", "nama", "id_buku"],
            data_pinjam
        )

        print("Peminjaman berhasil")

    else:
        print("Buku tidak tersedia")


def lihat_antrian_pinjam():

    data = lihat_antrian()

    if len(data) == 0:
        print("Antrian kosong")

    else:

        print("\nANTRIAN PEMINJAMAN")

        for i, nama in enumerate(data, start=1):
            print(i, ".", nama)


while True:

    print("\n===== SISTEM PERPUSTAKAAN =====")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Update Buku")
    print("4. Hapus Buku")
    print("5. Cari Buku")
    print("6. Urutkan Buku")
    print("7. Pinjam Buku")
    print("8. Lihat Antrian")
    print("9. Keluar")

    pilih = input("Pilih Menu : ")

    if pilih == "1":
        tambah_buku()

    elif pilih == "2":
        tampil_buku()

    elif pilih == "3":
        update_buku()

    elif pilih == "4":
        hapus_buku()

    elif pilih == "5":
        menu_cari()

    elif pilih == "6":
        menu_sort()

    elif pilih == "7":
        pinjam_buku()

    elif pilih == "8":
        lihat_antrian_pinjam()

    elif pilih == "9":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
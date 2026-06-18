from modules.csv_handler import baca_csv, tulis_csv

FILE_BUKU = "buku.csv"


def tambah_buku():

    data = baca_csv(FILE_BUKU)

    id_buku = input("ID Buku : ")
    judul = input("Judul : ")
    penulis = input("Penulis : ")
    stok = input("Stok : ")

    data.append({
        "id_buku": id_buku,
        "judul": judul,
        "penulis": penulis,
        "stok": stok
    })

    tulis_csv(
        FILE_BUKU,
        ["id_buku", "judul", "penulis", "stok"],
        data
    )

    print("Data berhasil ditambahkan")


def tampil_buku():

    data = baca_csv(FILE_BUKU)

    print("\nDATA BUKU")
    print("-" * 60)

    for buku in data:
        print(
            buku["id_buku"],
            buku["judul"],
            buku["penulis"],
            buku["stok"]
        )


def update_buku():

    data = baca_csv(FILE_BUKU)

    id_cari = input("Masukkan ID Buku : ")

    ditemukan = False

    for buku in data:

        if buku["id_buku"] == id_cari:

            buku["judul"] = input("Judul Baru : ")
            buku["penulis"] = input("Penulis Baru : ")
            buku["stok"] = input("Stok Baru : ")

            ditemukan = True
            break

    if ditemukan:

        tulis_csv(
            FILE_BUKU,
            ["id_buku", "judul", "penulis", "stok"],
            data
        )

        print("Data berhasil diupdate")

    else:
        print("Data tidak ditemukan")


def hapus_buku():

    data = baca_csv(FILE_BUKU)

    id_cari = input("Masukkan ID Buku : ")

    data_baru = []

    ditemukan = False

    for buku in data:

        if buku["id_buku"] != id_cari:
            data_baru.append(buku)
        else:
            ditemukan = True

    if ditemukan:

        tulis_csv(
            FILE_BUKU,
            ["id_buku", "judul", "penulis", "stok"],
            data_baru
        )

        print("Data berhasil dihapus")

    else:
        print("Data tidak ditemukan")
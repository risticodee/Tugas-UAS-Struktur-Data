def cari_buku(data, keyword):
    hasil = []

    for buku in data:
        if keyword.lower() in buku['judul'].lower():
            hasil.append(buku)

    return hasil
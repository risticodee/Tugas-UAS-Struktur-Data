from collections import deque

antrian = deque()


def tambah_antrian(nama):
    antrian.append(nama)


def proses_antrian():
    if len(antrian) > 0:
        return antrian.popleft()

    return None


def lihat_antrian():
    return list(antrian)
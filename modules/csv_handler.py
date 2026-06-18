import csv
import os


def baca_csv(file):
    data = []

    if not os.path.exists(file):
        return data

    with open(file, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            data.append(row)

    return data


def tulis_csv(file, fieldnames, data):
    with open(file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for row in data:
            writer.writerow(row)
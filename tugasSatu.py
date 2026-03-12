# [ Tugas 1 - Pertemuan 1 ]
# Buatlah sebuah program sederhana dengan menggunakan bahasa pemrograman python yang mengimplemetasikan konsep:
# 1. Struktur kontrol
# 2. Struktur data
# 3. Library (minimal 2 library)
# Kemudian, upload source code program tersebut ke GitHub dengan nama repositori sebagai berikut: NIM-PraktikumKB-Pertemuan1

# [ Pengumpulan Tugas 1 - Pertemuan 1 ]
# https://bit.ly/KB-Pertemuan1 
# Deadline: 17 Maret 2026 23.59

import datetime
import statistics

# IMPLEMENTASI STRUKTUR DATA
# List = Dictionary buat nyimpen data programmer Blakasutha 
# Array 'izin_per_bulan' = data izin (dalam hari) selama 6 bulan berturut-turut
data_programmer_blakasutha = [
    {"nama": "Alan", "izin_per_bulan": [1, 0, 2, 1, 0, 0]}, # Total: 4 hari
    {"nama": "Apip", "izin_per_bulan": [0, 0, 0, 1, 0, 0]}, # Total: 1 hari
    {"nama": "Arlen", "izin_per_bulan": [2, 3, 1, 2, 4, 1]}, # Total: 13 hari
    {"nama": "Vincent", "izin_per_bulan": [0, 1, 0, 1, 0, 1]}, # Total: 3 hari
    {"nama": "Pancar", "izin_per_bulan": [0, 1, 0, 1, 0, 1]} # Total: 3 hari
]

print("--- Laporan Hasil Riset Programmer Berdasarkan Kehadiran ---")

# IMPLEMENTASI LIBRARY ke 1: datetime
waktu_sekarang = datetime.datetime.now() # ambil waktu pas program di run
print(f"Tanggal Cetak: {waktu_sekarang.strftime('%d-%m-%Y %H:%M:%S')}\n")

# IMPLEMENTASI STRUKTUR KONTROL (Perulangan)
for programmer in data_programmer_blakasutha:
    nama = programmer["nama"]
    daftar_izin = programmer["izin_per_bulan"]
    
    total_izin = sum(daftar_izin)
    
    # IMPLEMENTASI STRUKTUR KONTROL (Percabangan)
    if total_izin == 0:
        status = "Kinerja Sangat Baik (Sangat Layak menjadi SOTM)"
    elif total_izin <= 3:
        status = "Kinerja Baik (Layak menjadi SOTM)"
    elif total_izin <= 6:
        status = "Kinerja Cukup (Dipertimbangkan)"
    else:
        status = "Kinerja Kurang (Tidak Layak menjadi SOTM)"
        
    print(f"Nama programmer    : {nama}")
    print(f"Data Izin 6 Bulan  : {daftar_izin}")
    print(f"Total Izin         : {total_izin} Hari")
    print(f"Status             : {status}")
    print("-" * 55)
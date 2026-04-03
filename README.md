# H1D024018-PraktikumKB-Pertemuan1
Official documentation of my Artificial Intelligence progress. Dedicated to [Assistant's Name]—thank you for your guidance and feedback throughout the semester.

---

## Penjelasan Program: tugasSatu.py

### Overview
Program ini dibuat untuk menganalisis data kehadiran programmer di Blakasutha berdasarkan jumlah izin yang mereka ambil selama 6 bulan terakhir. Program ini akan mengklasifikasikan setiap programmer ke dalam kategori kinerja tertentu sebagai bahan pertimbangan untuk pemilihan "Star of The Month" (SOTM).

### Implementasi Konsep

#### 1. **Struktur Data**
Program menggunakan kombinasi **List of Dictionaries** untuk menyimpan data programmer:
```python
data_programmer_blakasutha = [
    {"nama": "Alan", "izin_per_bulan": [1, 0, 2, 1, 0, 0]},
    ...
]
```
- **List** sebagai container utama untuk menampung semua data programmer
- **Dictionary** untuk menyimpan atribut setiap programmer (nama dan data izin)
- **Array/List** di dalam dictionary untuk menyimpan history izin per bulan

#### 2. **Struktur Kontrol**
**a. Perulangan (Looping)**
```python
for programmer in data_programmer_blakasutha:
    ...
```
Digunakan untuk iterasi setiap data programmer agar bisa diproses satu per satu.

**b. Percabangan (Conditional)**
```python
if total_izin == 0:
    status = "Kinerja Sangat Baik"
elif total_izin <= 3:
    status = "Kinerja Baik"
...
```
Menentukan kategori kinerja berdasarkan total hari izin dengan logika:
- 0 hari = Sangat Baik
- 1-3 hari = Baik  
- 4-6 hari = Cukup
- >6 hari = Kurang

#### 3. **Library Python**
**a. datetime**
```python
import datetime
waktu_sekarang = datetime.datetime.now()
```
Digunakan untuk mengambil timestamp saat program dijalankan dan menampilkan tanggal cetak laporan.

**b. statistics** (imported namun belum dimanfaatkan)
```python
import statistics
```
Library ini sudah di-import untuk keperluan analisis statistik lanjutan seperti menghitung rata-rata atau median izin programmer.

### Output Program
Program akan menghasilkan laporan berisi:
- Timestamp pencetakan laporan
- Detail setiap programmer (nama, data izin bulanan, total izin, status kinerja)
- Klasifikasi kelayakan untuk menjadi SOTM
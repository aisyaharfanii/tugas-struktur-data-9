# 🔁 Rekursif & Backtracking

Program Python yang mengimplementasikan tiga algoritma rekursif dan backtracking klasik: **N-Queens**, **Knight's Tour**, dan **Knapsack**.

---

## 📋 Daftar Isi

- [Deskripsi](#deskripsi)
- [Algoritma](#algoritma)
- [Cara Menjalankan](#cara-menjalankan)
- [Contoh Output](#contoh-output)
- [Struktur Program](#struktur-program)

---

## Deskripsi

Program ini dibuat untuk mendemonstrasikan konsep **rekursi** dan **backtracking** melalui tiga permasalahan klasik dalam ilmu komputer. Setiap algoritma mencoba semua kemungkinan solusi secara sistematis dan mundur (*backtrack*) ketika menemui jalan buntu.

---

## Algoritma

### 1. 👑 N-Queens
Menempatkan N buah ratu pada papan catur berukuran N×N sedemikian rupa sehingga tidak ada dua ratu yang saling menyerang (tidak berada di baris, kolom, atau diagonal yang sama).

- **Input:** Ukuran papan `N`
- **Output:** Susunan papan dengan posisi ratu (`Q`) dan kotak kosong (`.`)
- **Pendekatan:** Backtracking baris per baris

### 2. ♞ Knight's Tour
Mencari jalur bagi sebuah kuda catur untuk mengunjungi setiap kotak pada papan 8×8 tepat satu kali.

- **Input:** Posisi awal kuda `(x, y)` (0–7)
- **Output:** Papan 8×8 berisi urutan langkah kuda
- **Pendekatan:** Backtracking dengan 8 kemungkinan gerakan kuda

### 3. 🎒 Knapsack
Mencari kombinasi barang dari daftar yang tersedia agar totalnya tepat sama dengan kapasitas yang diberikan.

- **Input:** Kapasitas knapsack
- **Daftar barang tersedia:** `[2, 5, 6, 9, 12, 14, 20]`
- **Output:** Kombinasi barang dan total bobotnya
- **Pendekatan:** Rekursi dengan dua pilihan (ambil / tidak ambil)

---

## Cara Menjalankan

### Prasyarat

- Python 3.x

### Langkah

```bash
# Clone repository
git clone https://github.com/username/rekursif-backtracking.git
cd rekursif-backtracking

# Jalankan program
python rekursif.py
```

### Menu Program

```
===== PILIH PROGRAM =====
1. N-Queens
2. Knight's Tour
3. Knapsack
0. Keluar
```

---

## Contoh Output

### N-Queens (N = 4)

```
Masukkan ukuran papan N: 4

Solusi ditemukan:

. Q . .
. . . Q
Q . . .
. . Q .
```

### Knight's Tour (mulai dari 0, 0)

```
Masukkan posisi awal x (0-7): 0
Masukkan posisi awal y (0-7): 0

Solusi Knight's Tour:

 0 59 38 33 30 17  8 63
37 34 31 60  9 62 29 16
58  1 36 39 32 27 18  7
35 48 41 26 61 10 15 28
42 57  2 49 40 23  6 19
47 52 45 54 25 20 11 14
56 43 50  3 22 13 24  5
51 46 53 44 55  4 21 12
```

### Knapsack (kapasitas = 26)

```
Masukkan kapasitas knapsack: 26

Kombinasi barang ditemukan:
[2, 5, 9, 14]
Total: 26
```

---

## Struktur Program

```
rekursif.py
├── menu()                  # Tampilan menu utama
│
├── N-Queens
│   ├── aman()              # Cek apakah posisi aman
│   ├── solve_nqueen()      # Rekursi backtracking
│   └── program_nqueen()    # Handler input/output
│
├── Knight's Tour
│   ├── valid()             # Cek apakah langkah valid
│   ├── knight_tour()       # Rekursi backtracking
│   └── program_knight_tour()
│
├── Knapsack
│   ├── knapsack()          # Rekursi ambil/tidak ambil
│   └── program_knapsack()
│
└── Loop utama              # Pemilihan menu
```

---

## Konsep yang Digunakan

| Konsep | Penjelasan |
|--------|------------|
| **Rekursi** | Fungsi memanggil dirinya sendiri untuk memecah masalah |
| **Backtracking** | Mundur ke langkah sebelumnya jika solusi tidak ditemukan |
| **Pruning** | Memangkas cabang pencarian yang tidak valid sejak awal |

---

## Lisensi

Proyek ini dibuat untuk keperluan pembelajaran. Bebas digunakan dan dimodifikasi.

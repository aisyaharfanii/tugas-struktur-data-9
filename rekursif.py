# =====================================
# PROGRAM REKURSIF DAN BACKTRACKING
# =====================================
# 1. N-Queens
# 2. Knight's Tour
# 3. Knapsack
# =====================================


# =====================================
# MENU
# =====================================

def menu():
    print("\n===== PILIH PROGRAM =====")
    print("1. N-Queens")
    print("2. Knight's Tour")
    print("3. Knapsack")
    print("0. Keluar")


# =====================================
# 1. N-QUEENS
# =====================================

def aman(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueen(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if aman(board, row, col, n):
            board[row][col] = 1

            if solve_nqueen(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


def program_nqueen():
    n = int(input("Masukkan ukuran papan N: "))

    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_nqueen(board, 0, n):
        print("\nSolusi ditemukan:\n")

        for row in board:
            for cell in row:
                if cell == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("Tidak ada solusi")


# =====================================
# 2. KNIGHT'S TOUR
# =====================================

n_kuda = 8

langkah_x = [2, 1, -1, -2, -2, -1, 1, 2]
langkah_y = [1, 2, 2, 1, -1, -2, -2, -1]


def valid(x, y, board):
    return 0 <= x < n_kuda and 0 <= y < n_kuda and board[x][y] == -1


def knight_tour(x, y, langkah, board):
    if langkah == n_kuda * n_kuda:
        return True

    for i in range(8):
        next_x = x + langkah_x[i]
        next_y = y + langkah_y[i]

        if valid(next_x, next_y, board):
            board[next_x][next_y] = langkah

            if knight_tour(next_x, next_y, langkah + 1, board):
                return True

            board[next_x][next_y] = -1

    return False


def program_knight_tour():
    x = int(input("Masukkan posisi awal x (0-7): "))
    y = int(input("Masukkan posisi awal y (0-7): "))

    board = [[-1 for _ in range(n_kuda)] for _ in range(n_kuda)]

    board[x][y] = 0

    if knight_tour(x, y, 1, board):
        print("\nSolusi Knight's Tour:\n")

        for row in board:
            for cell in row:
                print(f"{cell:2}", end=" ")
            print()
    else:
        print("Tidak ada solusi")


# =====================================
# 3. KNAPSACK
# =====================================

barang = [2, 5, 6, 9, 12, 14, 20]


def knapsack(index, total, pilihan, kapasitas, hasil):
    if total > kapasitas:
        return False

    if total == kapasitas:
        hasil.extend(pilihan)
        return True

    if index >= len(barang):
        return False

    if knapsack(index + 1,
                 total + barang[index],
                 pilihan + [barang[index]],
                 kapasitas,
                 hasil):
        return True

    if knapsack(index + 1,
                 total,
                 pilihan,
                 kapasitas,
                 hasil):
        return True

    return False


def program_knapsack():
    kapasitas = int(input("Masukkan kapasitas knapsack: "))

    hasil = []

    if knapsack(0, 0, [], kapasitas, hasil):
        print("\nKombinasi barang ditemukan:")
        print(hasil)
        print("Total:", sum(hasil))
    else:
        print("Tidak ada kombinasi yang cocok")


# =====================================
# PROGRAM UTAMA
# =====================================

while True:
    menu()

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        program_nqueen()

    elif pilihan == "2":
        program_knight_tour()

    elif pilihan == "3":
        program_knapsack()

    elif pilihan == "0":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
import csv
import time
from tabulate import tabulate

# ===============================
# MEMBACA DATA CSV
# ===============================
data = []

with open("StudentsPerformance.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=';')
    header = reader.fieldnames
    for row in reader:
        data.append(row)

# Ambil 50 data pertama
data = data[:50]

# Ambil nilai matematika (data numerik)
math_scores = [int(row['math score']) for row in data]

# ===============================
# TAMPILKAN DATA AWAL
# ===============================
print("\nDATA NILAI MATEMATIKA SEBELUM SORTING:")
print(math_scores)

# ===============================
# ALGORITMA SORTING
# ===============================
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ===============================
# MENU SORTING
# ===============================
print("\nPILIH ALGORITMA SORTING:")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Selection Sort")
print("4. Quick Sort")
print("5. Merge Sort")

pilihan = input("Masukkan pilihan (1-5): ")

start = time.time()

if pilihan == "1":
    sorted_data = bubble_sort(math_scores)
elif pilihan == "2":
    sorted_data = insertion_sort(math_scores)
elif pilihan == "3":
    sorted_data = selection_sort(math_scores)
elif pilihan == "4":
    sorted_data = quick_sort(math_scores)
elif pilihan == "5":
    sorted_data = merge_sort(math_scores)
else:
    print("Pilihan tidak valid")
    exit()

end = time.time()

# ===============================
# OUTPUT HASIL SORTING
# ===============================
print("\nDATA NILAI MATEMATIKA SETELAH SORTING:")
print(sorted_data)
print(f"Waktu eksekusi sorting: {end - start:.6f} detik")

# ===============================
# BINARY SEARCH
# ===============================
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ===============================
# SEARCHING
# ===============================
target = int(input("\nMasukkan nilai matematika yang dicari: "))
index = binary_search(sorted_data, target)

if index != -1:
    print(f"Nilai {target} ditemukan pada indeks ke-{index}")
else:
    print("Nilai tidak ditemukan")
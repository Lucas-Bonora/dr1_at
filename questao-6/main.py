import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def measure_time(arr):
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    return end_time - start_time

list_1000 = [random.uniform(1, 1000) for _ in range(1000)]
time_1000 = measure_time(list_1000)
print(f"Tempo de execução para 1.000 elementos: {time_1000:.6f} segundos")

list_10000 = [random.uniform(1, 1000) for _ in range(10000)]
time_10000 = measure_time(list_10000)
print(f"Tempo de execução para 10.000 elementos: {time_10000:.6f} segundos")

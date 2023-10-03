from typing import List

def binary_search(arr: List[int], number: int) -> int:

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# На вход подаем целочисленный массив
arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]

print(f"Исходный массив: {arr}")
number = int(input("Введите искомый элеммент: "))
result = binary_search(arr, number)

if result == -1:
    print("Искомый элемент нет в массиве")
else:
    print(f"Искомый элемент: {number} найден по индексу: {result}")
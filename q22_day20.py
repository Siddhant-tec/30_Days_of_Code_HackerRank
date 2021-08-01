n = int(input())
a = [int(x) for x in input().split(" ")]


def bubble_sort():
    count = 0
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
            if count == 0:
                break
    print("Array is sorted in", count, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])


bubble_sort()

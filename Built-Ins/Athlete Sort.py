import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
    k = int(input().strip())

    sorted_arr = sorted(arr, key=lambda x: x[k])
    for row in sorted_arr:
        print(' '.join(str(y) for y in row))


# N, M = map(int, input().split())
#
# # taking for rows
# rows = [input() for _ in range(N)]
#
# # taking input from user
# K = int(input())#
# # sorting using sorted function
# for row in sorted(rows, key=lambda row: int(row.split()[K])):
#     print(row)
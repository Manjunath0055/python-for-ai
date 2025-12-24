# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
# print(result)

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# my_list = [[i,j,k]for i in range(x+1) for j in range (y+1) for k in range(z+1) if (i+j+k) != n]

# n = int(input())
# arr = map(int, input().split())
# arr = list(arr)
# arr.remove(max(arr))
# print(max(arr))
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
up_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    my_list = [name, score]
    up_list.append(my_list)
my_dict = dict(up_list)
val_list = sorted(set(my_dict.values()))
print(val_list)
second_lowest = val_list[1]
for name, score in sorted(my_dict.items()):
    if score == second_lowest:
        print(name) 
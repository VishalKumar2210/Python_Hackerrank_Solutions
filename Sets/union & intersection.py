# ***************add****************************

n = int(input())
Country = set()
for i in range(n):
    Country.add(input())
print(len(Country))

# ***************union****************************

n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)
print(len(s1.union(s2)))


# ***************intersection****************************


n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)
print(len(s1.intersection(s2)))

# ***************difference****************************

n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)
print(len(s1.difference(s2)))

# ***************symmetric_difference****************************

n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)
print(len(s1.disymmetric_difference(s2)))

# ***************set_add****************************

n = int(input())
Country = set()
for i in range(n):
    Country.add(input())
print(len(Country))
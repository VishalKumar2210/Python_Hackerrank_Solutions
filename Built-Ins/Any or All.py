N = int(input())
numbers = list(map(int, input().split()))
print(all([x > 0 for x in numbers]) and any([str(x) == str(x)[::-1] for x in numbers]))



# # importing the module
# from string import ascii_lowercase, ascii_uppercase
#
# # sorting accordingly
# sortkey = ascii_lowercase + ascii_uppercase + "1357902468"
#
# # taking input from user
# x = input()
#
# # printing sorted string
# print(*map(lambda y: y * x.count(y), sortkey), sep='')
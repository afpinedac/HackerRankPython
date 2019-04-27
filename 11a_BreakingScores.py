f = open('./files/test.txt', 'r')

lines = f.readlines()

for l in lines:
    print(l)

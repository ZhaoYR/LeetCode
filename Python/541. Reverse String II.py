s = input("s=:")
k = int(input("k=:"))
x = s[k-1::-1]
i = 1
j = k - 1
print('init x=',x)
print(s[2::-1]+s[3:6:1]+s[8:5:-1]+s[9:12:1]+s[14:11:-1])
zhiShu = 1
while i < len(s):
    if i % 2 == 0:
        x = x + s[i * k + j:(i-1) * k + j:zhiShu]
        # print(i * k + j,(i-1) * k + j,zhiShu)
    elif i % 2 != 0:
        x = x + s[i * k:(i+1) * k:zhiShu]
        # print(i * k + 1, (i - 1) * k + j, zhiShu)
    i = i + 1
    zhiShu = (-1)**(i-1)
print(x)


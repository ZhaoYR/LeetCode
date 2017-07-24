'''
557. Reverse Words in a String III
'''
s = input("s=:")

x = s.split()
j = []
k = ' '
for i in x:
    j .append( i[::-1])
j = k.join(j)

print(j)
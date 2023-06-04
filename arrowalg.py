list = []
binr =[]

num = input("Input: ")
for n in num:
    list.append(int(n))
for a, value in enumerate(list[0:-1]):
    b = list[a]
    c = list[a+1]
    if b>c:
        binr.append("1")
    else:
        binr.append("0")
with open("output_binr.txt", 'w') as arc:
    text = "".join(str(binr))
    arc.write(texto)

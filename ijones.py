with open("input.txt", 'r') as input:
    w, h = map(lambda x:int(x), input.readline().split())
    a = []
    for row in range(h):
        b = []
        line = input.readline()
        for j in range(w):
            b.append(line[j])
        a.append(b)

counter = []
dict = {}
for i in range(h):
    b = []
    for j in range(w):
        b.append(0)
        dict.update({a[i][j]:0})
    counter.append(b)

for row in range(h):
    counter[row][0] = 1
    dict.update({a[row][0]:dict.get(a[i][0])+1})

print(str(dict))


for col in range(1, w):
    row_dict = {}
    for row in range(h):
        counter[row][col] += dict.get(a[row][col])
        if(a[row][col]!=a[row][col-1]):
            counter[row][col] += counter[row][col-1]

        if not (a[row][col] in row_dict.keys()):
            row_dict.update({a[row][col]:dict.get(a[row][col])+counter[row][col]})
            print(str(dict.get(a[row][col])+counter[row][col]))
        else:
            row_dict.update({a[row][col]:row_dict.get(a[row][col])+counter[row][col]})

    print(str(row_dict))
    for key in row_dict.keys():
        dict.update({key:row_dict.get(key)})

print(str(dict))

with open('output.txt', 'w+') as output:
    for i in range(h):
        for j in range(w):
            output.write(str(counter[i][j])+' ')
        output.write('\n')
    output.write('(1, w):'+ str(counter[0][w-1])+'\n')
    output.write('(h, w):'+ str(counter[h-1][w-1])+'\n')
    if h==1:
        output.write(str(counter[0][w-1]))
    else:
        output.write(str(counter[0][w-1]+counter[h-1][w-1]))

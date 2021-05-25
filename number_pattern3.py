"""
printing column wise

1
12
123

"""

row = 3;
for i in range(row):
    for j in range(i+1):
        print(j+1,end=" ");
    print();

"""
printing column wise

123
12
1

"""

row = 3;
col = 3;
for i in range(row):
    for j in range(col):
        print(j+1,end=" ");
    
    print();
    col = col-1;

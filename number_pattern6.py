"""
printing row wise

111
22
3

"""

row = 3;
col = 3;
for i in range(row):
    for j in range(col):
        print(i+1,end=" ");
    
    print();
    col = col-1;

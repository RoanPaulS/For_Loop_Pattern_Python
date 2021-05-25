"""


   1
  121
 12321
 

"""

row = 5;
col = 0;
sp = 4;



for i in range(row):
    for j in range(sp):
        print(" ",end=" ");
    for k in range(col+1):
        print(k+1,end=" ");
    for l in range(col):
        print(col-l,end=" ");
    print();
    sp = sp-1;
    col = col+1;
    

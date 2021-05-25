"""
******#
****###
***####
**#####
*######

"""


row = 5;
col = 5;
sp = 0;

for i in range(row): # 0 to 4
    for j in range(col): # 0 to 4
        print(" ",end=" ");
    for k in range(i+1): # 0 to (i+1)
        print("#",end=" ");

    print();
    col = col-1;

word = "payilagam";
length = len(word); # length = 9;

no_of_times = length  # no_of_times = 9;

"""

for letter in range(length):
    print(word[letter],end=" ");
print();
length = length -1;

for letter in range(length):
    print(word[letter],end=" ");
print();
length = length -1;

for letter in range(length):
    print(word[letter],end=" ");
print();
length = length -1;

for letter in range(length):
    print(word[letter],end=" ");
print();
length = length -1;

"""
 # in below program repeat == row and letter == column


for repeat in range(no_of_times): # it will repeat (0 to 8) 9 times
    for letter in range(length): # length = 9  #8 #7 ....#1
        print(word[letter],end="");

    print();
    length = length -1;

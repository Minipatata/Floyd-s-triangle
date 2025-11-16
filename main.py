#Write a program to demonstrate a Floyd triangle pattern?
#1
#12
#123
#1234
#12345
number_numbers=int(input("Can you please enter any number for a Floyd triangle?"))
for j in range(1,number_numbers):
    for i in range(1,j+1):
        print(i,end=" ")
    print()
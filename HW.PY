# exercice 8
'''
for n in range (200,1,-1):
    print(n)

# exercice 9
for n in range (0,101,7):
    print(n)


# exercice 10

while True:
        x=int(input("Input number: "))
        if(x==-1):
            print("exit")
            break


# exercice 11

x = int(input("Input number: "))
sum=1
for n in range (1,x+1,1):
    sum=sum*n
print(sum)
'''
str_numb=[1,2,3,4,5]
#print(str_numb)
new_str=0
count=-1
while True:
    numb_ = int(input("input numb : "))
    count = -1

    for x in str_numb:
        count = count + 1
        print(count)
        print(str_numb)

        if (x == numb_):
            del str_numb[count]
            break
        else:
            continue
    if(len(str_numb)==0):
        print('stop')
        break




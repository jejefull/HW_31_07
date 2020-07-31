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
str_numb=[5,6,7,8,9]
count=0
count_true=0
#print(str_numb)
while True:
    numb_ = int(input("input numb : "))
    count=count+1
    if numb_<1 or numb_>60:
        print("you enter a wrong number")
        continue
    if count==10:
        print("you try too many time ->bye bye ")
        break
    if numb_ in str_numb:
        count_true=count_true+1
        if count_true==2:
            print("you are very good")
            break
        str_numb.remove(numb_)
        print(str_numb)
    else:
        print(str_numb)
        continue

    if(len(str_numb)==0):
        print('stop')
        break

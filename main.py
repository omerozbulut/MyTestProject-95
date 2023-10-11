my_list = [10, 20, 30, 40]

for num in my_list:
    print(num * 2 )

print("test")
for num in my_list:
    if num %8 ==0:
        print(num, " : 8 in katidir")


#yaşi integer olarak dogru girene kadar sormasi icin
while True:
    try:
        myAge = int(input("enter age :"))
        print(myAge * 2)
        break
    except:
        print("enter your age !!!")
    else:
        print("else executed")
    finally:
        print("finanlly")


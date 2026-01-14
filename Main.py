#Credit Card Validator Project


sum_odd=0
sum_even=0
total=0

card_num=input("Enter a credit card number: ")
card_num=card_num.replace("-","")
card_num=card_num.replace(" ","")
card_num=card_num[::-1]
print(card_num)

for x in card_num[::2]:
    sum_odd +=int(x)

for x in card_num[1::2]:
    x=int(x)*2
    if x>=10:
        sum_even+=(1+(x%10))
    else:
        sum_even+= x

total=sum_even+sum_odd

if total%10==0:
    print("Valid Credit Card ")
else:
    print("Invalid Credit Card ")



a=int(input("enter the 3 digit number="))
print("the reverse of the digits is=",a%10 * 100 + (a//10)%10 * 10 + a//100)
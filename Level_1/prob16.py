a=int(input("enter the 4 digit number="))
print("the reverse of the first two digits is=",((a//100)%10)*1000+a//1000*100+(a//10)%10+ a%10 * 10 )
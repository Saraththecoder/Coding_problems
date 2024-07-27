print("***sarath's mini calculator***")
print("1.Addition(+)\n2.Subraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Module Division(%)")
n=int(input("   Choose the Option:"))
def calci(a,b):
 if n==1:
     return print("The sum of two numbers is:",a+b)
 elif n==2:
       return print("The difference of two numbers is:",a-b)
 elif n==3:
      return print("The multiplication  of two numbers is:",a*b)
 elif n==4:
      return  print("The division of two numbers is:",a/b)
 elif n==5:
     return print("The module division of two numbers is:",a%b)
 else:
     return print("Out of range")
a=int(input("Enetr the first number:"))
b=int(input("Enetr the second number:"))
calci(a,b)
while(True):
    proceed=int(input("Do u want to try again(Yes(1)/No(0):)"))
    if proceed==1:
     print("1.Addition(+)\n2.Subraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Module Division(%)")
     n=int(input("   Choose the Option:"))
     a=int(input("Enetr the first number:"))
     b=int(input("Enetr the second number:"))
     calci(a,b)
    elif proceed==0:
      print("tq for reaching us")
      break
    else:
       print("Enter valid number")
    


    

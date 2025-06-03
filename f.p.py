bal=100
card=int(input("enter the pin number"))
if(card<=1000):
    print("the card is accessied");
    display=int(input("enter the number ,1 for bal check,2 for wd"))
if(display==1):
      print("balance=",bal);
else:
    print("processing your tranction....")
while(bal>0):
    wd=int(input("enter the withdraw amount"))
    bal=bal-wd
    print("the withdraw amountis",wd);
    print("the balance amount is",bal);
if (bal==0):
  print("insuffcient fund")

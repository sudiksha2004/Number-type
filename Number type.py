num=int(input("Accept a number"))
print("""
***MENU***
1.Prime Number
2.Factorial
3.Armstrong Number
4.Perfect Number
5.Happy Number
6.Automorphic Number
7.Special Number
8.Binary Equivalent 
9.Magic Number
""")

choice=int(input("Enter a number from the above eg. 1 :"))
#Prime number
if choice==1:
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
       print(num,"is not a prime number")

#factorial
elif choice==2 :
    factorial=1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print("The factorial of",num,"is",factorial)

   
elif choice==3:
    s=0
    n=num
    for i in range (1,n):
           if n==0:
               break
           #print("value of n",n)
           r=n%10
           s=s+(r*r*r)
           n=n//10

    if s==num :
        print(num,"is an Armstrong number")
    else :
        print(num,"is not an Armstrong number")

#perfect number
elif choice==4:    
    s=0
    a=1
    while(a<num):
         r=num%a
         if r==0:
             s+=a
         a+=1
    if (s==num):
         print (num,"is a Perfect number ")
    else :
         print (num,"is not a Perfect number")

#happy number
elif choice==5:
    while num!=1 :
            n=num
            temp=0
            while n!=0:
                rem=n%10
                temp=temp+(rem**2)
                n=n//10
            num=temp
            if num==4:#to break the loop if it is not a happy number
                break    
    if num==1:  
        print ("It is a Happy number")
    else :
        print("It is not a Happy number")
#automorphic number
elif choice==6:
    sr=num**2
    n=len(str(num))
    last=sr % pow(10,n)
    if last==num:
        print(num,"is an Automorphic Number")
    else:
        print(num,"is not an Automorphic Number")
#special number
elif choice==7:
         w=num
         s=0
         while(w>0):
             dig=w%10
             i=1
             fact=1
             while(i<=dig):
                 fact*=i
                 i+=1
             s+=fact
             w=w//10
         if (num==s):
            print(num,"Is a special number")
         else:
            print(num,"Is not a special number")        
#binary equivalent            
elif choice==8:
          a=[]
          while(num>0):
              dig=num%2
              a.append(dig)
              num//=2
          a.reverse()
          print("Binary Equivalent is:")
          for i in a:
              print(i,end="")
          print()
#magic number          
elif choice==9:
        s=0
        no=num
        for i in range(1,num):
            if num<9:
                break;
            if num>9:
              n=num
              s=0
              while(n>0):
                    r=n%10
                    s=s+r
                    n//=10
              num=s
        if s==1:
            print(no,"is a Magic Number")
        else:
            print(no,"is not magic number")
elif choice>9:
        print("Wrong choice!!!Please try again")
    

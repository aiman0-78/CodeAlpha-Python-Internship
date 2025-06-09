def fibonacci(x): #function defination
    #base veriable of fibonacci sequence
    a=0
    b=1
    while x<0: #when user enter nagitive number
            x = int(input("Please Enter a positive number: \n")) #if number nagitive for again enter number
            
    print("The fibonacci squence till ",x," is ")
    if x==0: #when user enter 0
        print(a)
    elif x==1: #when user enter 1
        print(a,b)
    else: #when user enter positive number greater than 1 
        print(a)
        print(b)
        for n in range(2,x+1): #loop from index 2 to x+1
            c=a+b        #adding two preceding numbers,
            a=b          #give value of b to a
            b=c          #give value of c to b
            print(b) #print sequence
x=int(input("Enter how many terms you want in your fibanocci sequence : \n")) #for taking input number from user
fibonacci(x) #function calling
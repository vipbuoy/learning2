def collatz(number):
        if number%2==0:
            print(number//2)
            return number//2
        else:
            print(3*number+1)
            return (3*number+1)
    
number=0
number1=0
print('Enter number:')
while number1!= 1:
    try:
       number=int(input())
       number1=collatz(number)    
    except ValueError:
       print('Don\'t check this program!, enter integer value...')

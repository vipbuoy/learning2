def collatz(number):
    try:
        if number%2==0:
            print(number//2)
            return number//2
        else:
            print(3*number+1)
            return (3*number+1)
    except ValueError:
        print('Don\'t check this program!, enter integer value...')
number=0
number1=0
print('Enter number:')
while number1!= 1:
    number=int(input())
    number1=collatz(number)    

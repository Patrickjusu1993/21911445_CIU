#dseral@gmail.com


#a program that get input from user that show how many iteration needed to find 
#out if a number is prime or not. If the number is not prime (composite) 
#it gives the factor(s) of the given number.


# Solution

print("{Patrick Jusu 21911445}")

number = int(input("Please input a number:"))

ite = 3

divisors = [i for i in range(2, number+1) if number % i == 0]
it = number - 1

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is composite number and factors are", divisors)
            print("With 1st method number of iteration is", it)
            print("With 2nd method number of iteration is", ite)
            break
    else:
        print(number, "is prime number and factors are", divisors)
        print("With 1st method number of iteration is", it)
        print("With 2nd method number of iteration is", ite)

else:
    print(number, "is neither prime nor composite and factor is", divisors)

    input("press enter to close")


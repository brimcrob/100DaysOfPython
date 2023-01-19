# Write your code below this line 👇
def prime_checker(number):
    if number == 1 or number == 2 or number == 3:
        print("It's a prime number")
    else:
        i = number - 1
        while i > 1:
            if number % i == 0:
                print("It's not a prime number")
                return
            i = i - 1
        print("It's a prime number")
        return


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

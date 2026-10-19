# 26th github project --> FizzBuzz
print('----------FizzBuzz----------')
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def main():
    try:
        n = int(input("How many numbers? "))
        fizzbuzz(n)
    except ValueError:
        print("Enter a whole number.")



main()
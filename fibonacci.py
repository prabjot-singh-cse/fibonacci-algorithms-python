def fibonacci():
    while True:
        print("\nTo exit the program, enter -1")
        x = int(input("Enter the number of terms: "))

        if x == -1:
            print("You successfully exited the program.")
            break

        if x <= 0:
            print("Please enter a positive number.")
            continue

        if x == 1:
            print("Fibonacci Series: 0")
            continue

        fib = [0, 1]

        for i in range(2, x):
            fib.append(fib[-1] + fib[-2])

        print("Fibonacci Series:", *fib)


fibonacci()
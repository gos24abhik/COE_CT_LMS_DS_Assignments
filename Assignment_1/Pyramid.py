def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
        
N_rows = int(input("Enter the number of input:"))
pyramid(N_rows)
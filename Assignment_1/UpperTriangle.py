def upper_triangular(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * i)
        
N_rows = int(input("Enter the number of input:"))
upper_triangular(N_rows)
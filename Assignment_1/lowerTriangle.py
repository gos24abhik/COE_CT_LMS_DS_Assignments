def lower_triangular(n):
    for i in range(1, n + 1):
        print("* " * i)
        
N_rows = int(input("Enter the number of input:"))
lower_triangular(N_rows)
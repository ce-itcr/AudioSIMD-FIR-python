import numpy as np

def fir_filter(x, b):
    Nx = len(x)
    Nb = len(b)
    Ny = Nx + Nb - 1  # Output length

    y = np.zeros(Ny, dtype=np.int16)  # Initialize the output

    for n in range(Ny):
        for k in range(max(0, n - Nx + 1), min(n, Nb)):
            y[n] += np.round(b[k] * x[n - k] * 2**8)

    return y

def main():
    # Define an input vector x and coefficients b in Q7.8 format
    x = np.random.randint(-128, 127, size=32) / 2**8  # Input vector x
    b = np.random.randint(-128, 127, size=16) / 2**8  # Filter coefficients b

    # Case a: The number of coefficients is equal to N
    y_a = fir_filter(x, b)

    # Case b: The number of coefficients is less than N
    b_b = np.random.randint(-128, 127, size=8) / 2**8  # Filter coefficients b for case b
    y_b = fir_filter(x, b_b)

    # Case c: The number of coefficients is greater than N and not a multiple of N
    b_c = np.random.randint(-128, 127, size=24) / 2**8  # Filter coefficients b for case c
    y_c = fir_filter(x, b_c)

    # Display results
    print("Result of case a:", y_a)
    print("Result of case b:", y_b)
    print("Result of case c:", y_c)

if _name_ == "_main_":
    main()
# File: fir_filter.py
# Author: @angelortizv
# Date: 03/03/2024
# Description: This Python program implements an FIR filter using NumPy vectorization and loop unrolling
#              to enhance performance. It compares three different cases based on the SIMD vector size (N = 16).


import numpy as np

def fir_filter_vectorized(x, b):
    Nx = len(x)
    Nb = len(b)
    Ny = Nx + Nb - 1  # Output length

    y = np.zeros(Ny, dtype=np.int16)  # Initialize the output

    for n in range(Ny):
        # Vectorization of the weighted sum calculation
        y[n] = np.round(np.sum(b[:min(n+1, Nb)] * x[n - min(n, Nx) : n - min(n, Nx) + min(n+1, Nb)]) * 2**8)

    return y

def main():
    x = np.random.randint(-128, 127, size=32) / 2**8  # Input vector x
    b = np.random.randint(-128, 127, size=16) / 2**8  # Filter coefficients b

    # Case a: The number of coefficients is equal to N
    y_a = fir_filter_vectorized(x, b)

    # Case b: The number of coefficients is less than N
    b_b = np.random.randint(-128, 127, size=8) / 2**8  
    y_b = fir_filter_vectorized(x, b_b)

    # Cases c: The number of coefficients is greater than N and not a multiply of N
    b_c = np.random.randint(-128, 127, size=24) / 2**8 
    y_c = fir_filter_vectorized(x, b_c)

    # Display results
    print("Result of case a:", y_a)
    print("Result of case b:", y_b)
    print("Result of case c:", y_c)

if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

def power_method(A, q0, k):
    """Evaluates k steps of the power iteration with starting vector q0 for the matrix A, returning a vector of eigenvalue iterates."""
    lambda_iterates = np.zeros(k, dtype=np.complex128)
    q = q0
    for i in range(k):
        z = A @ q  # Simplified matrix-vector multiplication
        q = z / np.linalg.norm(z)  # Normalizing q
        lambda_iterates[i] = np.vdot(q, A @ q)  # Using vdot for complex conjugate dot product
    return lambda_iterates

def companion_matrix(a):
    """Generate the companion matrix for a given polynomial represented by its coefficients."""
    # normalise the leading coefficient
    a = np.complex128(a)
    a = a / a[-1]
    n = len(a) - 1
    C = np.zeros((n, n), dtype=np.complex128)
    # Set the last column of C to be the negated coefficients (except the leading one)
    C[:, -1] = -np.array(a[:-1])
    # Set the subdiagonal elements to 1
    np.fill_diagonal(C[1:], 1)
    return C

def wilkinson_polynomial_coefficients(n):
    """Generate the coefficients of the Wilkinson polynomial of degree n"""
    def poly_multiply(poly1, poly2):
        """Multiply two polynomials represented as lists of coefficients."""
        result = [0] * (len(poly1) + len(poly2) - 1)
        for i, coef1 in enumerate(poly1):
            for j, coef2 in enumerate(poly2):
                result[i + j] += coef1 * coef2
        return result
    # Start with the polynomial x - 1
    poly = [1, -1]
    for i in range(2, n + 1):
    # Multiply the current polynomial by x - i using integer arithmetic
        poly = poly_multiply(poly, [1, -i])
    return poly

# Compute eigenvalues and plot
k = 200
i_max = 2
lambda_iterates = np.zeros((k, i_max), dtype=np.complex128)
for i in range(1, i_max):
    # Parameters and initial setup
    n = 5 * i
    A = companion_matrix(wilkinson_polynomial_coefficients(n))
    q0 = np.random.rand(n) + 1j * np.ones(n)  # Complex starting vector
    lambda_iterates[:, i] = power_method(A, q0, k)
    plt.semilogy(np.abs(lambda_iterates[:, i] - n), label=f"n = {n}")
    print(f"lambda_{i} = {lambda_iterates[-1, i]}")
plt.ylabel('$|\lambda_1^{(k)} - \lambda_1|$')
plt.xlabel('Iteration $j$')
plt.legend()
plt.show()

print(np.linalg.eig(A)[0])
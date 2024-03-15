import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import lu, solve_triangular

def power_method(A, z, k):
    lambda_iterates = np.zeros(k, dtype=np.complex128)
    for i in range(k):
        q = z / np.linalg.norm(z)
        lambda_iterates[i] = np.vdot(q, A @ q)
        z = A @ q
    return lambda_iterates

def inverse_iteration(A, z, sigma, k):
    lambda_iterates = np.zeros(k, dtype=np.complex128)
    n = A.shape[0]
    P, L, U = lu(A - sigma * np.eye(n, dtype=A.dtype))

    def applyMat(x):
        """Computes (A - sigma I)^{-1} x = (PLU)^{-1} x = U^{-1} L^{-1} P^T x"""
        return solve_triangular(U, solve_triangular(L, np.dot(P, x), lower=True))

    for i in range(k):
        q = z / np.linalg.norm(z)
        lambda_iterates[i] = np.vdot(q, A @ q)
        z = applyMat(q)  # (A - sigma I)^{-1} q

    return lambda_iterates

def rayleigh_quotient_iteration(A, z, sigma, k):
    lambda_iterates = np.zeros(k, dtype=np.complex128)
    n = A.shape[0]

    lambda_iterates[0] = sigma
    q = z / np.linalg.norm(z)
    for i in range(k):
        try:
            z = np.linalg.solve(A - sigma * np.eye(n, dtype=np.complex128), q)
        except:
            break
        q = z / np.linalg.norm(z)
        lambda_iterates[i] = np.vdot(q, A @ q)
        if np.abs(lambda_iterates[i] - sigma) < 0.001 * sigma:
            sigma = lambda_iterates[i]
        else:
            sigma = (1.0 + 0.001 * np.sign(lambda_iterates[i] - sigma)) * sigma

    return lambda_iterates

# Parameters and initial setup
n, k = 100, 400
A = np.diag(1.0 + np.arange(n, dtype=np.complex128))
z = np.ones(n)

# Compute eigenvalues and plot
lambda_iterates = np.zeros((k, 3), dtype=np.complex128)
lambda_iterates[:, 0] = power_method(A, z, k)
lambda_iterates[:, 1] = inverse_iteration(A, z, 1.8 * n, k)
lambda_iterates[:, 2] = rayleigh_quotient_iteration(A, z, 1.8 * n, k)
plt.semilogy(np.abs(lambda_iterates[:, 0] - n), label=f"Power")
plt.semilogy(np.abs(lambda_iterates[:, 1] - n), label=f"Inverse")
plt.semilogy(np.abs(lambda_iterates[:, 2] - n), label=f"Rayleigh")
print(lambda_iterates[-1, 0])
print(lambda_iterates[-1, 1])
print(lambda_iterates[-1, 2])
plt.ylabel('$|\lambda_1^{(k)} - \lambda_1|$')
plt.xlabel('Iteration $j$')
plt.legend()
plt.show()

import numpy as np
import scipy.linalg

def identify_system_parameters(input_data, output_data, system_order):
    """
    Identify system parameters using QR decomposition.

    Args:
    input_data (np.ndarray): Input data to the system.
    output_data (np.ndarray): Output data from the system.
    system_order (int): Order of the system.

    Returns:
    np.ndarray: Identified system parameters.
    """
    # Construct the matrix for the least squares problem
    N = len(input_data)
    A = np.zeros((N - system_order, system_order))
    for i in range(system_order, N):
        A[i - system_order, :] = input_data[i - system_order:i][::-1]

    # Solve the least squares problem using QR decomposition
    b = output_data[system_order:]
    Q, R = np.linalg.qr(A)
    parameters = scipy.linalg.solve_triangular(R, np.dot(Q.T, b))
    return parameters

# Step 1: Generate input and output data for a known system
np.random.seed(0)
system_order = 3
true_parameters = np.array([0.5, -0.25, 0.75])
input_data = np.random.randn(10000)
output_data = np.convolve(input_data, true_parameters, mode='full')[:len(input_data)]

# Step 2 and 3: Identify the system parameters
identified_parameters = identify_system_parameters(input_data, output_data, system_order)

# Step 4: Analyze the results
print("True Parameters:", true_parameters)
print("Identified Parameters:", identified_parameters)

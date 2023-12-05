"""

def SVD(A):
    def Norm(v):
        sqs = 0
        for i in v:
            sqs += (i**2)
        return np.sqrt(sqs)

    def rel_err(x1, x0):
        return abs((x1 - x0) / x1) * 100

    def ev(a):
        x = np.array([[np.random() for i in range(len(a))]])
        max_iter = 10
        old_eigval = 0
        tlr = 0.5
        for i in range(max_iter):
            x = np.dot(a, x.T)
            eigval = Norm(x.T)
            error = rel_err(eigval, old_eigval)
            x = x / eigval
            e, res = [eigval, x]
            if tlr < 0.5:
                break
            old_eigval = eigval
        return e, res

    A = np.array(A)  # Convert input to NumPy array
    B = A.T @ A
    eig, V = ev(B)

    if len(A) == 2:
        u0 = A @ V[:, 0] / Norm(A @ V[:, 0])
        u1 = A @ V[:, 1] / Norm(A @ V[:, 1])
        U = np.array([u0, u1])
    else:
        u0 = A @ V[:, 0] / Norm(A @ V[:, 0])
        u1 = A @ V[:, 1] / Norm(A @ V[:, 1])
        u2 = A @ V[:, 2] / Norm(A @ V[:, 2])
        U = np.array([u0, u1, u2])
    U = U.T

    D = np.round(U.T @ A @ V, decimals=5)
    D = np.where(np.eye(D.shape[0], dtype=bool), D, 0)

    return U, D, V
"""

"""

def power_iteration(matrix, initial_guess, max_iterations=100, tolerance=1e-10):
    v = normalize_vector(initial_guess)
    
    for _ in range(max_iterations):
        v_new = np.dot(matrix, v)
        eigenvalue = np.dot(v, v_new)
        
        if np.linalg.norm(v_new - eigenvalue * v) < tolerance:
            break
        
        v = normalize_vector(v_new)

    return eigenvalue, normalize_vector(v)

def normalize_vector(v):
    return v / np.linalg.norm(v)

def find_eigenvectors(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    eigenvectors = []

    for eigenvalue in eigenvalues:
        system_matrix = matrix - eigenvalue * np.identity(matrix.shape[0])
        _, normalized_v = power_iteration(system_matrix, np.random.rand(matrix.shape[0]))
        
        # Ensure that the eigenvector is unique by checking eigenvalues
        is_unique = all(
            not np.allclose(eigenvalue, ev[0]) for ev in eigenvectors
        )
        
        # Check if the eigenvalue and eigenvector are unique
        if is_unique:
            eigenvectors.append((eigenvalue, normalized_v))

    return eigenvectors
"""
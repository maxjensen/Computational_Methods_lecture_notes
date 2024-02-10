# Notation and facts

## Notation

- $f \in C[a,b]$: $f$ is continuous on $[a,b]$.
- $f \in C^n[a,b]$: $f$ is $n$ times continuously differentiable on $[a,b]$.
- $f \in C^\infty{n+1}[a,b]$: $f$ is arbitrary times continuously differentiable on $[a,b]$.
- $\mathcal{P}_n$: The set of polynomials of degree at most $n$.
- $\delta_{ij}$: The Kronecker delta, equal to $1$ if $i=j$ and 0 otherwise.
- $\mathbb{R}^n$: The $n$-dimensional real coordinate space.
- $\mathbb{R}^{m \times n}$: The set of $m \times n$ real matrices.
- $\mathbb{R}^+$: The set of positive real numbers.
- $e_i$: The $i$-th standard basis vector.
- $a_{ij}$: The element in the $i$-th row and $j$-th column of matrix $A$.
- $a_{:,j}$ or $a_j$:: The $j$-th column of matrix $A$.
- $a_{i,:}$: The $i$-th row of matrix $A$.
- $A^T$: The transpose of matrix $A$.
- $\text{diag}(a_1, \ldots, a_n)$: A diagonal matrix with diagonal elements $a_1, \ldots, a_n$.
- $\text{diag}(A)$: The diagonal of matrix $A$.
- $\det(A)$: The determinant of matrix $A$.
- $\text{rank}(A)$: The rank of matrix $A$.
- $\text{ker}(A)$: The kernel (null space) of matrix $A$.
 
## Facts

- **Geometric series**: $\sum_{k=0}^n x^k = \frac{1-x^{n+1}}{1-x}$ for $x \neq 1$. Converges to $\frac{1}{1-x}$ if $|x| < 1$.
- **Continuity and limits**: A function $f$ is continuous at a point $c$ if $\lim_{x \to c} f(x) = f(c)$.
- **Boundeness of continuous functions**: A continuous function on a closed interval is bounded.
- **Mean value theorem**: If $f \in C[a,b]$ and differentiable on $(a,b)$, there exists a $\xi \in (a,b)$ such that $f'(c) = \frac{f(b) - f(a)}{b-a}$.
- **Taylor's theorem**: For $f \in C^{n+1}[a,b]$ and $x_0, x \in [a,b]$, there's a $\xi$ between $x_0$ and $x$ with $f(x) = f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \ldots + \frac{f^{(n)}(x_0)}{n!}(x-x_0)^n + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}.$
- **Fundamental theorem of calculus:** If $f$ is continuous on $[a, b]$, then $\int_a^b f(x) dx = F(b) - F(a)$, where $f$ is the derivative of $F$.
- **Scalar product of vectors**: The scalar product of vectors $x$ and $y$ is $x^Ty$.
- **Outer product:** The outer product of two vectors $x$ and $y$, denoted as $x \otimes y$, is a matrix where the element in the $i$-th row and $j$-th column is given by $x_i y_j$. Thus, $x \otimes y = xy^T$.
- **Orthogonality**: Two vectors are orthogonal if their scalar product is zero.
- **Orthogonal complement**: The orthogonal complement of a subspace $V$ in $\mathbb{R}^n$ is the set of all vectors in $\mathbb{R}^n$ orthogonal to every vector in $V$.
- **Linear independence**: A set of vectors is linearly independent if no vector in the set can be written as a linear combination of the others.
- **Basis and dimension**: A basis of a vector space is a linearly independent set of vectors that spans the space. The number of vectors in a basis is the dimension of the space.
- **Rank of a matrix**: The rank of a matrix is the maximum number of linearly independent rows or columns.
- **Eigenvectors and eigenvalues**: For square matrix $A$, $v \neq 0$ is an eigenvector if $Av = \lambda v$ for some scalar $\lambda$ (the eigenvalue).
- **Characteristic polynomial**: The characteristic polynomial of matrix $A$ is $\det(A - \lambda I)$. Its roots are the eigenvalues of $A$.
- **Eigenvalues of triangular matrix**: Eigenvalues of a triangular matrix are its diagonal elements.
- **Determinant and eigenvalues**: The determinant of a matrix $A$ is the product of its eigenvalues.
- **Inverse**: A matrix $A$ is invertible if and only if its determinant is non-zero. The inverse of $A$ is $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$
- **Singularity**: A matrix is singular if it has no inverse, i.e., its determinant is zero.
- **Regular matrix**: A matrix is regular if it is non-singular.
- **Diagonalisation**: A matrix $A$ is diagonalisable if it has $n$ linearly independent eigenvectors. It can be written as $A = X \Lambda X^{-1}$, where $\Lambda$ is a diagonal matrix of eigenvalues and $X$ is a matrix of eigenvectors.
- **Geometric and algebraic multiplicity**: The geometric multiplicity of an eigenvalue is the dimension of the eigenspace. The algebraic multiplicity is the number of times the eigenvalue appears as a root of the characteristic polynomial.
- **Backward and forward substitution:** is used to solve a system of linear equations where the matrix is triangular. Backward substitution is also known as back substitution or backward elimination.
- **Gaussian elimination:** is a method for solving linear systems. It consists of applying row operations to transform the matrix into triangular form and then solving for the variables. Gaussian elimination is also known as row reduction.
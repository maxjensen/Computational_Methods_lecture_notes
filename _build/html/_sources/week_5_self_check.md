# Week 5 Self check questions and solutions

> **Question** A matrix $A$ is called tridiagonal if on its diagonal and first off-diagonals contain non-zero entries: $a_{ij} = 0$ if $|i - j| \geq 2$. Show that if $A$ is tridiagonal, then $R$ of its $QR$ factorisation is nonzero only on the diagonal and the first two upper off-diagonals.

**Answer**  Recall the structure of $R$:

$$
    R = \begin{pmatrix}
    \|\tilde{q}_1\|_2 & \langle a_2, q_1 \rangle & \ldots & \langle a_n, q_1 \rangle \\
                      & \|\tilde{q}_2\|_2        & \ddots & \vdots \\
                      &                          & \ddots & \langle a_n, q_{n-1} \rangle \\
                      &                          &        & \|\tilde{q}_n\|_2
    \end{pmatrix}
    $$
    
We need to show $r_{ij} = 0$ if $j + 2 \geq i$: 
- The result trivially holds for the first three columns because of the triangularity of $R$. Thus, let $j \geq 4$.
- We know that the first $j - 2$ entries of the $j$th column of $a_j$ vanish because of the tridiagonal structure.
- We that $\mathrm{span}(a_1, \ldots, a_i) = \mathrm{span}(q_1, \ldots, q_i)$ owing to the construction of the Gram-Schmid method. Because of the tridiagonal structure, only the $(i+1)$th elements of $q_k$, $k \leq i$, can be non-zero. 
- Therefore if $j + 2 \geq i$
  
  $$
  r_{ij} = \langle a_j, q_i \rangle = \sum_{k = 1}^n (a_j)_k, (q_i)_k = 0
  $$
  
  because in each part of the sum, one factor equals $0$.

> **Question** Given $A \in \mathbb{R}^{n \times m}$ with $m \geq n$ show that the factorisation $A = LQ$ exists, where $Q$ is an $n \times m$ matrix with orthogonal rows and where $L$ is an $n \times n$ lower triangular matrix. 

**Answer** Using the $QR$ decomposition $A^T = \bar{Q} R$ of the transpose,

$$
A = (A^T)^T = (\bar{Q} R)^T = R^T \bar{Q}^T = L Q
$$

with $L := R^T$ and $Q := \bar{Q}^T$.

> **Question** Determine the $2\times 2$ matrix $Q$ that rotates a vector by an angle $\theta$. Is this matrix orthogonal? Show that $Q^{-1}$ is identical to the matrix that rotates vectors by an angle of $-\theta$.

```{dropdown} **Answer**
The rotation matrix is given as follows:  
  
$$  
Q =   
\begin{bmatrix}  
\cos\theta & -\sin\theta\\  
\sin\theta & \cos\theta  
\end{bmatrix}  
$$  
  
The matrix $Q$ is orthogonal since $Q^TQ=I$. The rotation matrix for the angle $-\theta$ is obtained as  
  
$$  
\hat{Q} =  
\begin{bmatrix}  
\cos\theta & +\sin\theta\\  
-\sin\theta & \cos\theta  
\end{bmatrix},  
$$  
  
which is just the transpose of $Q$. Hence, as expected, the inverse of $Q$ is just the rotation by $-\theta$.
```

**Answer** The rotation matrix is given as follows:  
  
$$  
Q =   
\begin{bmatrix}  
\cos\theta & -\sin\theta\\  
\sin\theta & \cos\theta  
\end{bmatrix}  
$$  
  
The matrix $Q$ is orthogonal since $Q^TQ=I$. The rotation matrix for the angle $-\theta$ is obtained as  
  
$$  
\hat{Q} =  
\begin{bmatrix}  
\cos\theta & +\sin\theta\\  
-\sin\theta & \cos\theta  
\end{bmatrix},  
$$  
  
which is just the transpose of $Q$. Hence, as expected, the inverse of $Q$ is just the rotation by $-\theta$.

> **Question** Let $u\in\mathbb{R}^n$ with $\|u\|_2=1$. Define $P=uu^T$. Show that $P=P^2$. Is $P$ an orthogonal matrix? Describe what $P$ is doing. Matrices that satisfy $P=P^2$ are also called projectors.

**Answer** We have  
  
$$  
P^2 = uu^Tuu^T = uu^T  
$$  
  
since $u^Tu = 1$.  
  
$P$ is not orthogonal since it is singular. If $v\bot u$ then $Pv = 0$. $Px$ is the projection of a vector $x$ along $u$, that is it cancels out all components of $x$ orthogonal to $u$.

> **Question** Let $P=P^2$ be a projector satisfying $P=P^T$. Show that $Q=I-2P$ is an orthogonal matrix. Give a geometric interpretation of $Q$.

**Answer** We have  
  
$$  
(I-2P)^T(I-2P) = (I -2P)^2 = I - 4P + 4P^2 = I  
$$  
  
since $P=P^T$ and $P^2=P$. The matrix $Q$ is a reflector. All components orthogonal to $P$ are left untouched while all components in the range of $P$ are subtracted twice, therefore being reflected. In the special case that $P=uu^T$ for $\|u\|_2=1$, the matrix $Q$ is a Householder transformation.

> **Question** In the following we define two different ways of orthogonalising a set of vectors.
> 
> ```python
> import numpy as np  
>   
> def gram_schmidt(A):  
>     """Returns an orthogonal basis for the columns in A."""  
>     m = A.shape[0]  
>     n = A.shape[1]  
>       
>     Q = np.zeros((m, n), dtype=np.float64)  
>     Q[:, 0] = A[:, 0] / np.linalg.norm(A[:, 0])  
>       
>     for col in range(1, n):  
>         t = A[:, col]  
>         inner_products = Q[:, :col].T @ t  
>         t -= Q[:, :col] @ inner_products  
>         Q[:, col] = t / np.linalg.norm(t)  
>       
>     return Q  
>     def modified_gram_schmidt(A):  
>     """Return an orthogonal basis for the columns in A"""  
>           
> m = A.shape[0]  
>     n = A.shape[1]  
>       
>     Q = np.zeros((m, n), dtype=np.float64)  
>     Q[:, 0] = A[:, 0] / np.linalg.norm(A[:, 0])  
>       
>     for col in range(1, n):  
>         t = A[:, col]  
>         for index in range(col):  
>             t -= Q[:, index] * (np.inner(Q[:, index], t))  
>         Q[:, col] = t / np.linalg.norm(t)  
>       
>     return Q
> ```
> 
> Describe the difference between the two formulations and convince yourself that they are algebraically equivalent. Can you numerically demonstrate that the modified formulation is more accurate in floating point arithmetic?

**Answer** The Gram-Schmidt orthogonalisation first forms all inner products against the previous vectors and then subtracts them. In contrast, the modified Gram-Schmidt method subtracts immediately after forming the inner product with a previous column $q$. Modified Gram-Schmidt is just a reordering of the orthogonalisation. However, it can be shown that modified Gram-Schmidt is numerically more stable.  
  
In the example below, we orthogonalise a matrix $A$ with both methods and then compare the resulting matrix $Q$ with the identity matrix. The relative residual of modified Gram-Schmidt is much closer to machine precision than that of Gram-Schmidt. In practice, therefore, usually modified Gram-Schmidt is used.

```python
m = 1000  
n = 1000  
  
A = np.random.rand(m, n)  
Q_gs = gram_schmidt(A)  
Q_mgs = modified_gram_schmidt(A)  
  
ident = np.eye(n)  
res_gs = np.linalg.norm(Q_gs.T @ Q_gs - ident) / np.linalg.norm(ident)  
res_mgs = np.linalg.norm(Q_mgs.T @ Q_mgs - ident) / np.linalg.norm(ident)  
  
print(f"Residual for Gram-Schmidt: {res_gs}")  
print(f"Residual for modified Gram-Schmidt: {res_mgs}")
```

This results in the output

```python
Residual for Gram-Schmidt: 4.610285906483318e-11
Residual for modified Gram-Schmidt: 1.1165488100397485e-15
```
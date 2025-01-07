# Markdown and LaTeX

Following the [Introduction to Markdown and LaTeX](https://ashki23.github.io/markdown-latex.html), Markdown allows you to write in a simple plain-text format that supports text formatting, embedded graphics, source code, and LaTeX formulas. LaTeX is a high-quality typesetting system; it includes features designed to produce technical and scientific documentation. A basic understanding of Markdown and LaTeX enables the quick creation of high-quality documents and reports. This tutorial provides a quick reference for using Markdown and LaTeX. This text is written in Markdown; you can view the original text by clicking the download button in the top-right corner of this page.

**You need to submit your coursework on Crowdmark in Markdown.**

The following provides a quick reference to the most commonly used Markdown syntax.

## Emphasis

Text can be emphasised as follows:

- `*Italic* and **Bold**` becomes *Italic* and **Bold**

To quote text, use `>`. For example:

```markdown
> Imagination is more important than knowledge.
>
> Albert Einstein
```

gives
> Imagination is more important than knowledge.
>
> Albert Einstein

For a manual line break, use:

- `<br />`

## Headers

Headers and document titles are defined by lines beginning with hashes. More hashes indicate lower-ranked headers:

```markdown
# H1
## H2
### H3
#### H4
##### H5
###### H6
```

## Lists

Markdown supports lists using dashes (`-`), stars (`*`), or numbers, e.g.:

```markdown
- Item 1
- Item 2
    - Item 2a (2 tabs)
    - Item 2b
        - Item 2b-1 (4 tabs)
        - Item 2b-2
```

turns into

- Item 1
- Item 2
  - Item 2a (2 tabs)
  - Item 2b
    - Item 2b-1 (4 tabs)
    - Item 2b-2

```markdown
1. Item 1
2. Item 2
3. Item 3
    - Item 3a
    - Item 3b
```

turns into

1. Item 1
2. Item 2
3. Item 3
    - Item 3a
    - Item 3b

## Links and images

The name of a link is placed within square brackets, followed by the address in parentheses. For example: `[UCL](https://www.ucl.ac.uk/)` turns into [UCL](https://www.ucl.ac.uk/).

To display an image in the document, add an exclamation mark in front, using the structure `![...](...)`. For example, `![logo](https://www.ucl.ac.uk/brand/sites/brand/files/styles/small_image/public/ucl-logo-white-on-black.jpg)` turns into

![logo](https://www.ucl.ac.uk/brand/sites/brand/files/styles/small_image/public/ucl-logo-white-on-black.jpg)

## Tables

You can also add tables. For example:

```markdown
1st Header|2nd Header|3rd Header
---|:---:|---:
col 1 is|left-aligned|1
col 2 is|center-aligned|2
col 3 is|right-aligned|3
```

turns into

1st Header|2nd Header|3rd Header
---|:---:|---:
col 1 is|left-aligned|1
col 2 is|center-aligned|2
col 3 is|right-aligned|3

## Code blocks

In Markdown, you can add plain code blocks (non-evaluating) using triple backticks (`\`\`\``). Double-click on the text cell to understand the example:

```markdown
import matplotlib.pyplot as plt
import numpy as np
```

You can add syntax highlighting by specifying the programming language after the opening triple backticks:

```python
import matplotlib.pyplot as plt
import numpy as np
```

## LaTeX and adding mathematics to Markdown

LaTeX is a sophisticated typesetting system for mathematical texts. Markdown borrows from LaTeX to typeset mathematical formulas without going into the full complexity of LaTeX. For more information about LaTeX see for example [Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) and [Wikibooks](https://en.wikibooks.org/wiki/LaTeX/Mathematics).

We switch to inline formulas with a single `$` and to a display formula with a double `$$`.

```markdown
While $f(x) \ne g(y)$ is space-saving, this if often clearer:

$$
f(x) \ne g(x)
$$
```

gives

---
While $f(x) \ne g(y)$ is space-saving, this if often clearer:

$$
f(x) \ne g(x)
$$
---

## Symbols

### Operators

```markdown
- $x + y$
- $x - y$
- $x \times y$
- $x \div y$
- $\dfrac{x}{y}$
- $\sqrt{x}$
```

gives

- $x + y$
- $x - y$
- $x \times y$
- $x \div y$
- $\dfrac{x}{y}$
- $\sqrt{x}$

### Mathematical symbols

```markdown
- $\pi \approx 3.14159$
- $\pm \, 0.2$
- $\dfrac{0}{1} \neq \infty$
- $0 < x < 1$
- $0 \leq x \leq 1$
- $x \geq 10$
- $\forall \, x \in (1,2)$
- $\exists \, x \notin [0,1]$
- $A \subset B$
- $A \subseteq B$
- $A \cup B$
- $A \cap B$
- $X \implies Y$
- $X \impliedby Y$
- $a \to b$
- $a \longrightarrow b$
- $a \Rightarrow b$
- $a \Longrightarrow b$
- $a \propto b$
```

gives

- $\pi \approx 3.14159$
- $\pm \, 0.2$
- $\dfrac{0}{1} \neq \infty$
- $0 < x < 1$
- $0 \leq x \leq 1$
- $x \geq 10$
- $\forall \, x \in (1,2)$
- $\exists \, x \notin [0,1]$
- $A \subset B$
- $A \subseteq B$
- $A \cup B$
- $A \cap B$
- $X \implies Y$
- $X \impliedby Y$
- $a \to b$
- $a \longrightarrow b$
- $a \Rightarrow b$
- $a \Longrightarrow b$
- $a \propto b$

### Accents

```markdown
- $\bar a$
- $\tilde a$
- $\breve a$
- $\hat a$
- $a^ \prime$
- $a^ \dagger$
- $a^ \ast$
- $a^ \star$
- $\mathcal A$
- $\mathrm a$
- $\cdots$
- $\vdots$
- $\#$
- $\$$
- $\%$
- $\&$
- $\{ \}$
- $\_$
```

gives

- $\bar a$
- $\tilde a$
- $\breve a$
- $\hat a$
- $a^ \prime$
- $a^ \dagger$
- $a^ \ast$
- $a^ \star$
- $\mathcal A$
- $\mathrm a$
- $\cdots$
- $\vdots$
- $\#$
- $\$$
- $\%$
- $\&$
- $\{ \}$
- $\_$

### Greek letters

```markdown
$$
\alpha, \beta, \gamma, \delta, \epsilon, \pi,\\
\Gamma,\Sigma,\Upsilon,\Pi,\Theta
$$
```

gives

$$
\alpha, \beta, \gamma, \delta, \epsilon, \pi,\\
\Gamma,\Sigma,\Upsilon,\Pi,\Theta
$$

## Spaces

- Horizontal space: `\quad`
- Large horizontal space: `\qquad`
- Small space: `\,`
- Medium space: `\:`
- Large space: `\;`
- Negative space: `\!`

For example, `$a \; + \! b$` gives $a \; + \! b$.

## Matrices

To investigate the Markdown code for matrices, download this page's Markdown version by clicking the download button on the top right.

$$
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
$$

$$
M =
\begin{pmatrix}
\frac{5}{6} & \frac{1}{6} & 0 \\[0.3em]
\frac{5}{6} & 0 & \frac{1}{6} \\[0.3em]
0 & \frac{5}{6} & \frac{1}{6}
\end{pmatrix}
$$

$$
M =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

$$
M =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

$$
A_{m,n} =
\begin{pmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n}
\end{pmatrix}
$$

## Functions

Special function names such as trigonometic functions are traditionally written in non-italic font. To achieve this, write `f(x) = \sin(x)` instead of `f(x) = sin(x)`, which gives $f(x) = \sin(x)$ instead of $f(x) = sin(x)$.

Similarly, `\cos(x) \qquad \log(x) \qquad \exp(x)` gives

$$
\cos(x) \qquad \log(x) \qquad \exp(x).
$$

## Sub and superscripts

- Subscripts: `$a_i$ or $a_{ij}$` gives $a_i$ or $a_{ij}$
- Superscripts: `$a^i$ or $a^{ij}$` gives $a^i$ or $a^{ij}$

## Sums and products

A sum is written `S_n = \sum_{i=1}^n X^i`:

$$
S_n = \sum_{i=1}^n X^i
$$

A product is written `P_n = \prod_{i=1}^n X_i`:

$$
P_n = \prod_{i=1}^n X_i
$$

## Derivatives and integrals

Derivatives `f'(x) = \frac{df}{dx}`:

$$
f'(x) = \frac{df}{dx}
$$

Partial derivatives `f(a,b) = f(0,b) + \frac{\partial f}{\partial x} a + \text{higher-order terms}`:

$$
f(a,b) = f(0,b) + \frac{\partial f}{\partial x} a + \text{higher-order terms}
$$

Integrals `\int_0^1 f(x) \, dx`:

$$
\int_0^1 f(x) \, dx
$$

## Examples

Investigate the Markdown code for matrices by double-clicking on the text cell.

$$
\forall x \in X\quad \exists y \subset \Sigma
$$

$$
x_n \rightarrow 0 \text{ as } n \rightarrow \infty
$$

$$
\|A\|_p := \sup_{x \in R^n \setminus \{0\}} \frac{\|Ax\|_p}{\|x\|_p}
$$

Question: Find the roots of

$$
x^2+p x + q = 0
$$

Solution:

$$
x_\pm = -\frac{p}{2} \pm \sqrt{\Big(\frac{p}{2}\Big)^2 - q}
$$

## Converting LaTeX to Markdown

If you have already written a text in LaTeX and need it in Markdown, you can use tools like [Pandoc](https://pandoc.org/) to convert from one format to another.

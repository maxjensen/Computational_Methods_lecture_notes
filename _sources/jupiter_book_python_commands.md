# Commands to compile and upload Jupyter Books (version 1)

- Make sure changes are saved before executing the below.

## Entering the `jb1` environment

- In VSC, you can set the compiler, using Command Palette → Python: Select Interpreter → Enter interpreter path… and picking the interpreter

```
/Users/maxjensen/Annexe/Python/Python/envs/jb1/.venv/bin/python
```

Alternatively,

```
source /Users/maxjensen/Annexe/Python/Python/envs/jb1/.venv/bin/activate
```

- Compile to HTML:

```
uv run jupyter-book build .
```

- Compile to single page HTML and then PDF:

```
uv run jupyter-book build . --builder pdfhtml
```

- Clean:

```
uv run jupyter-book clean .
```

- Upload to Github:

```
uv run ghp-import -n -p -f _build/html
```

## Not entering the `jb1` environment

- Compile to HTML:

```
uv --project ~/Annexe/Python/Python/envs/jb1 run jupyter-book build .
```

- Compile to single page HTML and then PDF:

```
uv --project ~/Annexe/Python/Python/envs/jb1 run jupyter-book build . --builder pdfhtml
```

- Clean:

```
uv --project ~/Annexe/Python/Python/envs/jb1 run jupyter-book clean .
```

- Upload to Github:

```
uv --project ~/Annexe/Python/Python/envs/jb1 run ghp-import -n -p -f _build/html
```
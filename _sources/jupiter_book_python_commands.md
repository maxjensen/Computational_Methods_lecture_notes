# Commands to compile and upload Jupyter Books (version 1)

- Make sure changes are saved before executing the below.

## Entering the `legacy` environment

- In VS Code, you can set the interpreter using Command Palette → Python: Select Interpreter → Enter interpreter path… and pick:

```
$HOME/Python/envs/legacy/bin/python
```

Alternatively,

```
source $HOME/Python/envs/legacy/bin/activate
```

- Compile to HTML:

```
jupyter-book build .
```

- Compile to single page HTML and then PDF:

```
jupyter-book build . --builder pdfhtml
```

- Clean:

```
jupyter-book clean .
```

- Upload to Github:

```
ghp-import -n -p -f _build/html
```

## Not entering the `legacy` environment

- Compile to HTML:

```
source $HOME/Python/envs/legacy/bin/activate
uv --project $HOME/Python/Python_standard_configuration/envs/legacy run --active jupyter-book build .
deactivate
```

- Compile to single page HTML and then PDF:

```
source $HOME/Python/envs/legacy/bin/activate
uv --project $HOME/Python/Python_standard_configuration/envs/legacy run --active jupyter-book build . --builder pdfhtml
deactivate
```

- Clean:

```
source $HOME/Python/envs/legacy/bin/activate
uv --project $HOME/Python/Python_standard_configuration/envs/legacy run --active jupyter-book clean .
deactivate
```

- Upload to Github:

```
source $HOME/Python/envs/legacy/bin/activate
uv --project $HOME/Python/Python_standard_configuration/envs/legacy run --active ghp-import -n -p -f _build/html
deactivate
```

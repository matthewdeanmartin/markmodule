# markmodule
Import python from markdown files.

## Usage

In a file named `hello_module.md` define a function. I'm escaping the fence, use a real three-tick fence.

```markdown
Here is a function

``(`)python
def hello() -> str:
    return "Hello"
``(`) 
```

Generate a type stub and import using the usual syntax. `generate_side_by_side_pyi` will write a `.pyi` file to the file system and enable IDEs type hinting to work.

```python
import sys
import markmodule
markmodule.generate_side_by_side_pyi("hello_module")
sys.meta_path.append(markmodule.MdFinder())
import hello_module
print(hello_module.hello())
```

Import with path to file.
```python
import markmodule
markmodule.import_md("hello_module.md")
import hello_module
print(hello_module.hello())
```

## Markdown is a hammer, everything is a nail

You can use markdown:

- as a place to put module code, [markmodule](https://pypi.org/project/markmodule), this library

The do-everything-with-markdown ecosystem is surprisingly robust.
- as a Makefile alternative, [mask](https://github.com/jacobdeichert/mask)
- as a place to put scripts, eg python's [markdown-exec](https://pypi.org/project/markdown-exec/), or ruby's [markdown_exec](https://github.com/fareedst/markdown_exec)
- as a place to put unit tests, [pytest-markdown-docs](https://pypi.org/project/pytest-markdown-docs/),  [pytest-codeblocks](https://pypi.org/project/pytest_codeblocks/), and [pytest-markdown](https://pypi.org/project/pytest-markdown/)
- as a string template, [proof-of-concept gist](https://gist.github.com/facelessuser/53fa4d93f27c252fda813b5e0ba7325c)


## Change Log

- 0.1.0 - Basic idea.
- 0.2.0 - Updates to readme
- 0.3.0 - Generates pyi and you can use `import` syntax 

## Documentation

- [Contributing](https://github.com/matthewdeanmartin/markmoduel/blob/main/docs/contributing.md)
- [TODO](https://github.com/matthewdeanmartin/markmoduel/blob/main/docs/TODO.md)
- [Related StackOverflow Links](https://github.com/matthewdeanmartin/markmoduel/blob/main/docs/stackoverflow.md)

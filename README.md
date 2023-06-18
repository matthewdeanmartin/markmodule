# markmodule
Import python from markdown files.

## Markdown is a hammer, everything is a nail

You can use markdown:

- as a place to put module code, [markmodule](https://pypi.org/project/markmodule), this library

The do-everything-with-markdown ecosystem is surprisingly robust.
- as a Makefile alternative, [mask](https://github.com/jacobdeichert/mask)
- as a place to put scripts, eg python's [markdown-exec](https://pypi.org/project/markdown-exec/), or ruby's [markdown_exec](https://github.com/fareedst/markdown_exec)
- as a place to put unit tests, [pytest-markdown-docs](https://pypi.org/project/pytest-markdown-docs/),  [pytest-codeblocks](https://pypi.org/project/pytest_codeblocks/), and [pytest-markdown](https://pypi.org/project/pytest-markdown/)
- as a string template, [proof-of-concept gist](https://gist.github.com/facelessuser/53fa4d93f27c252fda813b5e0ba7325c)

## Usage

In a file named `hello_module.md`m define a function. I'm escaping the fence, use a real three tick fence.

```markdown
Here is a function

``(`)python
def some_function(args: str) -> str:
    """This is a function that does something."""
    return "Hello World" + args
``(`)

And some more documentation 
```

Import. Your IDE will not recognize the module, but it will work at runtime.
```python
import markmodule
markmodule.import_md("hello_module.md")
import hello_module

print(hello_module.some_function("yo!"))
```

## Change Log

- 0.1.0 - Basic idea.
- 0.2.0 - Updates to readme
- 
## Documentation

- [Contributing](https://github.com/matthewdeanmartin/markmoduel/blob/main/docs/contributing.md)
- [TODO](https://github.com/matthewdeanmartin/markmoduel/blob/main/docs/TODO.md)
- [Related StackOverflow Links](https://github.com/matthewdeanmartin/markmoduel/blob/main/docs/stackoverflow.md)



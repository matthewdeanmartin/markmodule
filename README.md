# markmodule
Import python from markdown files.

## Markdown is a hammer, everything is a nail

You can use markdown:

- as a place to put module code  (markmodule, this library)
- as a Makefile alternative
- as a place to put scripts
- as a place to put unit tests
- as a string template

## Usage

```python
import markmodule
import_md("hello_module.md")
import hello_module

print(hello_module.some_function("yo!"))
```

## Development Setup

```bash
cargo install mask
```
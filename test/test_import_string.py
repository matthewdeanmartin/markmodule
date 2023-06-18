from markmodule import import_code_string
from markmodule.import_string import import_markdown_string


def test_import_markdown_string():
    marks = """
```python
print('hello')
```
"""
    import_markdown_string(marks, "hello2")


def test_import_code_string():
    import_code_string("print('hello')", "hello")

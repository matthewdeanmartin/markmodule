from markmodule import import_md

if __name__ == "__main__":
    import_md("../hello/hello_module.md")
    import hello_module

    print(hello_module.some_function("yo!"))

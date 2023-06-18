from markmodule import import_code_string


def run():
    code_string = """
def greet(name):
    print(f'Hello, {name}!')
    """
    module_name = "my_module"
    import_code_string(code_string, module_name)
    # pycharm doesn't know what to do with this.
    from my_module import greet

    greet("world")


if __name__ == "__main__":
    run()

import os
from pathlib import Path

# import markdown2
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


import mistune


class MyRenderer(mistune.HTMLRenderer):
    # def block_code(self, code, lang):
    def block_code(self, code, info=None):
        if not info:
            return "\n<pre><code>%s</code></pre>\n" % mistune.escape(code)
        lexer = get_lexer_by_name(info, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


def generate_index_html(root_folder):
    html_files = []

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    html_content = (
        "<html>\n<head>\n<title>Index</title>\n"
        "<link rel='stylesheet' href='./style.css'>\n"
        "</head>\n"
        "</head>\n<body>\n<ul>\n"
    )

    for file in html_files:
        file_name = os.path.basename(file)
        base_url = "/".join(Path(file).parts[1:-1])
        if base_url == "":
            url = file_name
        else:
            url = f"{base_url}/{file_name}"
        html_content += f"<li><a href='{url}'>{file_name}</a></li>\n"

    html_content += "</ul>\n</body>\n</html>"

    with open(os.path.join(root_folder, "index.html"), "w") as file:
        file.write(html_content)


def convert_markdown_to_html_with_syntax_highlighting(md_file: str) -> str:
    # Read the contents of the Markdown file
    with open(md_file) as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    MyRenderer()
    markdown = mistune.create_markdown(renderer=MyRenderer())
    html_content = markdown(markdown_content)
    # html_content = markdown2.markdown(markdown_content, extras=["fenced-code-blocks"])

    return html_content


def generate_html_from_markdown(root_folder: str) -> None:
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            print(file)
            if file.endswith(".md"):
                md_file = os.path.join(root, file)
                html_content = convert_markdown_to_html_with_syntax_highlighting(md_file)

                # Generate HTML file with the same name
                html_file = os.path.splitext(md_file)[0] + ".html"
                with open(html_file, "w") as file:
                    file.write("<link rel='stylesheet' href='./style.css'>\n")
                    file.write(html_content)


root_folder = "sample_module"
generate_html_from_markdown(root_folder)
generate_index_html(root_folder)

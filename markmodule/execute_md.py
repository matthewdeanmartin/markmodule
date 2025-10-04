# In some site-packages module you register a codec:
from __future__ import annotations

import io
from encodings import utf_8
import codecs
from codecs import CodecInfo
from typing_extensions import Buffer


def decode(input_bytes, errors="strict"):
    """
    Extract all fenced Python code blocks (```python ... ```) from text.
    Returns concatenated code without fences.
    """
    text = input_bytes.decode("utf-8", errors=errors)
    lines = text.splitlines()

    inside = False
    blocks = []
    current = []

    for line in lines:
        if not inside:
            # opening fence
            if line.strip().lower().startswith("```python") or line.strip().lower().startswith("```py"):
                inside = True
                current = []
        else:
            # closing fence
            if line.strip().startswith("```") or line.strip().startswith("~~~"):
                inside = False
                if current:
                    blocks.append("\n".join(current))
            else:
                current.append(line)

    joined = ("\n\n".join(blocks)).strip() if blocks else ""
    return joined, len(input_bytes)


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(  # pragma: no cover
        self,
        input: Buffer,
        errors: str,
        final: bool,
    ) -> tuple[str, int]:

        if final:
            return decode(input, errors)
        else:

            return "", 0


class StreamReader(utf_8.StreamReader):
    """decode is deferred to support better error messages"""

    _stream = None
    _decoded = False

    @property
    def stream(self) -> codecs._ReadableStream:
        assert self._stream is not None
        if not self._decoded:
            text, _ = decode(self._stream.read())
            self._stream = io.BytesIO(text.encode("UTF-8"))
            self._decoded = True
        return self._stream

    @stream.setter
    def stream(self, stream: codecs._ReadableStream) -> None:
        self._stream = stream
        self._decoded = False


def markdown_search(name: str) -> CodecInfo | None:
    if name != "markdown":
        return None

    return CodecInfo(
        name="markdown",
        # encode=None,
        decode=decode,
        # name=name,
        encode=utf_8.encode,
        # decode=decode,
        incrementalencoder=utf_8.IncrementalEncoder,
        # incrementaldecoder=codecs.BufferedIncrementalDecoder,
        # streamreader=utf_8.StreamReader,
        incrementaldecoder=IncrementalDecoder,
        # streamreader=StreamReader,
        # streamreader=utf_8.StreamReader,
        # streamwriter=utf_8.StreamWriter,
    )


def register():
    codecs.register(markdown_search)


if __name__ == "__main__":
    print(decode("```python\nprint('hello')\n```\n# hello ```\n\n```python\nprint('hello')\n```".encode()))

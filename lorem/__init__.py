# The MIT License (MIT)
#
# Copyright (c) 2016 Stefan Fischer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Generator for random text that looks like Latin.

The project was initiated by Stefan Fischer.

"""
import sys

if sys.version_info.minor >= 9:
    # INFO: See this for more info
    # https://www.python.org/dev/peps/pep-0585/
    from collections.abc import Sequence
    Tuple = tuple
else:
    from typing import Tuple, Sequence
from .text import TextLorem as _Lorem

__author__ = 'Stefan Fischer'
__email__ = 'sfischer13@ymail.com'
__version__ = '0.1.2'

__all__ = ['sentence', 'paragraph', 'text']


def sentence(
    wsep: str = ' ',
    ssep: str = ' ',
    psep: str = '\n\n',
    srange: Tuple[int, int] = (4, 8),
    prange: Tuple[int, int] = (5, 10),
    trange: Tuple[int, int] = (3, 6),
    words: Sequence[str] = None
) -> str:
    return _Lorem(
        wsep=wsep,
        ssep=ssep,
        psesp=psep,
        srange=srange,
        prange=prange,
        trange=trange,
        words=words
    ).sentence()


def paragraph(
    wsep: str = ' ',
    ssep: str = ' ',
    psep: str = '\n\n',
    srange: Tuple[int, int] = (4, 8),
    prange: Tuple[int, int] = (5, 10),
    trange: Tuple[int, int] = (3, 6),
    words: Sequence[str] = None
):
    return _Lorem(
        wsep=wsep,
        ssep=ssep,
        psesp=psep,
        srange=srange,
        prange=prange,
        trange=trange,
        words=words
    ).paragraph()


def text(
    wsep: str = ' ',
    ssep: str = ' ',
    psep: str = '\n\n',
    srange: Tuple[int, int] = (4, 8),
    prange: Tuple[int, int] = (5, 10),
    trange: Tuple[int, int] = (3, 6),
    words: Sequence[str] = None
):
    return _Lorem(
        wsep=wsep,
        ssep=ssep,
        psesp=psep,
        srange=srange,
        prange=prange,
        trange=trange,
        words=words
    ).text()

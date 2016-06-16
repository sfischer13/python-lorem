import random

from .data import WORDS


class TextLorem():
    def __init__(self, wsep=' ', ssep=' ', psep='\n\n',
                 srange=(4, 8), prange=(5, 10), trange=(3, 6),
                 words=None):
        self._wsep = wsep
        self._ssep = ssep
        self._psep = psep
        self._srange = srange
        self._prange = prange
        self._trange = trange
        if words:
            self._words = words
        else:
            self._words = WORDS

    def sentence(self):
        n = random.randint(*self._srange)
        s = self._wsep.join(self._word() for _ in range(n))
        return s[0].upper() + s[1:] + '.'

    def paragraph(self):
        n = random.randint(*self._prange)
        p = self._ssep.join(self.sentence() for _ in range(n))
        return p

    def text(self):
        n = random.randint(*self._trange)
        t = self._psep.join(self.paragraph() for _ in range(n))
        return t

    def _word(self):
        return random.choice(self._words)

from passlib.crypto._blowfish.base import BlowfishEngine as _BlowfishEngine

class BlowfishEngine(_BlowfishEngine):
    def encipher(self, l, r): ...
    def expand(self, key_words) -> None: ...

__all__ = ["BlowfishEngine"]

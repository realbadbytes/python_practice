class CountFromBy:

    def __init__(self, v=0, i=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr(self) -> str:
        return str(self.val)
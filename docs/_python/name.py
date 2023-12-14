from pydantic import BaseModel

from clipstick import parse


class MyName(BaseModel):
    """What is my name.

    In case you forgot I will repeat it x times.
    """

    name: str
    """Your name."""

    repeat_count: int = 10
    """How many times to repeat your name."""

    def main(self):
        for _ in range(self.repeat_count):
            print(f"Hello: {self.name}")


if __name__ == "__main__":
    model = parse(MyName)
    model.main()

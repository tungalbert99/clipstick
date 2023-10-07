# a list will always be considered a keyworded argument parser.

from pydantic import BaseModel
from clipstick._clipstick import parse


class ListModel(BaseModel):
    values: list[str]


class TupleModel(BaseModel):
    values: tuple[int]


class SetModel(BaseModel):
    values: set[str]


def test_list_model():
    model = parse(ListModel, ["--values", "val1", "--values", "val2"])
    assert model == ListModel(values=["val1", "val2"])

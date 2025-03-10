import pytest
from clipstick import parse
from pydantic import BaseModel


class Main(BaseModel):
    pos_value_1: str
    pos_value_2: int

    required_bool: bool

    optional_1: str = "opt1"
    optional_2: int = 20
    optional_bool: bool = False


def test_main_all_args():
    model = parse(
        Main,
        [
            "val1",
            "10",
            "--required-bool",
            "--optional-1",
            "alt_opt1",
            "--optional-2",
            "22",
            "--optional-bool",
        ],
    )

    assert model == Main(
        pos_value_1="val1",
        pos_value_2=10,
        required_bool=True,
        optional_1="alt_opt1",
        optional_2=22,
        optional_bool=True,
    )


def test_main_some_args():
    model = parse(
        Main,
        [
            "val1",
            "10",
            "--required-bool",
            "--optional-2",
            "22",
            "--optional-bool",
        ],
    )

    assert model == Main(
        pos_value_1="val1",
        pos_value_2=10,
        required_bool=True,
        optional_2=22,
        optional_bool=True,
    )


def test_optionals_out_of_order():
    model = parse(
        Main,
        [
            "--optional-2",
            "22",
            "val1",
            "10",
            "--required-bool",
        ],
    )

    assert model == Main(
        pos_value_1="val1", pos_value_2=10, required_bool=True, optional_2=22
    )


def test_main_help(capture_output):
    """Manually check the output at `help_output` folder."""
    with pytest.raises(SystemExit) as err:
        capture_output(Main, ["-h"])

    assert err.value.code == 0
    assert "pos-value-1" in capture_output.captured_output

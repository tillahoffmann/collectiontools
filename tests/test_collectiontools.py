import collectiontools as ct
import pytest


def test_transpose() -> None:
    x = [
        {"a": 1, "b": {1, 2}},
        {"a": "foo", "b": None},
    ]
    y = {
        "a": [1, "foo"],
        "b": [{1, 2}, None],
    }
    assert ct.transpose_to_dict(x) == y
    assert ct.transpose_to_list(y) == x
    assert ct.transpose(x) == y
    assert ct.transpose(y) == x
    assert ct.transpose(ct.transpose(x)) == x
    assert ct.transpose(ct.transpose(y)) == y

    with pytest.raises(ValueError, match="inconsistent keys"):
        ct.transpose_to_dict(
            [
                {"a": 1, "b": {1, 2}},
                {"a": "foo"},
            ]
        )

    with pytest.raises(ValueError, match="inconsistent sizes"):
        ct.transpose_to_list(
            {
                "a": [],
                "b": [1],
            }
        )

    with pytest.raises(ValueError, match="mapping or iterable"):
        ct.transpose(7)


def test_map_values():
    assert ct.map_values({"a": 1, "b": "hello"}, lambda x: 2 * x) == {
        "a": 2,
        "b": "hellohello",
    }


def test_update_and_union():
    x = {"a": "b", "c": 1}
    assert ct.update(x, {"a": ct.Delete, "c": 7, "d": None}) == {"c": 7, "d": None}
    assert "a" not in x
    assert ct.union(x, d=ct.Delete, c=9) == {"c": 9}
    assert "d" in x

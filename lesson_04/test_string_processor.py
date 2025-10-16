import pytest
from string_utils import StringUtils


@pytest.mark.positive.test
@pytest.mark.parametrize("vhod, rez", [("Good", "Good"), ("good", "Good")])
def test_pozitive_cap(vhod, rez):
    proc = StringUtils()
    assert proc.capitalize(vhod) == rez


@pytest.mark.negative.test
@pytest.mark.parametrize("vhod, rez", [(" good", " good"), ("3", "3"),
                                       ("g", "G"), ("..", ".."), ("", ""),
                                       (" ", " ")])
def test_neganiv_cap(vhod, rez):
    proc = StringUtils()
    assert proc.capitalize(vhod) == rez


@pytest.mark.positive.test
@pytest.mark.parametrize("vhod, rez", [("Good", "Good"), (" Good", "Good"),
                                       ("  Good", "Good")])
def test_pozitive_trim(vhod, rez):
    proc = StringUtils()
    assert proc.trim(vhod) == rez


@pytest.mark.negative.test
@pytest.mark.parametrize("vhod, rez", [("        good", "good"), (" . ", ". "),
                                       ("", ""), (" ", "")])
def test_neganiv_trim(vhod, rez):
    proc = StringUtils()
    assert proc.trim(vhod) == rez


@pytest.mark.positive.test
@pytest.mark.parametrize("vhod, rez", [("Good", "G"), ("good", "d"),
                                       ("Hello world", "w")])
def test_pozitive_cont(vhod, rez):
    proc = StringUtils().contains(vhod, rez)
    assert proc


@pytest.mark.negative.test
@pytest.mark.parametrize("vhod, rez", [("Good", "t"), ("Good", "g"),
                                       (" ", "o"), ("", " ")])
def test_neganiv_cont(vhod, rez):
    proc = StringUtils().contains(vhod, rez)
    assert not proc


@pytest.mark.positive.test
@pytest.mark.parametrize("vhod, isk, rez", [("Good", "o", "Gd"),
                                            (" Good", "d", " Goo"),
                                            ("Good", "ood", "G")])
def test_pozitive_del(vhod, isk, rez):
    proc = StringUtils()
    assert proc.delete_symbol(vhod, isk) == rez


@pytest.mark.negative.test
@pytest.mark.parametrize("vhod, isk, rez", [(" good", " ", "good"),
                                            (" . ", ".", "  "), ("", "g", ""),
                                            (" ", " ", "")])
def test_neganiv_del(vhod, isk, rez):
    proc = StringUtils()
    assert proc.delete_symbol(vhod, isk) == rez

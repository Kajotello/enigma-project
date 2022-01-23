from rsc_manager import read_from_json, write_to_json
from rsc_manager import WrongPathError
import pytest


def test_read_from_json_dir_error():
    with pytest.raises(WrongPathError):
        read_from_json('/home')


def test_read_from_json_not_file():
    with pytest.raises(WrongPathError):
        read_from_json('/home/test.txt')


def test_write_to_json():
    assert 0 == 1


def test_write_to_json_dir_error():
    with pytest.raises(WrongPathError):
        write_to_json('/home', {})
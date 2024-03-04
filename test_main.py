import pytest
from main import hello

def test_main():
    assert hello() == "hello world"
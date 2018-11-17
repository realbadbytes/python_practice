import pytest

@pytest.mark.xfail
def test1():
    assert 1 == 2

def main():
    test1()

if __name__ == '__main__':
    main()

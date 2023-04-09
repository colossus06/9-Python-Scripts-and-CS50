import pytest
from seasons import life


def main():
    test_hour()
    test_min()



def test_hour():
    assert life("2022-07-03")== ("2022", "07", "03")

def test_min():
    assert life("2020-0-0")==None


if __name__ == "__main__":
    main()





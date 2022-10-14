from sys import exc_info
from src.combine import Combine
import pandas as pd

def test_add(capsys):
    files = ['./invalid.csv']
    combine = Combine()
    combine.combine_cvs(files)
    captured = capsys.readouterr()
    # when entering invalid path file, an error message should throw out
    assert captured.out == "Please enter valid csv file path.\n"





def main():
    test_add()


if __name__ == '__main__':
    main()
from src.combine import Combine
import pandas as pd

def test_add():
    files = ['./fixtures/accessories.csv', './fixtures/clothing.csv', './fixtures/household_cleaners.csv']
    combine = Combine()
    test_pd = combine.combine_cvs(files)
    expected_pd = pd.read_csv('./output.csv')
    # check their shape are the same
    assert(test_pd.shape) == (expected_pd.shape)
    col = test_pd.shape[1]
    for index, row in expected_pd.iterrows():
        for j in range(col):
            # check each row, each col are the same
            assert(row[j]) == (test_pd.iloc[index,j])



def main():
    test_add()


if __name__ == '__main__':
    main()
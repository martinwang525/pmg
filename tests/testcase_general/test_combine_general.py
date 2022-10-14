from src.combine import Combine
import pandas as pd
import os

def test_add():
    # handle absolute path of test tiles
    current_path = os.path.abspath(__file__)
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    files = ['/fixtures/accessories.csv', '/fixtures/clothing.csv', '/fixtures/household_cleaners.csv']
    for i in range(len(files)):
        files[i] = father_path + files[i]
    
    combine = Combine()
    # execute main function
    test_pd = combine.combine_cvs(files)
    # pre-written output file
    expected_pd = pd.read_csv(father_path+'/output.csv')
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
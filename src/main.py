import sys
import pandas as pd
from combine import Combine

def main():
    files = sys.argv[1:]
    if files:
        combine = Combine()
        res = combine.combine_cvs(files)
        combine.output_csv(res)
    else:
        print("Please enter at least one valid csv file.")
    

if __name__ == '__main__':
    main()
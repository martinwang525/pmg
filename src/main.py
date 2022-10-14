import sys
import pandas as pd
from combine import Combine

def main():
    # get csv file paths from command line
    files = sys.argv[1:]
    # validation of input
    if files:
        combine = Combine()
        # combine dataframe
        res = combine.combine_cvs(files)
        # output the dataframe into csv file
        combine.output_csv(res)
    # error input catch
    else:
        print("Please enter at least one valid csv file.")
    

if __name__ == '__main__':
    main()
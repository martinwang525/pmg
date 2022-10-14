from datetime import datetime
from tracemalloc import start
import pandas as pd

class Combine:

    """
    combine csv files given their file path
    """
    def combine_cvs(self,files):
        df_list = []
        try:
            # Loop through each csv file
            for path in files:
                # Read 50000 rows each time to prevent memory run out for big csv
                reader = pd.read_csv(path, chunksize=50000)
                path_list = path.split('/')
                file_name = path_list[-1]
                chunk_list = []
                for chunk in reader:
                    # Add new column with the filename
                    chunk['filename'] = file_name
                    chunk_list.append(chunk)
                # Concatenate each chunk
                ans = pd.concat(chunk_list, ignore_index=True)
                df_list.append(ans)
            # Combine each csv file
            result = pd.concat(df_list, ignore_index=True)
            return result
        except OSError:
            print('Please enter valid csv file path.')

    """
    output the script into a new csv file
    """
    def output_csv(self,pd):
        try:
            pd.to_csv('./combine.csv', index=None)  
        except AttributeError:
            print('Cannot generate combine.csv due to invalid input file')        

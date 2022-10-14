# CSV Combiner

## Before started
Please make sure that you have installed python 3.x, pytest, and pandas on your computer.

You can install pandas by running the following command on your terminal:
```
$ pip install pandas
```
You can install pytest by running the following command on your terminal:
```
$ pip install -U pytest
```


## Main function
Please make sure that you open the terminal in the `/src` file, then you can execute the following command:

```
$ python main.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv
```

The output script will be stored in the file `combined.csv`.

You can change csv files in the `/src/fixtures` folder to test different inputs.


## Unit test
The unit tests are developed using the pytest framework. Please make sure that you run the unit test starting with the keyword "pytest".

For example, if you're in the root(`/pmg` foler), you can execute the following command:

```
$ pytest tests/testcase_multiple_columns/test_combine_multiple_columns.py
```

It will run the unit test for csv files with multiple columns. You can see Passed on the terminal if the unit test passed.




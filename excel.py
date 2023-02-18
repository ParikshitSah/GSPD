import pandas as pd


def read_file(column,path):
    """Takes a csv file and returns a list with the values in column name

    Args:
        path (String): location of the csv file
        column (String): csv file header name

    Returns:
        list: Column values in list form
    """
    
    # Load the Excel file into a pandas dataframe
    df = pd.read_csv(path)

    # Extract the values from a specific column using the header name
    column_values = df[column].values

    NamesExcel = [i for i in column_values]

    # Return the column values
    return NamesExcel


print(read_file('Name (Original Name)',"./2.7.2023 Budgeting and Saving Money.csv"))
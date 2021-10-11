# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, qualifying_loans):
    """Save qualifying loan data to CSV file.  

    Args:
        csvpath (Path): The csv file path.
        qualifying_loans (List): Dictionary of loan data that needs to be written to file.
    Returns:
        None
    """
    with open(csvpath, "w", newline='') as fp:
        # Open file in the path

        csvwriter = csv.writer(fp, delimiter=',')
        # Create a new CSV writer.

        # No header info. We should pass the header row as well.
        
        for loan in qualifying_loans:
        # Loop through each loan
    
            csvwriter.writerow(loan)
            # Write loan to file.
            
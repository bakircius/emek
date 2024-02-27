import pandas as pd
import numpy as np
import datetime
import time
import ast
import sosq



# Function to convert date to Unix time
def date_to_unix_time(year, month, day):
    date_time = datetime.datetime(year, month, day)
    return int(time.mktime(date_time.timetuple()))

# Function to process and count tags for a given year
def process_tags_for_year(df, year):
    start_time = date_to_unix_time(year, 1, 1)
    end_time = date_to_unix_time(year + 1, 1, 1)
    year_df = df.loc[(df["creation_date"] > start_time) & (df["creation_date"] < end_time)]
    
    # Convert tags string to list and flatten the list of lists
    tags_series = year_df["tags"].apply(ast.literal_eval).explode()
    
    # Count occurrences of each tag
    tag_counts = tags_series.value_counts().rename_axis('tag').reset_index(name=str(year))
    
    return tag_counts

# Main function to process the data
def process_data(df):
    
    # Process each year and accumulate the results
    results = [process_tags_for_year(df, year) for year in range(2008, 2024)]
    
    # Merge results for all years
    final_df = pd.concat(results, axis=1).fillna(0)
    
    # Save the final DataFrame to CSV
    final_df.to_csv("tags.csv", index=False)

# Uncomment the lines below to run the function with the file path

#query = ""

#df = sosq.get_result(query, "your_key", "your_access_token")

# process_data(df)

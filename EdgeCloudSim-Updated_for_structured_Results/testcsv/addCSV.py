# import os


# files = os.listdir('/Users/tarunrajpurohit/Bits Goa/RP/testcsv/Files/')
# filesPath = []

# for file in files:
#     filesPath.append(f"/Users/tarunrajpurohit/Bits Goa/RP/testcsv/Files/{file}")
# print(files)

# import pandas as pd

# df = pd.concat(map(pd.read_csv, filesPath), ignore_index=True)

# print(os.getcwd())
# df.to_csv('file2.csv', header=False, index=False)

import pandas as pd
import glob

# Path of the directory containing the CSV files to merge
path = '/Users/tarunrajpurohit/Bits Goa/RP/EdgeCloudSim/sim_results/ite1'

# Get a list of all CSV files in the directory
all_files = glob.glob(path + "/*.csv")

# Read each CSV file into a pandas dataframe and append it to a list
dfs = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    dfs.append(df)

# Merge the dataframes into a single dataframe
merged_df = pd.concat(dfs, axis=0, ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged.csv', index=False)
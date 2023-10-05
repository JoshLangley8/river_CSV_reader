import pandas as pd
import glob

# Directory containing the CSV files for each month
directory_path = '/home/joshlangley/river_CSV_reader/mean_values_per_month_faure/mean/*.csv'

# Get a list of all CSV files in the directory
csv_files = glob.glob(directory_path)

# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each CSV file and concatenate the data
for csv_file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Assuming the first row contains column names and the second row contains data
    # We'll skip the first row (header) and set the first row as the header
    df = pd.read_csv(csv_file, skiprows=1, header=None)
    df.columns = ['mon_feature_id', 'sample_begin_depth', 'Ca_Diss_Water', 'Cl_Diss_Water',
                  'DMS_Tot_Water', 'EC_Phys_Water', 'F_Diss_Water', 'K_Diss_Water', 'Mg_Diss_Water',
                  'Na_Diss_Water', 'NH4_N_Diss_Water', 'NO3_NO2_N_Diss_Water', 'P_Tot_Water', 'pH_Diss_Water',
                  'PO4_P_Diss_Water', 'Si_Diss_Water', 'SO4_Diss_Water', 'TAL_Diss_Water']
    
    # Append the DataFrame to the combined DataFrame
    combined_df = pd.concat([combined_df, df], axis=0, ignore_index=True)

# Reset the index of the combined DataFrame
combined_df.reset_index(drop=True, inplace=True)

# Write the combined DataFrame to a new CSV file representing the yearly report
combined_df.to_csv('faure_mean.csv', index=False)

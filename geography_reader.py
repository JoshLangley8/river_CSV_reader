import pandas as pd
import os

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class CSVDataManipulator:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
    
    def display_data(self):
        print(self.df)
    
    def filter_monthly_data(self, month):
        # Extract only the entries for the specified month
        self.df['date_time'] = pd.to_datetime(self.df['date_time'])
        monthly_data = self.df[self.df['date_time'].dt.month == month]
        return monthly_data
    
    def calculate_mean(self, data):
        # Calculate mean for numerical columns
        numerical_columns = data.select_dtypes(include='number')
        mean_values = numerical_columns.mean()
        return mean_values

    def calculate_max(self, data):
        numerical_columns = data.select_dtypes(include='number')
        max_values = numerical_columns.max()
        return max_values

    def calculate_min(self, data):
        numerical_columns = data.select_dtypes(include='number')
        min_values = numerical_columns.min()
        return min_values
    
    def save_to_csv(self, data, output_path):
        data.to_csv(output_path, index=False)

    def calculate_and_save_max_for_all_months(self, output_directory):

        # Initialize an empty DataFrame to store max values for all months
        max_values_all_months = pd.DataFrame()

        for month in range(1, 13):
            # Filter data for the current month
            monthly_data = self.filter_monthly_data(month)

            # Calculate max for the current month's data
            max_values = self.calculate_max(monthly_data)

            # Add the max values for the current month to the combined DataFrame
            max_values_all_months = max_values_all_months._append(pd.DataFrame(max_values).T)

        # Generate the output path for the combined max values
        output_path_max_combined = os.path.join(output_directory, 'max_values_combinedEdit.csv')

        # Save the combined max values to a CSV file
        self.save_to_csv(max_values_all_months, output_path_max_combined)
        print(f"Combined max values for all months saved to {output_path_max_combined}.")

    def calculate_and_save_mean_for_all_months(self, output_directory):

        # Initialize an empty DataFrame to store max values for all months
        mean_values_all_months = pd.DataFrame()

        for month in range(1, 13):
            # Filter data for the current month
            monthly_data = self.filter_monthly_data(month)

            # Calculate max for the current month's data
            mean_values = self.calculate_mean(monthly_data)

            # Add the max values for the current month to the combined DataFrame
            mean_values_all_months = mean_values_all_months._append(pd.DataFrame(mean_values).T)

        # Generate the output path for the combined max values
        output_path_mean_combined = os.path.join(output_directory, 'mean_values_combinedEdit.csv')

        # Save the combined max values to a CSV file
        self.save_to_csv(mean_values_all_months, output_path_mean_combined)
        print(f"Combined max values for all months saved to {output_path_mean_combined}.")

    def calculate_and_save_min_for_all_months(self, output_directory):

        # Initialize an empty DataFrame to store max values for all months
        min_values_all_months = pd.DataFrame()

        for month in range(1, 13):
            # Filter data for the current month
            monthly_data = self.filter_monthly_data(month)

            # Calculate max for the current month's data
            min_values = self.calculate_min(monthly_data)

            # Add the max values for the current month to the combined DataFrame
            min_values_all_months = min_values_all_months._append(pd.DataFrame(min_values).T)

        # Generate the output path for the combined max values
        output_path_min_combined = os.path.join(output_directory, 'min_values_combinedEdit.csv')

        # Save the combined max values to a CSV file
        self.save_to_csv(min_values_all_months, output_path_min_combined)
        print(f"Combined max values for all months saved to {output_path_min_combined}.")

# Example usage
if __name__ == "__main__":
    # Path to the CSV file

    location = "faure"
    csv_file_path = f'/home/joshlangley/river_CSV_reader/{location}/{location}Edited.csv'

    # Instantiate the CSVDataManipulator
    data_manipulator = CSVDataManipulator(csv_file_path)

    # Example: Calculate max for each month and save to separate CSV files
    output_directory = f'{location}'
    data_manipulator.calculate_and_save_max_for_all_months(output_directory)
    data_manipulator.calculate_and_save_mean_for_all_months(output_directory)
    data_manipulator.calculate_and_save_min_for_all_months(output_directory)
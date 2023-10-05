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

    def calculate_max(self,data):
        numerical_columns = data.select_dtypes(include='number')
        max_values = numerical_columns.max()
        return max_values

    def calculate_min(self,data):
        numerical_columns = data.select_dtypes(include='number')
        min_values = numerical_columns.min()
        return min_values
    
    def save_to_csv(self, data, output_path):
        data.to_csv(output_path, index=False)

    def calculate_and_save_mean_for_each_month(self, output_directory):
        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)

        for month in range(1, 13):
            # Filter data for the current month
            monthly_data = self.filter_monthly_data(month)

            # Calculate mean for the current month's data
            mean_values = self.calculate_mean(monthly_data)
            max_values = self.calculate_max(monthly_data)
            min_values = self.calculate_min(monthly_data)
            
            # Generate the output path for the current month
            output_path = os.path.join(output_directory, f'mean_values_month_({month})_{months[month-1]}.csv')
            output_path1 = os.path.join(output_directory, f'max_values_month_({month})_{months[month-1]}.csv')
            output_path2 = os.path.join(output_directory, f'min_values_month_({month})_{months[month-1]}.csv')

            # Save the mean values to a new CSV file for the current month
            self.save_to_csv(pd.DataFrame(mean_values).T, output_path)
            self.save_to_csv(pd.DataFrame(max_values).T, output_path1)
            self.save_to_csv(pd.DataFrame(min_values).T, output_path2)
            print(f"Mean values for month {month} saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Path to the CSV file
    csv_file_path = '/home/joshlangley/HayleyScripts/kleinplaas.csv'

    # Instantiate the CSVDataManipulator
    data_manipulator = CSVDataManipulator(csv_file_path)

    # Example: Calculate mean for each month and save to separate CSV files
    output_directory = 'mean_values_per_month_kleinplaas'
    data_manipulator.calculate_and_save_mean_for_each_month(output_directory)

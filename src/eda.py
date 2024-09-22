import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ydata_profiling


class EDA:
    def __init__(self, data):
        self.data = data

    def basic_info(self):
        print("Data Information:")
        print(self.data.info())
        print("\nStatistical Overview:")
        print(self.data.describe())
    
    def data_profile(self, output_file="eda_report.html"):
        profile = ydata_profiling.ProfileReport(self.data, title="Profiling Report")
        profile.to_file(output_file)  # Save the report to an HTML file
        print(f"Profiling report saved as {output_file}")
        return profile

    def missing_values(self):
        missing_data = self.data.isnull().sum()
        missing_percentage = (missing_data / len(self.data)) * 100
        print("Missing Data (Count):")
        print(missing_data[missing_data > 0])
        print("\nMissing Data (Percentage):")
        print(missing_percentage[missing_percentage > 0])

    def distribution(self):
        for col in self.data.select_dtypes(include=['object']).columns:
            print(f"\n{col} Distribution:")
            print(self.data[col].value_counts())
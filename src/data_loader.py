import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if self.file_path.endswith('.xlsx'):
            data = pd.read_excel(self.file_path)
        elif self.file_path.endswith('.csv'):
            data = pd.read_csv(self.file_path)
        else:
            raise ValueError("Unsupported file format.")
        return data

    def check_data_format(self):
        print(f"File path: {self.file_path}")
        if self.file_path.endswith('.xlsx'):
            print("Data format: Excel")
        elif self.file_path.endswith('.csv'):
            print("Data format: CSV")
        else:
            print("Unsupported format.")
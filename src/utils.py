import pandas as pd
import os

class InsuranceDataUtils:
    def __init__(self, csv_file_path, cleaned_csv_file_path):
        self.csv_file_path = csv_file_path
        self.cleaned_csv_file_path = cleaned_csv_file_path
    
    def load_data(self):
        # Load data with specified dtypes
        dtype = {
            'Bank': str,
            'AccountType': str,
            'MaritalStatus': str,
            'Gender': str,
            'VehicleType': str,
            'make': str,
            'Model': str,
            'Cylinders': float,
            'cubiccapacity': float,
            'kilowatts': float,
            'bodytype': str,
            'NumberOfDoors': float,
            'VehicleIntroDate': str
        }
        return pd.read_csv(self.csv_file_path, dtype=dtype, low_memory=False)
    
    def clean_data(self, df):
        # Drop columns with a high proportion of missing values
        threshold = 0.5
        df_cleaned = df.dropna(thresh=len(df) * (1 - threshold), axis=1)
        
        # Drop rows with missing values in specific columns
        columns_to_check = ['Bank', 'AccountType', 'MaritalStatus', 'Gender']
        df_cleaned = df_cleaned.dropna(subset=columns_to_check)
        
        # Fill missing values with mode or default values
        df_cleaned['Bank'] = df_cleaned['Bank'].fillna(df_cleaned['Bank'].mode()[0])
        df_cleaned['AccountType'] = df_cleaned['AccountType'].fillna(df_cleaned['AccountType'].mode()[0])
        df_cleaned['Gender'] = df_cleaned['Gender'].fillna(df_cleaned['Gender'].mode()[0])
        df_cleaned['VehicleType'] = df_cleaned['VehicleType'].fillna('Unknown')
        
        # Forward fill for VehicleIntroDate
        df_cleaned['VehicleIntroDate'] = df_cleaned['VehicleIntroDate'].ffill()
        
        return df_cleaned
    
    def save_data(self, df):
        df.to_csv(self.cleaned_csv_file_path, index=False)


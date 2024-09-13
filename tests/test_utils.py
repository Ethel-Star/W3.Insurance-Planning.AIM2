# tests/test_utils.py
import pytest
from src.utils import InsuranceDataUtils

def test_load_data():
    # Example test for load_data method
    utils = InsuranceDataUtils(
    r'E:\2017.Study\Tenx\Week-3\Data\data\raw_data.csv',
    r'E:\2017.Study\Tenx\Week-3\Data\data\cleaned_data.csv'
    )

    df = utils.load_data()
    assert df is not None
    assert 'Bank' in df.columns

def test_clean_data():
    # Example test for clean_data method
    data = {
        'Bank': [None, 'Bank A', 'Bank B'],
        'AccountType': [None, 'Savings', 'Checking'],
        'MaritalStatus': [None, 'Single', 'Married'],
        'Gender': [None, 'Male', 'Female'],
        'VehicleType': [None, 'SUV', 'Sedan'],
        'VehicleIntroDate': [None, '2020-01-01', '2021-01-01']
    }
    df = pd.DataFrame(data)
    utils = InsuranceDataUtils('path/to/raw_data.csv', 'path/to/cleaned_data.csv')
    df_cleaned = utils.clean_data(df)
    
    assert df_cleaned['Bank'].notna().all()  # Check that 'Bank' column has no NaN values
    assert df_cleaned['AccountType'].notna().all()  # Check 'AccountType'
    assert df_cleaned['Gender'].notna().all()  # Check 'Gender'
    assert df_cleaned['VehicleType'].notna().all()  # Check 'VehicleType'
    assert df_cleaned['VehicleIntroDate'].notna().all()  # Check 'VehicleIntroDate'

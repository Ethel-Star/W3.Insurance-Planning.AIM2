import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_ind, chi2_contingency
class InsuranceDataUtils:
    def __init__(self, df):
        """
        Initializes the InsuranceDataUtils with a DataFrame.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("The input must be a pandas DataFrame.")
        self.df = df
        # A/B Hypothesis Testing
    def categorize_provinces(self, metric_col):
        """
        Categorize provinces into high-risk and low-risk based on the average value of a given metric.

        Parameters:
        - metric_col: The column name of the metric to use for categorization ('TotalClaims').

        Returns:
        - high_risk_provinces: List of high-risk provinces.
        - low_risk_provinces: List of low-risk provinces.
        """
        # Calculate average metric per province
        province_avg = self.df.groupby('Province')[metric_col].mean().reset_index()
        province_avg.columns = ['Province', 'AverageMetric']
        
        # Calculate the overall average metric
        overall_avg = province_avg['AverageMetric'].mean()
        
        # Define risk groups
        high_risk_provinces = province_avg[province_avg['AverageMetric'] > overall_avg]['Province'].tolist()
        low_risk_provinces = province_avg[province_avg['AverageMetric'] <= overall_avg]['Province'].tolist()
        
        return high_risk_provinces, low_risk_provinces

    def test_risk_differences(self, metric_col, high_risk_provinces, low_risk_provinces):
        """
        Test for significant differences in risk between high-risk and low-risk provinces.

        Parameters:
        - metric_col: The column name of the metric to analyze (e.g., 'TotalClaims').
        - high_risk_provinces: List of provinces classified as high-risk.
        - low_risk_provinces: List of provinces classified as low-risk.

        Returns:
        - t_statistic: The t-statistic of the test.
        - p_value: The p-value of the test.
        - interpretation: Interpretation of the results.
        """
        # Filter data for each group
        group_a_data = self.df[self.df['Province'].isin(high_risk_provinces)][metric_col]
        group_b_data = self.df[self.df['Province'].isin(low_risk_provinces)][metric_col]
        
        # Check if there is enough data in each group
        if len(group_a_data) == 0 or len(group_b_data) == 0:
            raise ValueError("One or both of the groups have no data. Please check the group names and data.")
        
        # Perform t-test
        t_statistic, p_value = stats.ttest_ind(group_a_data, group_b_data, equal_var=False)
        
        # Interpretation
        if p_value < 0.05:
            interpretation = "Reject the null hypothesis: There are significant differences in risk."
        else:
            interpretation = "Fail to reject the null hypothesis: No significant differences in risk."
        
        return t_statistic, p_value, interpretation

    def print_summary(self, t_statistic, p_value, interpretation):
        """
        Print the summary of the test results.
        """
        print(f"T-statistic: {t_statistic:.4f}")
        print(f"P-value: {p_value:.4f}")
        print(f"Interpretation: {interpretation}")


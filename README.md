# AlphaCare Insurance Solutions - Insurance Planning and Marketing Analysis

## Overview

This project is focused on analyzing historical insurance claim data for AlphaCare Insurance Solutions (ACIS) with the goal of enhancing marketing strategies and identifying low-risk targets to optimize premium rates. This will help attract new clients and improve the efficiency of marketing efforts in South Africa.

## Task 1: Git and GitHub

In Task 1, the objective is to set up a robust version control system using Git and GitHub. This involves creating a new Git repository for the week’s work, ensuring that all code is tracked and versioned appropriately. Key activities include implementing Git version control to manage changes through commits and branches, and setting up continuous integration and deployment (CI/CD) using GitHub Actions. This will automate the testing and deployment processes, ensuring consistent and reliable project updates. Additionally, exploratory data analysis (EDA) will be performed to understand the data, identify patterns, and generate insights. This includes calculating descriptive statistics, reviewing data structures, assessing data quality, and visualizing data distributions and relationships. Statistical thinking will be applied to provide evidence for actionable insights derived from EDA.

## Task 2: Data Version Control (DVC)

Task 2 involves implementing Data Version Control (DVC) to manage and track data changes efficiently. The first step is to install DVC using `pip install dvc`, followed by initializing DVC in the project directory with `dvc init`. Setting up local remote storage is crucial; this involves creating a directory for local storage and configuring DVC to use it. Once the storage is set up, datasets need to be tracked with DVC by using `dvc add` commands for each dataset file. Committing the DVC files to version control ensures that all data-related changes are tracked alongside the code. Finally, pushing the data to the local remote storage using `dvc push` ensures that the data is securely stored and accessible.

## Installation

To get started with this project, first clone the repository from GitHub. After cloning, install the necessary dependencies by running `pip install -r requirements.txt` and `pip install dvc`. This setup ensures that all required packages and tools are available for the analysis.

## Usage

Begin by initializing the Git repository with `git init`. Set up DVC by running `dvc init`, which will prepare the project for data versioning. Configure the DVC remote storage by creating a directory for storing data and adding this storage to DVC with `dvc remote add`. Track the data files using `dvc add` to include them in the version control system. Commit the changes to Git to save the DVC configuration and data tracking setup. Finally, push the data to the remote storage with `dvc push` to ensure that it is securely saved and versioned.

## Data Files

The project includes two main data files: `raw_data.csv` and `cleaned_data.csv`. The `raw_data.csv` file contains the initial raw insurance claim data, while `cleaned_data.csv` includes the processed data with cleaned entries, ready for analysis.

## Analysis

Exploratory Data Analysis (EDA) will be conducted to gain a comprehensive understanding of the data. This includes calculating descriptive statistics for numerical features like TotalPremium and TotalClaim, verifying the data types of each column, and assessing the presence of missing values. Univariate analysis will involve plotting histograms and bar charts to explore the distribution of individual variables, while bivariate and multivariate analysis will examine relationships between variables such as TotalPremium and TotalClaims. Data comparison will focus on trends over geography, and outlier detection will use visual methods like box plots. Additionally, creative and insightful plots will be produced to effectively communicate key findings from the analysis.

For machine learning and statistical modeling, a linear regression model will be developed to predict total claims for each zip code. A predictive model will be created to estimate optimal premium values based on various features, including those related to the car, owner, location, and other relevant factors. The final report will detail the methodologies used, present the findings, and offer recommendations for modifying or enhancing insurance products based on the analysis results.

## Contributing

Contributions to this project are welcome. If you have improvements or additional features to add, please fork the repository, make your changes, and submit a pull request with a detailed description of the modifications.

## License

This project is licensed under the Apache License. For more details, please refer to the [LICENSE](LICENSE) file.

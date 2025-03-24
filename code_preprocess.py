import pandas as pd

# File paths
file1 = r"D:\Downloads-E\shanmugapriyaproject\Project 2 - birds species\Bird_Monitoring_Data_FOREST.XLSX"
file2 = r"D:\Downloads-E\shanmugapriyaproject\Project 2 - birds species\Bird_Monitoring_Data_GRASSLAND.XLSX"


# Function to read all sheets from an Excel file
def read_all_sheets(file_path):
    excel_data = pd.ExcelFile(file_path)  # Load the Excel file
    sheet_dfs = [excel_data.parse(sheet_name) for sheet_name in excel_data.sheet_names]  # Read all sheets
    return pd.concat(sheet_dfs, ignore_index=True)  # Combine all sheets

# Read all sheets from both files
df1 = read_all_sheets(file1)
df2 = read_all_sheets(file2)

# Combine both datasets into a single DataFrame
combined_df = pd.concat([df1, df2], ignore_index=True)

# Save the final cleaned dataset
combined_csv_path = combined_csv_path = r"D:\Downloads-E\shanmugapriyaproject\Project 2 - birds species\Cleaned_Bird_Monitoring_Data.csv"

combined_df.to_csv(combined_csv_path, index=False)

print(f"✅ Combined dataset saved successfully as '{combined_csv_path}'!")
import pandas as pd

# Enable new Pandas behavior
pd.set_option('future.no_silent_downcasting', True)

def preprocess_bird_data(input_path, output_path):
    # Load dataset
    df = pd.read_csv(input_path)

    # Step 1: Remove columns that are 80% empty
    threshold = 0.8 * len(df)
    df = df.loc[:, df.isnull().sum() < threshold]

    # Step 2: Identify categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

    # Step 3: Fill missing values correctly
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            mode_value = df[col].mode()[0]
            df[col] = df[col].fillna(mode_value)  

    df = df.infer_objects(copy=False)  # Explicitly infer types

    for col in numerical_cols:
        if df[col].isnull().sum() > 0:
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)

    # Step 4: Save cleaned dataset
    df.to_csv(output_path, index=False)

    print(f"✅ Preprocessing complete! Cleaned data saved at: {output_path}")
    return df

# Updated file paths
file_path = r"D:\Downloads-E\shanmugapriyaproject\Project 2 - birds species\Cleaned_Bird_Monitoring_Data.csv"
output_path = r"D:\Downloads-E\shanmugapriyaproject\Project 2 - birds species\preprocessed_data.csv"

# Run preprocessing
cleaned_df = preprocess_bird_data(file_path, output_path)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the preprocessed dataset
file_path = r"D:\Downloads-E\shanmugapriyaproject\Project 2 - birds species\preprocessed_data.csv"
df = pd.read_csv(file_path)

# Display basic info
print(df.info())  # Check column types & missing values
print(df.describe())  # Summary of numerical columns
print(df.head())  # Preview first few rows
df['Date'] = pd.to_datetime(df['Date'])
df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%H:%M:%S').dt.time
df['End_Time'] = pd.to_datetime(df['End_Time'], format='%H:%M:%S').dt.time
plt.figure(figsize=(10,5))
df['Year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("Bird Sightings Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Sightings")
plt.show()
top_species = df['Common_Name'].value_counts().head(10)
plt.figure(figsize=(10,5))
top_species.plot(kind='bar', color='green')
plt.title("Top 10 Most Observed Bird Species")
plt.xlabel("Species")
plt.ylabel("Observations Count")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8,5))
df['Location_Type'].value_counts().plot(kind='bar', color=['brown', 'green'])
plt.title("Bird Observations by Habitat")
plt.xlabel("Location Type")
plt.ylabel("Number of Sightings")
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Sky'], y=df['Temperature'], palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Temperature Distribution Based on Sky Condition")
plt.show()
top_observers = df['Observer'].value_counts().head(10)
plt.figure(figsize=(10,5))
top_observers.plot(kind='bar', color='purple')
plt.title("Top 10 Observers with Most Sightings")
plt.xlabel("Observer")
plt.ylabel("Number of Sightings")
plt.xticks(rotation=45)
plt.show()









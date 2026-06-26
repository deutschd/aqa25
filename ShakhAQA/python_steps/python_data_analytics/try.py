import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

median_salary_year = df['salary_year_avg'].median()
#%%
median_salary_hour = df['salary_hour_avg'].median()
#%%
df_filled = df

print(df_filled['salary_year_avg'].fillna(median_salary_year))
print(['salary_hour_avg'].fillna(median_salary_hour))
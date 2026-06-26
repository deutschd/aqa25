# if True:
#     print("What's up Data Nerds")
# years_experience = 3
# job_skill = 'SQL'
# applicant_skill = 'Python'
# # if job_skill == applicant_skill:
# #     print("Skills Match!")
# # elif years_experience >= 5:
# #     print("Enough Experience: No SQL")
# # elif applicant_skill == 'Python':
# #     pass
# #     print("This applicant should know SQL")
# # else:
# #     print('No skill or experience')
#
# if job_skill == applicant_skill:
#     ...
from unittest.mock import inplace

import pd
from datasets import load_dataset

print('\nA little bit training with Pandas')
import pandas as pd
# df = pd.read_csv(r"D:\LEARNING\PythonPRO\car_prices.csv")
# print(df.head())
# print(df.info())
#
# print(type(df))

# print(df['sellingprice'])
# print(df.sellingprice[0])
# print(df.make[2])

# from datasets import load_dataset
# load_dataset('lukebarousse/data_jobs')

# dataset = load_dataset('lukebarousse/data_jobs')
# print(type(dataset['train']))
#
# print(dataset['train'].to_pandas())
#
# df = dataset['train'].to_pandas()
# print(df.info())


print('\nA little bit training with Pandas')
import pandas as pd
from datasets import load_dataset
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()
# print(df.head(10))
# print(df.tail(3))
# print(df['job_title_short'].head(5))
# print(df[['job_title_short', 'job_location']].head(5))
# print(df.iloc[90:100, 0:2])
# print(df.info())
# print(df.shape)
# print(df.describe())
# print(df.job_title_short.unique())
# print(df.job_title_short == 'Data Analyst') # if it's inside of it True False
# print(df[df.job_title_short == 'Data Analyst']) # if it's inside of it True False
# print(df[(df.job_title_short == 'Data Analyst') & (df.salary_year_avg.notna())])
print(df.info())
print(type(df.job_posted_date[0]))
print(pd.to_datetime(df.job_posted_date))
print(df.info())
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
print(df.info())
print(df.job_posted_date.dt.month)
df.job_posted_month = df.job_posted_date.dt.month
print(df.info())
df.sort_values('job_posted_date')
df.sort_values('job_posted_date', inplace=True)

print(df.drop(labels='salary_hour_avg', axis=1, inplace=True))
df.dropna(subset=['salary_year_avg'], inplace=True)
print(df.info())








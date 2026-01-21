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

print('\nA little bit training with Pandas')
import pandas as pd
df = pd.read_csv(r"D:\LEARNING\PythonPRO\car_prices.csv")
print(df.head())
print(df.info())

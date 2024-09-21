import pandas as pd
file_path = 'Employees.csv'
df = pd.read_csv(file_path)
df= df.drop_duplicates()
df['Age'] = df['Age'].astype(int)
df['Salary(EGP)'] = df['Salary(USD)'] * 50
df.drop('Salary(USD)', axis=1, inplace=True) 
average_age = df['Age'].mean() 
median_salary = df['Salary(EGP)'].median()
male_count = df[df['Gender'] == 'M'].shape[0] 
female_count = df[df['Gender'] == 'F'].shape[0]  
if female_count > 0:
    ratio = male_count / female_count
else:
    ratio = 'No female employees'
print(f'Average age: {average_age}')
print(f'Median salary: {median_salary}')
print(f'Ratio of males to females: {ratio}')
df.to_csv('new_Employees.csv', index=False)
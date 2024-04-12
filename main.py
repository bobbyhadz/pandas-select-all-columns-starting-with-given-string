# Select all Columns starting with a given String in Pandas

import pandas as pd

df = pd.DataFrame({
    'Employee_ID': [1, 2, 3, 4],
    'Employee_Name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'Age': [29, 30, 31, 32],
    'Employee_Salary': [1500, 1000, 2000, 3000],
})

column_names = [column for column in df
                if column.startswith('Employee')]

# 👇️ ['Employee_ID', 'Employee_Name', 'Employee_Salary']
print(column_names)

print('-' * 50)

#    Employee_ID Employee_Name  Employee_Salary
# 0            1         Alice             1500
# 1            2         Bobby             1000
# 2            3          Carl             2000
# 3            4           Dan             3000
print(df[column_names])
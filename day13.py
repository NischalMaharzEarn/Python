import pandas as pd
#df = pd.read_csv('data.csv')
#print(df['Calories'].std())
salary = [515,62,62,65,16,233,451]
s = pd.series(salary)
print(s.median())
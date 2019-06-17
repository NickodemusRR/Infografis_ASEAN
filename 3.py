import sqlalchemy
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

engine = sqlalchemy.create_engine(
    'mysql+pymysql://guest:12345CobaFlask@localhost:3306/world'
)
query = "select Name, GNP from country where region = 'Southeast Asia' order by Name"
df = pd.read_sql(query, engine)
# print(df)

plt.figure('Pendapatan Bruto Nasional Asean', figsize=(10,8))
plt.style.use('seaborn-whitegrid')
plt.bar(df['Name'], df['GNP'], width=0.6, color=['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple', 'pink', 'brown', 'grey'])
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.xticks(rotation=20)
plt.xlabel('Negara')
plt.ylabel('Gross National Product (US$)')

for i, j in enumerate(df['GNP']):
    plt.text(i-.25, j, str(j), color='black')

plt.show()
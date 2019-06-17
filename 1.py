import sqlalchemy
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

engine = sqlalchemy.create_engine(
    'mysql+pymysql://guest:12345CobaFlask@localhost:3306/world'
)
query = "select Name, Population from country where region = 'Southeast Asia' order by Name"
df = pd.read_sql(query, engine)
# print(df)

plt.figure('Populasi Negara Asean', figsize=(15,10))
plt.style.use('seaborn-whitegrid')
plt.bar(df['Name'], df['Population'], width=0.6, color=['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple', 'pink', 'brown', 'grey'])
plt.title('Populasi Negara ASEAN')
plt.xticks(rotation=20)
plt.xlabel('Negara')
plt.ylabel('Populasi (x100 juta jiwa)')

for i, j in enumerate(df['Population']):
    plt.text(i-.3, j, str(j), color='black')

plt.show()
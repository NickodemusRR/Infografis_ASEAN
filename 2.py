import sqlalchemy
import pandas as pd 
import matplotlib.pyplot as plt 

engine = sqlalchemy.create_engine(
    'mysql+pymysql://guest:12345CobaFlask@localhost:3306/world'
)
query = "select Name, Population from country where region = 'Southeast Asia' order by Name"
df = pd.read_sql(query, engine)

plt.figure('Persentase Penduduk Asean', figsize=(10,8))
plt.pie(df['Population'], labels=df['Name'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('Persentase Penduduk ASEAN')

plt.show()
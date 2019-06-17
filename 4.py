import sqlalchemy
import pandas as pd 
import matplotlib.pyplot as plt 

engine = sqlalchemy.create_engine(
    'mysql+pymysql://guest:12345CobaFlask@localhost:3306/world'
)
query = "select Name, SurfaceArea from country where region = 'Southeast Asia' order by Name"
df = pd.read_sql(query, engine)
# print(df)

plt.figure('Persentase Luas Daratan Asean', figsize=(10,8))
plt.pie(df['SurfaceArea'], labels=df['Name'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('Persentase Luas Daratan ASEAN')

plt.show()
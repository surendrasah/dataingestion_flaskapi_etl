import pandas as pd
from sqlalchemy import create_engine, inspect
import os

engine = create_engine('sqlite:///' + os.path.join(os.getcwd(), 'data.db'))

inspector = inspect(engine)
print(inspector.get_table_names())

machine_data = pd.read_sql_table('machine_data', engine)
production_data = pd.read_sql_table('production_data', engine)
merged_data = pd.merge(machine_data, production_data, on='time')

print("all the merged data\n", merged_data.head())

# Group the merged DataFrame by 'product' and calculate the correlation between each machine parameter and 'production'
correlations = merged_data.groupby('product').corr()['production']

# Print the top three machine parameters that have the highest correlation with 'production' for each product
for product, product_correlations in correlations.groupby(level=0):
    print(f'Top three parameters for {product}:')
    print(product_correlations.sort_values(ascending=False).iloc[1:4])

# Output the result to a CSV file
df = pd.DataFrame(correlations)
df.to_csv('correlations.csv', index=False)

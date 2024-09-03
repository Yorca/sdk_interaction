import pandas as pd

df = pd.read_excel('SDK Interaction_raw_3types.xlsx')

df_combined = df.groupby('SDK Name')['Type'].apply(lambda x: ','.join(x)).reset_index()

df_combined.to_excel('processed_file_3types.xlsx', index=False)
import os
import pandas as pd
import glob

files = glob.glob(os.path.dirname(__file__) + "/data/*")

renamed_columns = {}
new_values = ("date", "close", "open", "high", "low", "volume", "delete", "type", "description")
new_values_list = list(new_values)
new_values_list.remove('delete')
df_final = pd.DataFrame(columns=new_values_list)

for file in files:
    type_descrption = os.path.basename(file).split('.')[0].split('_')

    df = pd.read_csv(file)
    df['type'] = type_descrption[0]
    df['description'] = type_descrption[1]

    for index, element in enumerate(list(df)):
        renamed_columns[element] = new_values[index]
    df.rename(columns=renamed_columns, inplace=True)

    df.drop(columns=['delete'], inplace=True)

    df_final = pd.concat([df_final, df], ignore_index=True)

df_final.to_csv(os.path.dirname(__file__) + '/data.csv', index=False)
print(df_final)

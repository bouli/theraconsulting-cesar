import xml.etree.ElementTree as ET
import re, os
import pandas as pd
import numpy as np

tree = ET.parse(os.path.dirname(__file__) + '/data/news_formated.xml')
root = tree.getroot()

last_index = np.nan

df = pd.DataFrame(columns=['date', 'description', 'actual_state', 'close', 'forecast'])

for news in root.iter('news'):

    numbers = re.findall(r"[-+]?\d*\.\d+", news.find('preview').text)
    last_index = numbers[0]
    if len(numbers) == 1:
        numbers.append(last_index)

    if len(numbers) == 2:
        numbers.append(np.nan)

    df_append = pd.DataFrame(
        {
            'date': [news.find('date').text],
            'description': ['chinese-caixin-services-pmi-596'],
            'actual_state': [numbers[1]],
            'close': [numbers[0]],
            'forecast': [numbers[2]]
        }, )

    df = pd.concat([df, df_append], ignore_index=True)
df.to_csv(os.path.dirname(__file__) + '/data.csv', index=False)

print(os.path.dirname(__file__).split('/')[-1] + " data loaded successfully!")

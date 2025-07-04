###
import xml.etree.ElementTree as ET
import re

tree = ET.parse('data/news_formated.xml')
root = tree.getroot()

fwrite = open('dump.sql', 'w+')
last_index = 'NULL'
for news in root.iter('news'):

    numbers = re.findall(r"[-+]?\d*\.\d+", news.find('preview').text)
    last_index = numbers[0]
    if len(numbers) == 1:
        numbers.append(last_index)

    if len(numbers) == 2:
        numbers.append('NULL')
    query = f"INSERT INTO EconomicCalendar (date, description, actual_state, close, forecast) VALUES ('{news.find('date').text}', 'chinese-caixin-services-pmi-596', {numbers[1]}, {numbers[0]}, {numbers[2]});\n"
    fwrite.write(query)
    print(query)

fwrite.close()


import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

url = "https://br.investing.com/economic-calendar/chinese-caixin-services-pmi-596"
conn_string = "postgresql://postgres:postgres@localhost:6500/theraconsultingcesar"
conn_string = "postgresql://postgres:postgres@db:5432/theraconsultingcesar"

response = requests.get(url)

html_parsed = BeautifulSoup(response.content, 'html.parser')
div_content = html_parsed.find("div", {"id": "releaseInfo"})
html_data = list()
for div in div_content.find_all("div"):
    internal_text = div.text.split(".")
    internal_text.reverse()
    internal_text = "-".join(internal_text)
    internal_text = internal_text.replace(",", ".")
    html_data.append(internal_text)

if len(html_data) == 4:
    data = {}
    data['date'] = html_data[0]
    data['description'] = url.split("/")[-1]
    data['actual_state'] = html_data[3]
    data['close'] = html_data[1]
    data['forecast'] = html_data[2]

    query_string = "SELECT * FROM \"EconomicCalendar\" WHERE 1 = 1 "
    query_string = query_string + " AND description = '" + data['description'] + "'"
    query_string = query_string + " AND date = '" + data['date'] + "'"
    query_string = query_string + " AND actual_state = " + data['actual_state']
    query_string = query_string + " AND close = " + data['close']
    query_string = query_string + " AND forecast = " + data['forecast']

    connection = psycopg2.connect(conn_string)
    cursor = connection.cursor()
    cursor.execute(query_string)
    cursor.close()

    if(cursor.rowcount == 0):
        db = create_engine(conn_string)
        conn = db.connect()

        df = pd.DataFrame(data, index=[0])
        df.to_sql("EconomicCalendar", con=conn, if_exists='append', index=False)

        conn.close()
        logging.error("New data added successfully!")

    else:
        logging.error("Data already exists")

else:
    logging.error("Data is not valid")

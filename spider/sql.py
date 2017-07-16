import sqlite3
import pandas

with sqlite3.connect('news.sqlite') as db:
    news = pandas.read_sql_query('SELECT * FROM news', con = db)
    print(news)
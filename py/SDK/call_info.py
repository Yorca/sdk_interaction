import sqlite3
import matplotlib.pyplot as plt
import networkx as nx

conn = sqlite3.connect('/Users/yorca/Downloads/final_filter_all_v2.db')
cursor = conn.cursor()

cursor.execute('SELECT * from sdkconnectionrough')

for row in cursor.fetchall():
    with open("call_info.txt", "a") as file:
        file.write(str(row) + "\n")

conn.close()

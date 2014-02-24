import sqlite3

connection = sqlite3.connect('magpie.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS switches
                    (name text, device text, status text, type text, slide int, alarm real)
                 """)

cursor.execute("""CREATE TABLE IF NOT EXISTS power
                (date text, power real)
             """)

cursor.execute("""CREATE TABLE IF NOT EXISTS temperature
                (temp real)
             """)

# Adding switches
cursor.execute("INSERT INTO switches VALUES ('B1', 'Fan 1', 'off', 'F', '12', '23.12')")
cursor.execute("INSERT INTO switches VALUES ('B2', 'Light 1', 'on', 'L', '15', '23.46')")
cursor.execute("INSERT INTO switches VALUES ('B3', 'Fan 2', 'on', 'F', '4', '9.30')")

# Adding power usage
cursor.execute("INSERT INTO power VALUES ('2014-02-14', 6.05)")
cursor.execute("INSERT INTO power VALUES ('2014-02-15', 12.64)")
cursor.execute("INSERT INTO power VALUES ('2014-02-16', 17.36)")

# Adding sample temperature
cursor.execute("INSERT INTO temperature VALUES (26.7)")

connection.commit()
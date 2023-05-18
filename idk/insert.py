import sqlite3

# Connect to the database
conn = sqlite3.connect("game_data.db")
cursor = conn.cursor()

# Update ability names
cursor.execute("UPDATE ability SET name = ? WHERE id = ?", ("Fireball", 1))
cursor.execute("UPDATE ability SET name = ? WHERE id = ?", ("Frost Bolt", 2))

# Update weapon names
cursor.execute("UPDATE weapon SET name = ? WHERE id = ?", ("Sword", 1))
cursor.execute("UPDATE weapon SET name = ? WHERE id = ?", ("Axe", 2))

# Commit the changes and close the connection
conn.commit()
conn.close()
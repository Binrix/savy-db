from database import Database
import error

db = Database()

# try:
#     db.create_table("Person", "Name, Vorname, Alter, Groesse")
#     db.create_table("Spiel", "Bezeichnung, Hersteller, Erscheinungsdatum")
# except error.TableAlreadyExists as error:
#     print(error.message)

# try:
#     db.insert_into("Person", "Jan, Galliker, 18, 179")
#     db.insert_into("Person", "Benjamin, Klein, 22, 176")
# except error.DatabaseError as error:
#     print(error.message)


db.set_column_as_index("Person", "Name")
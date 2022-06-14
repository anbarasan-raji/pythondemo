import db
import json

obj = db.conn.cursor()
obj.callproc("pr_get_Branch_Master")

for result in obj.stored_results():
    details = result.fetchall()

print(json.dumps(details))

obj.close()
db.conn.close()

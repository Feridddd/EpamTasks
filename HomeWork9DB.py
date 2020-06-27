import csv
from pymongo import MongoClient

mongo = MongoClient(host='localhost', port=27017)


def _connect_mongo(host, port, username, password, db):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db]


# csv files to db
csv_projects = open('projects.csv', 'r')  # file with projects
csv_tasks = open('tasks.csv', 'r')  # file with tasks

reader_proj = csv.DictReader(csv_projects)
reader_tasks = csv.DictReader(csv_tasks)
db = mongo.itest_db  # access to my db not created yet
db.projects.drop()  # Removes a projects collection
db.tasks.drop()  # Removes a tasks collection

header_projects = ["name", "description", "deadline"]
# insert projects to projects_table
for each in reader_proj:
    row = {}
    for field in header_projects:
        row[field] = each[field]
    db.projects.insert_one(row)

header_tasks = ["id", "priority", "details", "status", "deadline", "completed", "project"]
# insert_tasks_to tasks table
for each in reader_tasks:
    row = {}
    for val in header_tasks:
        row[val] = each[val]
    db.tasks.insert_one(row)

# Printing the data with done status
cursor = db.tasks.find({"status": "done"})
for record in cursor:
    print(record)

print("**************** Projects with status done *********************************")
# SELECT WHERE NAME = PROJECT
cursor_tasks = db.projects.aggregate([
    {"$lookup": {
        "from": "tasks",
        "localField": "name",
        "foreignField": "project",
        "as": "task_name"
    }
    },
    {"$match": {"task_name.status": "done"}},
    {"$project": {
        "name": 1
    }
    }
])
for i in cursor_tasks:
    print(i)

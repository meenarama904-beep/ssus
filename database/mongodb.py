from pymongo import MongoClient
try:
    Mongo_URI="mongodb+srv://meenarama904_db_user:Mahadev9981@cluster0.z4csst7.mongodb.net/?appName=Cluster0"
    client = MongoClient(Mongo_URI)
    client.admin.command("ping")
    db = client["ssus1234"]


    students_collection = db["student"]
    mark_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]


    print("mongoDB connected successfully")

except Exception as e:
    print("MongoDB Error :",e)

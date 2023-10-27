import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']
table = mydb.employee_info
record = {
    'first_name': 'Pankaj',
    'last_name': 'Rawat',
    'Age': 26
}
# add multiple objects.
records = [{
    'first_name': 'Neeraj',
    'last_name': 'Rawat',
    'Age': 20
},
{
    'first_name': 'Manoj',
    'last_name': 'Rawat',
    'Age': 22
}]
# table.insert_one(record)
table.insert_many(records)
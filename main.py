# This is a sample Python script.
import json

with open("dummydata.json") as json_file:
    print(json.load(json_file))


str = [{"_id": "60beb338abe3dd4300d844b8",
        "email": "hemitpatel0@gmail.com",
        "typeVaccine": "Moderna",
        "status": "Yes", "__v": 0},
       {
           "_id": "60bf716b145de95f1c84fb2f",
           "email": "hemit.2009@outlook.com",
           "typeVaccine": "Asternzcana",
           "status": "No", "__v": 0},
       {
           "_id": "60bf7196145de95f1c84fb31",
           "email": "hemitpatel@computer4u.com",
           "typeVaccine": "Phizer",
           "status": "Yes", "__v": 0},
       {
           "_id": "60bf758f145de95f1c84fb32",
           "email": "blahbro96@gmail.com",
           "typeVaccine": "none",
           "status": "No",
           "__v": 0},
       {
           "_id": "60bf7cda145de95f1c84fb33",
           "email": "vimal4282@yahoo.co.in",
           "typeVaccine": "Moderna",
           "status": "Yes",
           "__v": 0}
       ]
with open("dummydata3.json",'w') as new_json_file:
    json.dump(str,new_json_file)


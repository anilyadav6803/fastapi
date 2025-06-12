from fastapi import FastAPI , Path , HTTPException , Query
import json
app = FastAPI()


def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Data API is run done!"}


@app.get("/about")
def about():
    return {"message": "This API access to patient data."} 


@app.get("/view")
def view_data():
    data = load_data()
    return {"data": data}



@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to view" ,  example="P001")): 
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")



@app.get("/sort")
def sort_data(sort_by: str = Query("name", description="The field to sort by", example="name")):
    data = load_data()
    if sort_by not in ["name", "age", "id"]:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1][sort_by]))
    return {"data": sorted_data}

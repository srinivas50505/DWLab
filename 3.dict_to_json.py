import json 
employee_details={
    "Id":"1",
    "Name":"Ravi",
    "Department":"Developer"
}
json_object=json.dumps(employee_details,indent=4)
print("employee_details\n",employee_details)
print("json_details\n",json_object)
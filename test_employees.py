import pytest
import requests
import json
from assertpy.assertpy import assert_that
from config import *


def test_get_all_employees_data():
    response = requests.get(BASE_URL+"/employees", headers=HEADERS)
    data = json.loads(response.text)
    
    assert_that(response.status_code).is_equal_to(200)
    assert_that(data["status"]).is_equal_to("success")

def get_all_users():
    response = requests.get(BASE_URL+"/employees", headers=HEADERS)
    return json.loads(response.text)

def test_create_employee():
    f = open('sample_data/employee.json')
    payload = json.load(f)
    f.close()
    response = requests.post(BASE_URL+"/create", headers=HEADERS, data=payload)
    newly_created_emp = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(newly_created_emp["status"]).is_equal_to("success")

    employees = get_all_users()
    
    new_users = [emp for emp in employees["data"] if emp['id'] == newly_created_emp["data"]["id"]]

    assert_that(new_users).is_not_empty()


def create_new_user():
    f = open('sample_data/employee.json')
    payload = json.load(f)
    f.close()
    response = requests.post(BASE_URL+"/create", headers=HEADERS, data=payload)
    return json.loads(response.text)

def search_emp_by_id(employees, newly_created_emp):
    return [emp for emp in employees["data"] if emp['id'] == newly_created_emp["data"]["id"]]

def test_delete_employee():
    employees = get_all_users()
    newly_created_emp = create_new_user()
    new_emp = search_emp_by_id(employees, newly_created_emp)[0]

    emp_to_be_deleted = new_emp['id']

    response = requests.delete(BASE_URL+"/delete/"+str(emp_to_be_deleted), headers=HEADERS)
    
    assert_that(response.status_code).is_equal_to(200)

def test_update_employee():
    employees = get_all_users()
    newly_created_emp = create_new_user()
    new_emp = search_emp_by_id(employees, newly_created_emp)[0]

    emp_to_be_updated = new_emp['id']

    response = requests.put(BASE_URL+"/update/"+str(emp_to_be_deleted), headers=HEADERS)

    assert_that(response.status_code).is_equal_to(200)





    


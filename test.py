import requests

BASE_URL = "http://127.0.0.1:8000"

student_1 = {
    "id": 1,
    "name": "John Doe",
    "age": 20,
    "course": "Math"
}

student_2 = {
    "id": 2,
    "name": "Jane Smith",
    "age": 22,
    "course": "Physics"
}


def test_create_student():
    response = requests.post(f"{BASE_URL}/students", json=student_1)
    assert response.status_code == 200
    assert response.json() == student_1

    response = requests.post(f"{BASE_URL}/students", json=student_2)
    assert response.status_code == 200
    assert response.json() == student_2


def test_get_students():
    response = requests.get(f"{BASE_URL}/students")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = requests.get(f"{BASE_URL}/students", params={"age": 22})
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Jane Smith"

    response = requests.get(f"{BASE_URL}/students", params={"course": "Math"})
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "John Doe"


def test_get_student():
    response = requests.get(f"{BASE_URL}/students/1")
    assert response.status_code == 200
    assert response.json() == student_1


def test_update_student():
    updated_student = student_1.copy()
    updated_student["age"] = 21

    response = requests.put(f"{BASE_URL}/students/1", json=updated_student)
    assert response.status_code == 200
    assert response.json() == updated_student


def test_delete_student():
    response = requests.delete(f"{BASE_URL}/students/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Student deleted successfully"}

    response = requests.get(f"{BASE_URL}/students/1")
    assert response.status_code == 404


if __name__ == "__main__":
    test_create_student()
    #test_get_students()
    #test_get_student()
    test_update_student()
    test_delete_student()
    print("All tests passed!")

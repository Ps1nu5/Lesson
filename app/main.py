from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

templates = Jinja2Templates(directory='templates')

students = {}


class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str


# get post put delete http://127.0.0.1:8000/students
@app.get('/students')
async def get_students(request: Request, age: Optional[int] = Query(None), course: Optional[str] = Query(None)):
    filtered_student = list(students.values())

    if age:
        filtered_student = [student for student in filtered_student if student['age'] == age]
    if course:
        filtered_student = [student for student in filtered_student if student['course'] == course]

    return templates.TemplateResponse('students.html', {'request': request, 'students': filtered_student})


@app.get('/students/{student_id}')
async def get_student(request: Request, student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail='Student not found')
    student = students[student_id]

    return templates.TemplateResponse('student_detail.html', {'request': request, 'student': student})


@app.post('/students')
async def create_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400, detail='Student with this ID already exists')
    students[student.id] = student

    return student


@app.put('/students/{student_id}')
async def update_student(student_id: int, updated_student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail='Student not found')
    students[student_id] = updated_student

    return updated_student


@app.delete('/students/{student_id}')
async def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail='Student not found')
    del students[student_id]

    return {'message': 'Student deleted successfully'}


@app.delete('/students')
async def delete_all_students():
    students.clear()

    return {'message': 'All students was deleted'}


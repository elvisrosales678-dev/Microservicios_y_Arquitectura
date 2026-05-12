from fastapi import FastAPI, HTTPException

app = FastAPI(title='student-service')

STUDENTS = {
    '1': {'id': '1', 'name': 'Ana Pérez', 'status': 'ACTIVE'},
    '2': {'id': '2', 'name': 'Juan Gómez', 'status': 'INACTIVE'}
}

@app.get('/students/{id}')
def get_student(id: str):
    student = STUDENTS.get(id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student

@app.get('/health')
def health():
    return {'status': 'ok'}

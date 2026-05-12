import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(title='enrollment-service')

STUDENT_SERVICE_URL = os.getenv('STUDENT_SERVICE_URL', 'http://localhost:3001')

ENROLLMENTS = []
EVENTS = []

class EnrollmentIn(BaseModel):
    studentId: str
    course: str

@app.post('/enrollments')
async def create_enrollment(payload: EnrollmentIn):
    async with httpx.AsyncClient(timeout=5.0) as client:
        resp = await client.get(f"{STUDENT_SERVICE_URL}/students/{payload.studentId}")

    if resp.status_code == 404:
        raise HTTPException(status_code=400, detail='El estudiante no existe')
    if resp.status_code >= 400:
        raise HTTPException(status_code=502, detail='Error consultando student-service')

    student = resp.json()
    if student.get('status') != 'ACTIVE':
        raise HTTPException(status_code=400, detail='El estudiante no está activo')

    enrollment = {'studentId': payload.studentId, 'course': payload.course}
    ENROLLMENTS.append(enrollment)

    event = {'type': 'EnrollmentCreated', 'studentId': payload.studentId, 'course': payload.course}
    EVENTS.append(event)

    print(f"EVENTO PUBLICADO: EnrollmentCreated - studentId={payload.studentId} - course={payload.course}")

    return {'message': 'Inscripción creada', 'enrollment': enrollment}

@app.get('/events')
def get_events():
    return EVENTS

@app.get('/health')
def health():
    return {'status': 'ok', 'studentServiceUrl': STUDENT_SERVICE_URL}

Actividad Evaluativa – Microservicios y Arquitectura Orientada a Eventos

Este proyecto corresponde a la actividad evaluativa relacionada con Microservicios y Arquitectura Orientada a Eventos. El objetivo es demostrar el funcionamiento de dos microservicios independientes que se comunican entre sí mediante una API REST y que generan un evento cuando ocurre una acción dentro del sistema.

Proyecto desarrollado en Python utilizando FastAPI y contenedores Docker.

Proyecto elegido: Sistema de inscripción a cursos.


Descripción general del sistema

El sistema está compuesto por dos microservicios independientes:

1. student-service
   Servicio encargado de gestionar estudiantes.

2. enrollment-service
   Servicio encargado de registrar inscripciones a cursos.

Ambos servicios se ejecutan en contenedores separados y se comunican entre ellos usando HTTP (REST).


Arquitectura utilizada

La solución sigue los principios de microservicios:

- Independencia física de cada servicio.
- Comunicación REST entre servicios.
- Separación de responsabilidades.
- Contenedores Docker para cada microservicio.
- Orquestación mediante docker-compose.

Además, se implementa un enfoque orientado a eventos: cuando se crea una inscripción, el sistema genera un evento.


Microservicio student-service

Responsabilidad:
Gestionar información de estudiantes.

Puerto:
3001

Endpoint implementado:

GET /students/{id}

Ejemplo de respuesta:
{
  "id": "1",
  "name": "Ana Pérez",
  "status": "ACTIVE"
}


Microservicio enrollment-service

Responsabilidad:
Registrar inscripciones a cursos.

Puerto:
3002

Endpoints implementados:

POST /enrollments

Body de ejemplo:
{
  "studentId": "1",
  "course": "Arquitectura de Software"
}

Antes de registrar una inscripción, este servicio consulta al student-service para validar que el estudiante exista y que su estado sea ACTIVE.

GET /events

Este endpoint permite consultar los eventos generados en memoria.


Arquitectura orientada a eventos

Cuando una inscripción se crea correctamente, el enrollment-service genera un evento del tipo:

EnrollmentCreated

Ejemplo de evento:
{
  "type": "EnrollmentCreated",
  "studentId": "1",
  "course": "Arquitectura de Software"
}

El evento se evidencia de dos formas:
- Se imprime en los logs del servicio.
- Se almacena en memoria y se expone mediante el endpoint GET /events.


Docker y contenedores

Cada microservicio cuenta con su propio archivo Dockerfile.

El archivo docker-compose.yml permite levantar ambos servicios simultáneamente con el siguiente comando:

docker compose up --build

Esto demuestra la ejecución independiente de los servicios y su correcta comunicación.


Evidencias de ejecución

En este computador no fue posible instalar Docker Desktop ni Docker Engine por restricciones del entorno.

Como alternativa, se utiliza GitHub Actions para ejecutar Docker en un entorno Linux remoto, lo cual permite:

- Construir las imágenes Docker.
- Levantar los contenedores.
- Probar los endpoints.
- Visualizar los logs con el evento EnrollmentCreated.

Las evidencias se obtienen a partir de los logs reales del workflow, donde se observa:
- docker compose build
- docker compose up
- consumo REST entre microservicios
- publicación del evento
- docker ps y docker images

Las capturas correspondientes se adjuntan como evidencia de funcionamiento.


Conclusión

Este proyecto demuestra el uso de microservicios independientes, comunicación REST entre servicios y un flujo orientado a eventos. La solución cumple con los requisitos mínimos de la actividad y evidencia el uso de contenedores, orquestación con Docker Compose y desacoplamiento entre servicios.

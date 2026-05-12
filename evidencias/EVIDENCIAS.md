Evidencias para la entrega

Como en este computador no fue posible instalar Docker Desktop ni Docker Engine, las evidencias se obtienen ejecutando Docker con GitHub Actions (entorno Linux remoto).

1. Subir el proyecto a GitHub.
2. Ejecutar el workflow docker-compose-ci (pestaña Actions).
3. Tomar capturas del log donde se vea:

- docker compose build
- docker compose up -d
- Respuesta del GET /students/1
- Respuesta del POST /enrollments
- Respuesta del GET /events
- docker logs enrollment-service mostrando la línea: EVENTO PUBLICADO: EnrollmentCreated
- docker ps
- docker images

Estas capturas son evidencia real de construcción de imágenes, ejecución de contenedores, comunicación REST y publicación del evento.

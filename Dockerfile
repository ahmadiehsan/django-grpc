FROM python:3.11-alpine

# machine requirements
RUN apk --no-cache update
RUN apk --no-cache add bash

# project requirements
COPY ./requirements ./requirements
RUN pip install --no-cache-dir -r requirements/prerequisite/pip-tools.txt
RUN pip-sync requirements/compiled/prod.txt --pip-args '--no-cache-dir'

# wait script
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

# project content
WORKDIR /django_grpc
COPY . .

# port
EXPOSE 8000

# command
CMD ["/wait", "&&", "gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "main_app.wsgi"]

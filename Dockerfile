FROM python:3.11-alpine

# Machine requirements
RUN apk --no-cache update
RUN apk --no-cache add bash gettext

# Project requirements
COPY ./requirements ./requirements
RUN pip install --no-cache-dir -r requirements/prerequisite/pip-tools.txt
RUN pip-sync requirements/compiled/prod.txt --pip-args '--no-cache-dir'

# Wait script
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.12.0/wait /wait
RUN chmod +x /wait

# Envs
ENV PYTHONUNBUFFERED=1

# Project content
WORKDIR /django_grpc
COPY . .

# Port
EXPOSE 8000

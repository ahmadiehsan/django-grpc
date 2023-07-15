# Django gRPC

## Quick Start

```shell
git clone <this_repo>
cd <cloned_dir>

cp confs/docker_compose_envs/postgres.env.example confs/docker_compose_envs/postgres.env
vim confs/docker_compose_envs/postgres.env

cp confs/docker_compose_envs/django_grpc.env.example confs/docker_compose_envs/django_grpc.env
vim confs/docker_compose_envs/django_grpc.env

./run docker.build
./run app.provision
./run app.runserver
```

## Available Commands

- `./run pre_commit.init`
- `./run pre_commit.run_for_all`
- `./run requirements.compile`
- `./run requirements.install.dev`
- `./run requirements.install.prod`
- `./run docker.build`
- `./run docker.destroy`
- `./run docker.down`
- `./run docker.stop`
- `./run postgres.shell`
- `./run app.shell`
- `./run app.runserver`
- `./run app.makemigrations`
- `./run app.migrate`
- `./run app.collectstatic`
- `./run app.makemessages`
- `./run app.compilemessages`
- `./run app.createsuperuser`
- `./run app.provision`

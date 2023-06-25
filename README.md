# Django gRPC

## Quick Start

```shell
git clone <this_repo>
cd <cloned_dir>

cp confs/docker_compose_envs/postgres.env.example confs/docker_compose_envs/postgres.env
vim confs/docker_compose_envs/postgres.env

cp confs/docker_compose_envs/django_grpc.env.example confs/docker_compose_envs/django_grpc.env
vim confs/docker_compose_envs/django_grpc.env

./runner docker.build
./runner app.provision
./runner app.runserver
```

## Available Commands

- `./runner git.pre_commit.init`
- `./runner git.pre_commit.run_for_all`
- `./runner requirements.compile`
- `./runner requirements.install.dev`
- `./runner requirements.install.prod`
- `./runner docker.destroy`
- `./runner app.runserver`
- `./runner app.makemigrations`
- `./runner app.migrate`
- `./runner app.collectstatic`
- `./runner app.compilemessages`
- `./runner app.createsuperuser`
- `./runner app.provision`
- `./runner makemigrations`
- `./runner postgres.shell`

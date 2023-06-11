# Django gRPC

## Quick Start

```shell
git clone <this_repo>
cd <cloned_dir>

cp conf/docker_compose_envs/postgres.env.example conf/docker_compose_envs/postgres.env
vim conf/docker_compose_envs/postgres.env

cp conf/docker_compose_envs/django_grpc.env.example conf/docker_compose_envs/django_grpc.env
vim conf/docker_compose_envs/django_grpc.env

./runner runserver
```

## Additional Commands

- `./runner git.pre_commit.init`
- `./runner git.pre_commit.run_for_all`
- `./runner requirements.compile`

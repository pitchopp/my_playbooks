# vps playbooks

## Build Docker Image for tests

```bash
docker build --tag=debian:bullseye-python .
docker run --detach --name=test_container debian:bullseye-python
```
# dind-unprivileged
Little experiment with running Docker in Docker on Kubernetes and not giving users the rights to schedule privileged containers

# Resources used to create this:
* http://blog.phymata.com/2016/07/30/develop-a-docker-authz-plugin-in-python/
* https://docs.docker.com/engine/extend/plugins_authorization/
* Docker official DinD images

# Usage:
* Schedule the K8S yaml
* Connecting is possible using `docker -H=tcp://docker.default.svc.cluster.local:2375 ps`

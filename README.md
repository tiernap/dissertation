# dissertation

This project demonistrates a Jupyter application stack realised in two environment paradigms:

- Virtual machine with Vagrant/Ansible 
- Containers with Kubernetes/Docker

# Local deploy

To create application stack locally.

## Virtual machine

Requirements:
- Virtualbox
- Vagrant
- vagrant-hostmanager plugin
- ansible

to create:

`vagrant up`

Endpoint is available at:

`jupyter.internal.tld:8888`

## Containers

To create application stack in Kubernetes

Requirements:
- Virtualbox
- Minikube
- kubectl

to create:

```
kubectl apply -f kube-deploy.yaml
```

To expose endpoint:

`minikube service jupyter`

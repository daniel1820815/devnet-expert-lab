# 4.0 Containers (10%)

## 4.1 Create a Docker image (including Dockerfile) 

#### Verify your Docker installation

docker -v
	
#### List all docker containers

docker ps -a
	
#### List all local docker images

docker images

### 4.1.a From a provided image
	
#### Search for a public Docker container image in Docker hub repositories
	
docker search hello-world
	
#### Run a container image
	
docker run hello-world
	
#### Run container image and interact with terminal
	
docker run -ti ubuntu
		
#### Run container image and interact with bash terminal
	
docker run -it --name testapp ubuntu /bin/bash
	
#### Save the container into a local image with a name
	
docker commit testapp myapp
	
#### Run a container from the stored image 
	
docker run --name testapp myapp /myapp.sh
		
#### Make changes to a local image
	
docker commit --change='CMD ["/myapp.sh"]' testapp myapp
		
#### Run a container and remove it afterwards
	
docker run --rm myapp
	
### 4.1.b Expose ports
	
#### Expose ports on command line
	
docker run -d -p <outside port>:<inside port> docker/getting-started
	
docker run -d -p 80:80 docker/getting-started
	
#### Expose ports on dockerfile (by default tcp)

```yaml
EXPOSE <port>	
EXPOSE 80/tcp
EXPOSE 80/udp
```

### 4.1.c Add or copy files
	
### 4.1.d Run commands during image build
	
#### Creates a new image from Dockerfile 
	
docker build .
	
### 4.1.e Manipulate entry point and initial commands
	
### 4.1.f Establish working directories
	
### 4.1.g Environment variables as part of a definition to control an application 

### 4.1.h Docker ignore file

### 4.1.i Volumes

## 4.2 Package and deploy a solution by using Docker Compose 

### 4.2.a Deploy and manage containers
	
### 4.2.b Define services, networks, volumes, and links

## 4.3 Package and deploy a solution by using Kubernetes

#### Running a pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  app: myapp
spec:
  containers:
  - name: myapp
    image: trxuk/clus-1999-app2:latest
```

kubectl create -f pod.yaml

#### View running pod

kubectl get po

### 4.3.a Use deployments, secrets, services, ingress, volumes, namespaces, and replicas
	
#### deployments

Provides replicas and updates.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  labels:
    app: myapp
spec:
  replicas: 4
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: trxuk/clus-1999-app3:latest
        ports:
        - containerPort: 5000
```

kubectl create -f <filename>.yaml

#### secrets
	
#### services

Provide access and Load Balancing.

```yaml
kind: Service
apiVersion: v1
metadata:
  name: myapp-service
spec:
  type: NodePort
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 5000
```

kubectl create -f <filename>.yaml

#### ingress

Layer 7 version of services with routing of traffic based on HTTP header and path data.

Ingress may provide load balancing, SSL termination and name-based virtual hosting.

Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minimal-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx-example
  rules:
  - http:
      paths:
      - path: /testpath
        pathType: Prefix
        backend:
          service:
            name: test
            port:
              number: 80
```

#### volumes

#### namespaces

#### replicas


### 4.3.b Manage the lifecycle of pods (e.g., scale up, scale down, help status, logs)

#### Viewing logs

kubectl logs myapp

#### Getting more details

kubectl describe po myapp

kubectl describe service myapp-service

kubectl describe deployments

#### Delete a pod

kubectl delete -f pod.yaml

kubectl delete pod myapp

#### View deployments

kubectl get deployments

kubectl get pods

4.3.c Monitor pods by building health checks)
4.3.d Use the kubectl interface

4.4 Create, consume, and troubleshoot a Docker host and bridge-based networks and integrate them with external networks

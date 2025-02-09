# UE-AD-A1-GRPC

## TP GRPC

TP Flask, REST, OpenAPI and gRPC

## How to dockerize ?

Run ```docker-compose up -d```
This will launch all the services on their respective ports
To launch test run ```python3 test/main.py```
All other tests need to be done by hand

## Services list :

| Service  | Port |
|----------|------|
| movie    | 3001 |
| booking  | 3002 |
| user     | 3004 |
| showtime | 3003 |

WARNING : Put your IMDB_KEY in a .env, otherwise you will not be able to fetch from IMDB's API

All services communicate throught the docker default network, and use the respective container hostname with their respective port

BOËLLE Octave
GLOCK Matteo

# File structuration :

```
project
│   requirements.txt <- Dependencies for this project
│
└───services
│   └───service1
│   │   └───data                <- Sample database .json
│   │   └───protos              <- Where the pb2 generated files will be
│   │   │   service1.py         <- The servicer class file
│   │   │   Dockerfile          <- To easily deploy the service later with Docker
│   │   │   requirements.txt    <- Used by Docker to install dependencies
│   │
│   └───service2
│   └───...
│   │
│   └───client  <- The client folder, NB : It is not a service, and you can't name a service 'client'
│       │          It is for testing your services only, you can delete it if you test your service with something else
│       └───protos              <- pb2 for each service will be also generated here
│       │   client.py           <- The client main script used to make requests to our services to test them
│
└───protos
│   │   service1.proto <- Proto file for service1
│   │   service2.proto <- Proto file for service2
│   │   base.proto     <- Proto file imported in other proto files, not representing a service
│   │   ...NB : A the service name should be the same than its proto file name
│
└───venv <- We suggest you to use a virual environment

```

# How to properly import files in .proto files :

## Do it this way :

```python
import "protos/base.proto";
```

# How to create Docker images with docker-compose :

#TODO

# How to compile a service ?

## Under a windows terminal :

You can use the python module we made and that is included in requirements.txt : `grpyc`

To build every services and compile them in the client :
`grpyc -cc`

To run a specific service :
`grpyc -s service_name`

To see other commands :
`grpyc --help`

## Otherwise :

Follow grpcio for python documentation

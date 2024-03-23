# SMSHER

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

SMSHER is multipurpose messaging service emulation in termux. It used backend service as redis and termux-api.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Install python on your system. For Arch based distro
```
pkg upgrade; pkg install python
```

setup redis and start the redis server
```
pkg install redis-server
```

### Installing and Deployment

A step by step series of examples that tell you how to get a development env running.

setting up the virtual environment

```
python -m venv virt
```

activate your virtual venv

```
source virt/bin/activate
```

activate your virtual venv

```
pip install -r requirements.txt
```

start the server

```
uvicorn app.main:app
```


## Usage <a name = "usage"></a>

go to the [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

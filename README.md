# CS 361 TA Scheduler Application


- [CS 361 TA Scheduler Application](#cs-361-ta-scheduler-application)
  - [About](#about)
  - [Prerequisites](#prerequisites)
  - [Setup Remote Server](#setup-remote-server)
  - [Configure Environment Variables](#configure-environment-variables)
  - [Setting Up Local Development Environment with Docker Context](#setting-up-local-development-environment-with-docker-context)

## About
our group worked together using test-driven development (TDD) methods to build a small project using Django. We utilized agile development methods, such as daily stand-up meetings, sprint planning, and retrospectives, to help us work together effectively. We created artifacts such as user stories, high level, and low level designs to ensure everyone was on the same page.

One of the key aspects of our methodology was testing. We wrote unit tests for each feature before writing any code, and used these tests to guide the development process. We also utilized main branch protection which required pull request reviews and required passing tests before merging new code into the main branch.

In addition to TDD, we used various other methods to ensure the quality of our code. For example, we conducted code reviews and utilized automated code analysis tools. We also practiced good version control habits, such as using descriptive commit messages and branching appropriately.

Overall, our goal was to build high-quality code that met the needs of our stakeholders. By using TDD and other best practices, we were able to achieve this goal and create a successful project.

## Prerequisites
- A Digital Ocean account and a Droplet created with Docker installed.
- A registered domain name that points to the IP address of your Digital Ocean Droplet.
- A local Django project ready for deployment.

## Setup Remote Server
1. SSH into your remote server:
```shell
ssh root@your_server_ip
```

2. Update the package list and upgrade the packages:
```shell
sudo apt update && sudo apt upgrade
```

3. Clone the project repository into the remote server:
```shell
git clone https://github.com/Anthony-Alagna/361Project.git
```
**Note**: To connect to your remote server securely, it is recommended to set up SSH public key authentication. If you don't have an SSH key pair yet, you can generate one using the `ssh-keygen` command. For a step-by-step guide on creating an SSH key pair and configuring public key authentication, please follow this [SSH key generation guide](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804).


## Configure Environment Variables
1. In the root directory of your Django project, create a `template.env` file with the following content as a template:


2. Replace the placeholder values with your actual settings:

- 'SECRET_KEY': The secret key for your Django project. This is a unique string used to provide cryptographic signing, ensuring the security of various components of your application. Generate a new, random secret key and keep it secret. You can use [Django Secret Key Generator](https://djecrety.ir/) to create a new secret key.

- 'DEBUG': A boolean value (True or False) that indicates whether your Django project is running in debug mode. In a production environment, this should be set to False to prevent sensitive information from being leaked.

- 'DB_NAME': The name of your database. Choose a name that represents your project or application.

- 'DB_ENGINE': The database engine for your Django project. This value determines which database system Django will use. Common options are 'django.db.backends.postgresql' for PostgreSQL, 'django.db.backends.mysql' for MySQL, and 'django.db.backends.sqlite3' for SQLite.

- 'MAIL_SERVER': The mail server for your Django project. This value specifies the server that will handle sending emails for your application. e.g.'smtp.gmail.com' 

- 'MAIL_USERNAME': The email address or username used for sending emails from your Django project. This should be the email address associated with your chosen mail server.

- 'MAIL_PASSWORD': The password for the email address or username used for sending emails from your Django project. Make sure to keep this value secure and not shared with anyone.

- 'ENVIRONMENT': The environment your Django project is running in. This value helps you manage different settings and configurations for different environments (e.g., development, staging, production).


3. For the local environment, create a copy of the `template.env` file and name it `.env`. This file will contain your environment variables for the local development setup:

```shell
cp template.env .env
```

4. For the remote environment, rename the `template.env` file to `prod.env`:
```shell
mv template.env prod.env
```
Now, your .env file will be used for your local environment, and your prod.env file will be used for your remote environment. These files contain the respective environment variables, which will be used by Docker Compose to set up the containers.

**Note**: Make sure to add `prod.env` to your `.gitignore` file to prevent it from being tracked by Git.


## Setting Up Local Development Environment with Docker Context

To set up your local development environment using Docker, you'll be using a Docker context. This will allow you to manage and deploy containers from your local machine to the remote server. In this process, you will also use Docker Compose commands to build, start, and manage your containers and their associated volumes.

1. First, install Docker and Docker Compose on your local machine. Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) and the [Docker Compose installation guide](https://docs.docker.com/compose/install/) for your operating system.

2. To create a new Docker context for your remote server, run the following command, replacing `your_server_ip` with the IP address of your Digital Ocean Droplet:

```shell
docker context create my_remote_server --docker "host=ssh://root@your_server_ip"
```

3. Switch to the newly created Docker context:
```shell
docker context use my_remote_server
```

4. Now, you can use Docker Compose commands to manage your containers and their associated volumes. To stop and remove any running containers along with their volumes, run:
```shell
docker-compose down -v
```

5. To build, create, and start your containers in the background, use the following command. This will also renew any anonymous volumes, remove any orphan containers, and force recreate the containers:
```shell
docker-compose up -d --build --renew-anon-volumes --remove-orphans --force-recreate
```
With this setup, you can now manage your remote containers from your local development environment using Docker and Docker Compose.
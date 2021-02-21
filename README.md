Notification Django app
=======================

## Prerequisites

- Docker; if you don’t have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms);
- Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/).

## Setup

- Clone the repo

- Build and Run following with the local env vars checked in VCS
  ```
  $ docker-compose -f local.yml build django
  $ docker-compose -f local.yml up -d django
  ```

- Create a superuser with following command.

``` bash
 $ docker-compose -f local.yml run django python manage.py createsuperuser
```

- To create notifications from UI visit(http://localhost:8000/users/notification/create/)

- Create some another user which will create Notification via post-save signal from User model with msg "Your account is created"

- To view the notifications in django admin, visit (http://localhost:8000/admin/notifications/notification/)


## Additional third party package used

- [Django Notifications](https://github.com/django-notifications/django-notifications)


## Credits

- This project was bootstrapped with [cookiecutter-django](https://github.com/pydanny/cookiecutter-django).
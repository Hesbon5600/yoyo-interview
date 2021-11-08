### Yoyo Group interview

#### Api Documentation

> ## How to set up the project.

### Features.

- Python 3.9
- Django REST framework
- pipenv

---

### Installation.

- clone the repository

```
$ git clone https://github.com/Hesbon5600/yoyo-interview.git
```

- cd into the directory

```
$ cd yoyo-interview
```

- Install dependencies

```
$ make install
```

- After dependencies are installed, run the virtual environment

```
$ pipenv shell
```

- create environment variables
  On Unix or MacOS, run:

```
$ touch .env
```

open .env file and enter your corresponding database details as follows

```
SECRET_KEY='f++w+u3=qh%fkj(6l2$oyyk7*g8+u3*hz0b1*qc*@(ll-uq^'
WEATHER_API_KEY=77e334f55f184f91afc144327201409
```

Note: There is no space next to '='

---

##### On terminal,

```
$ source .env
```

- Run the application

```
make run
```

- Testing the application

```
$ make test
```

- Testing code linting

```
$ make lint
```

---

## API documentation

> For the API documentation, the url is:

```
$ http://localhost:8000/api/docs/
```

---

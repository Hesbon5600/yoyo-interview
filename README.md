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
$ cp .env.example .env
```

The env should now have the following variables:

```
SECRET_KEY=<value-here>
WEATHER_API_KEY=<value-here>
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

- Expand the endpoint and click `try it out`

---

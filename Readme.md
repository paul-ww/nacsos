# NACSOS: NLP Assisted Classification, Synthesis and Online Screening

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4121525.svg)](https://doi.org/10.5281/zenodo.4121525)

Authors: Max Callaghan, Jérôme Hilaire, Finn Müller-Hansen, Yuan Ting Lee

## Summary

NACSOS is a django site for managing collections of documents, screening or coding them by hand, and doing NLP tasks with them like topic modelling or classifiation.

It was built for handling collections of scientific document metadata, but has extensions that deal with twitter data and parliamentary data.

It currently contains many experimental, redundant or unsupported features, and is not fully documented.

The part that deals with topic modelling is a fork of Allison J.B Chaney's **tmv** [repository](https://github.com/blei-lab/tmv). It extends this by managing multiple topic models and linking these with various document collections.

NACSOS is research software produced by the APSIS working group at the Mercator Research Institute on Global Commons and Climate Change ([MCC](https://www.mcc-berlin.net/)), and some parts of the repository are instution specific. We are in an ongoing process of generalising, and documenting.

Refer to the [documentation](https://github.com/mcallaghan/tmv/wiki/Scoping-Documentation) for a (partial) guide to using the app.

## Citation

If you use NACSOS in academic work, you can cite it as

Max Callaghan, Finn Müller-Hansen, Jérôme Hilaire, & Yuan Ting Lee. (2020). NACSOS: NLP Assisted Classification, Synthesis and Online Screening. Zenodo. http://doi.org/10.5281/zenodo.4121525

### Install Docker
[Installing Docker](https://docs.docker.com/get-docker/) allows each component to run within its own container.

### Install VSCode
It is recommended to [install VSCode](https://code.visualstudio.com/docs/setup/linux) along with the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) to quickly setup a development environment for NACSOS.

### Building the project using Docker
If you have VSCode installed, it should be enough to clone this repository and to wait for the prompt to `Reopen this project inside a container`. The images will then be built and the current directory opened inside the main Docker container.

### Setting up scoping-tmv
We use an `.env` file to load local settings as well as sensitive variables. Copy the template below, replacing the secret information with your own and store it as `.env` in the root of this repository.

```
# Store this as '.env' in the repository root

# Debug Mode
DEBUG = True
MAINTENANCE = False

# Network
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ['*']

# Celery
CELERY_BROKER_URL = redis://redis:6379/0

# Database
DB_NAME = scoping_tmv
DB_USER = scoper
DB_PASSWORD = secure_password
DB_HOST = db

# Email
EMAIL_HOST = your-email-server
EMAIL_HOST_USER = your-email-user
EMAIL_PORT = your-email-port

# Secrets
SECRET_KEY = your-secret
CONSUMER_KEY = your-key
CONSUMER_SECRET = your-secret
ACCESS_TOKEN = your-token
ACCESS_SECRET = your-secret

V2_API_KEY = your-key
V2_API_SECRET_KEY = your-key
V2_BEARER_TOKEN = your-token

# Paths
STATIC_ROOT = /var/www/tmv/BasicBrowser/static/
MEDIA_ROOT = /var/www/tmv/BasicBrowser/media
QUERY_DIR = /usr/local/apsis/queries/
WARP_LDA_PATH = /home/galm/software/warplda/release/src
```

### Create a superuser

Create an admin user if using on a clean database

```
python manage.py createsuperuser
```

### Prepare and make outstanding migrations

Since some tables might be missing if working with a clean DB, make sure that all migrations
have been prepared and run. `cd` into `BasicBrowser` and run

```
python manage.py makemigrations
python manage.py migrate
```

### Setting up Celery
We use celery to execute computation-heavy tasks in the background.

To start celery, `cd` into `BasicBrowser` and run

```
celery -A BasicBrowser.celery worker --loglevel=info
```

### Start a local server

Now you should be done, and ready to run a local server. `cd` into `BasicBrowser` and run

```
python manage.py runserver
```

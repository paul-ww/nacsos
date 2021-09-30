# [Choice] Python version: 3, 3.8, 3.7, 3.6
ARG VARIANT=3.8
FROM joyzoursky/python-chromedriver:${VARIANT}-selenium

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends libfreetype6-dev libpq-dev python3-cffi \
                                                   libxml2-dev libxslt1-dev libgdal-dev binutils \
                                                   libproj-dev gdal-bin xvfb

# Install requirements
COPY BasicBrowser/requirements_docker.txt .
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -Ur requirements_docker.txt

# Download NLTK stopwords
RUN [ "python", "-c", "import nltk; nltk.download('stopwords')" ]
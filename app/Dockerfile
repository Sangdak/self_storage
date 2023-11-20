# pull official base image
FROM python:3.11

# set shell
SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# build dependencies
ARG BUILD_DEPS="curl python3 python3-pip"
RUN apt-get update && apt-get install -qy $BUILD_DEPS

RUN pip install --upgrade pip && pip install virtualenv

# create the app user and folders
RUN useradd -rms /bin/bash testuser && chmod 777 /opt /run

WORKDIR /testuser

RUN mkdir /testuser/staticfiles && mkdir /astrouser/mediafiles && chown -R testuser:testuser /testuser && chmod 755 /testuser

COPY --chown=testuser:testuser . .

RUN pip install -r requirements.txt

USER testuser

CMD ["gunicorn", "-b", "0.0.0.0:8000", "selfstorage.wsgi:application"]

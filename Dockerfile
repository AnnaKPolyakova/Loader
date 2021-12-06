#FROM python:3.9
#WORKDIR /code
#COPY poetry.lock pyproject.toml /
#RUN pip3 install --upgrade pip
#RUN pip3 install poetry
#RUN poetry install
#COPY . .
#CMD gunicorn loader.wsgi:application --bind 0.0.0.0:8000
FROM python:3.8.5
WORKDIR /code
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . .
CMD gunicorn loader.wsgi:application --bind 0.0.0.0:8000
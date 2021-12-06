FROM python:3.9
WORKDIR /code
COPY poetry.lock pyproject.toml /
RUN pip3 install --upgrade pip
RUN pip3 install poetry
# Turn off VirtualEnv
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
CMD gunicorn loader.wsgi:application --bind 0.0.0.0:8000

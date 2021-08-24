FROM python:3.9-slim-buster

RUN pip install pipenv

RUN pip install "dipdup==2.0.3"

WORKDIR /radiate
COPY Pipfile.lock Pipfile /radiate/

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /radiate

ENTRYPOINT ["pipenv", "run", "dipdup"]
CMD ["-c", "dipdup.yml", "run"]
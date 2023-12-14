# file: Dockerfile

FROM python:3.9-slim

RUN mkdir -p /extractor/extractor

WORKDIR /extractor

RUN pip install -U pip && pip install install pipenv

COPY Pipfile Pipfile.lock /extractor/

RUN pipenv install --system --deploy

COPY . . 

EXPOSE 3002

CMD ["uvicorn", "extractor.app:app", "--host", "0.0.0.0", "--port", "3002"]
FROM python:3.12
RUN pip install poetry

ADD . /app
WORKDIR /app
RUN poetry install

ENV PROD=1 \
    PORT=8080

EXPOSE 8080
CMD ["poetry", "run", "python", "./main.py"]

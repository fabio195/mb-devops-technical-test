FROM python:3.12-alpine3.20

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/app/main.py

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

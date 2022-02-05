# создание контейнера
# docker build -t hw .
#
# запуск контейнера
# docker run --rm --name hw_03 -p 8000:8000 hw


FROM python:3.9-buster

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD uvicorn app:app --host=0.0.0.0 --port=8000
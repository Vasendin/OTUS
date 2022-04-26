# создание образа
# docker build -t hw_dc .
#
# запуск контейнера
# docker run --rm --name cont_hw_dc -p 5000:5000 hw_dc


FROM python:3.9-buster

ENV PYTHONBUFFERED=1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r ./requirements.txt

COPY . /usr/src/app/

ENV CONFIG_NAME=DevelopmentConfig

RUN chmod +x prestart.sh
ENTRYPOINT ["bash", "prestart.sh"]

EXPOSE 5000

CMD flask db upgrade
CMD flask run --host=0.0.0.0 --port=5432

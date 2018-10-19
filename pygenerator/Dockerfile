FROM python:2

COPY ./grafana-cfg grafana-cfg/
COPY generator generator/

RUN chmod -R 777 /grafana-cfg /generator

RUN apt-get update && apt-get install -y netcat
RUN pip install -U -r generator/requirements.txt

ENTRYPOINT ["generator/run.sh"]

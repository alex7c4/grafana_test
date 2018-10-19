#!/usr/bin/env bash

# waiting for services
while ! (nc -z grafana 3000 && nc -z elasticsearch 9200 && nc -z graphite 2003)
do
    echo "waiting services"
    sleep 1
done

# Add datasources to grafana
curl -X POST "http://grafana:3000/api/datasources" --user admin:secret -H "Content-Type: application/json" --data @grafana-cfg/datasource_graphite.json
curl -X POST "http://grafana:3000/api/datasources" --user admin:secret -H "Content-Type: application/json" --data @grafana-cfg/datasource_elasticsearch.json

# Add dashboard  to grafana
curl -X POST "http://grafana:3000/api/dashboards/db" --user admin:secret -H "Content-Type:application/json" --data @grafana-cfg/my_dashboard.json

# run data generator
python generator/generate_messages.py

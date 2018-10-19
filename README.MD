This scripts will setup Grafana (with Graphite and ElasticSearch as data sources) configuration with following containers:
* `graphite`
* `elasticsearch`
* `grafana`
* `pygenerator`

Python script from `pygenerator` container will generate random data to data sources.

Grafana GUI: [http://localhost:3000/login](http://localhost:3000/login)
```
user: admin
pass: secret
```

![grafana_gui](img/grafana_out.png)

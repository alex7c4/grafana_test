"""
Data generator for Graphyte and ElasticSearch

ElasticSearch:
    https://elasticsearch-py.readthedocs.io/en/master/
    https://github.com/elastic/elasticsearch-py

Graphyte:
    https://github.com/Jetsetter/graphyte
"""
from datetime import datetime
from random import randint
from time import sleep

import graphyte
from elasticsearch import Elasticsearch


ES_INDEX = 'es_test_index'
G_METRIC1 = 'test.data1'  # system.sync.test.data1
G_METRIC2 = 'test.data2'  # system.sync.test.data2


def data_generator_1():
    return randint(0, 100)


def data_generator_2():
    return randint(0, 100)


def send_to_es(es):
    doc = {
        'timestamp': datetime.now(),
        'value1': data_generator_1(),
        'value2': data_generator_2(),
    }
    res = es.index(index=ES_INDEX, doc_type='data', body=doc)
    print res


def send_to_graphyte():
    if graphyte.default_sender is None:
        raise EnvironmentError('Init graphyte first')
    graphyte.send(G_METRIC1, data_generator_1())
    graphyte.send(G_METRIC2, data_generator_2())


def main():
    # init elasticsearch
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    es.indices.create(index=ES_INDEX, ignore=400)

    # init graphyte
    graphyte.init('graphite', port=2003, prefix='system.sync')

    # send data
    while True:
        send_to_es(es)
        send_to_graphyte()
        sleep(5)


if __name__ == '__main__':
    main()

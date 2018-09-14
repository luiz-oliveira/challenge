from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Integer, Text, Date, Float

connections.create_connection()

class TransactionIndex(DocType):
    pk = Integer()
    customer_id = Integer()
    amount = Float()
    date_debt = Date()
    payment_type = Text()

    class Meta:
        index = 'transaction-index'

TransactionIndex.init()
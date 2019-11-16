from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('172.26.154.143', 9090);

transport = TTransport.TBufferedTransport(transport)

protocol = TBinaryProtocol.TBinaryProtocol(transport);

client = Hbase.Client(protocol)
transport.open()


tableName = 'test'
rowKey = 'row-key1'

result = client.getRow(tableName, rowKey, None)
print(result)
for r in result:
    print('the row is ' , r.row)
    print('the values is ' , r.columns.get('cf:a').value)

print(client.getTableNames())
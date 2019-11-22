# -*- coding: utf-8 -*-
import redis
import happybase
class feedHandler:
    pool = redis.ConnectionPool(host='47.92.67.19', port=6379, decode_responses=True)
    conn = happybase.Connection("39.99.140.90", 9090)
    def quickSave(self,userid,movieid,like):
        r = redis.Redis(connection_pool=self.pool)
        r.set('%d_%d'%(userid,movieid),str(like),ex=10)
    
    def quickRead(self,userid,movieid):
        r = redis.Redis(connection_pool=self.pool)
        return r.get('%d_%d'%(userid,movieid))
    
    def hbaseSaveByRedis(self,userid,movieid):
        like = self.quickRead(userid,movieid)
        table = self.conn.table("feedback")
        table.put(str(userid),{"movie:%d"%movieid:like})

    def hbaseSave(self,userid,movieid,like):
        table = self.conn.table("feedback")
        table.put(str(userid),{"movie:%d"%movieid:str(like)})
    
    def hbaseRead(self,userid,movieid,like):
        table = self.conn.table("feedback")
        row = table.row(str(userid))
        return row[b"movie:%d"%movieid]
'''
fh = feedHandler()
fh.hbaseSave(1,1,1)
'''
'''
fh = feedHandler()
fh.quickSave(1,1,1)
print(fh.quickRead(1,1))
'''
'''
conn = happybase.Connection("39.99.140.90", 9090)
conn.create_table('feedback',{"movie":{}})
'''
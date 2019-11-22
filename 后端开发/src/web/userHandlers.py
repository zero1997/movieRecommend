
# -*- coding: utf-8 -*-
import pymysql
codes = {}
codes[200] = "success"
codes[500] = "user not exist"
codes[401] = "user not verify"
codes[501] = "password incorrect"
codes[502] = "invalid username"

class mysqlDB:
	ip = "39.100.226.136"
	user = "root"
	pwd = ""
	db = "recommendation"

class userHandler:
    dbInfo = mysqlDB()
    loginCheck = "select * from userSecurity where username<=>'%s';"
    createSec = "insert into userSecurity(userpwd,username) values('%s','%s')"
    getUserid = "select userid from userSecurity where username<=>'%s'"
    createInfo = "insert into userInfo(userid,username) values('%d','%s')"
    getInfos = "select * from userInfo where userid=%d;"
    modifyInfos = "update userInfo set username = '%s' , birth='%s' , city = '%s', sex = %d where userid=%d" 
    def userLoginCheck(self,username,pwd):
        db = pymysql.connect(mysqlDB.ip,mysqlDB.user,mysqlDB.pwd,mysqlDB.db,use_unicode=True,charset='utf8')
        cursor = db.cursor()
        cursor.execute(self.loginCheck%username)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        if len(data)<1:
            return 500,codes[500],"-1","游客"
        elif len(data)>1:
            return 502,codes[502],"-1","游客"
        else:          
            if data[0][1] == pwd:
                return 200,codes[200],data[0][0],data[0][2]
            else:
                return 501,codes[501],"-1","游客"

    def userCreate(self,username,userpwd):
        db = pymysql.connect(mysqlDB.ip,mysqlDB.user,mysqlDB.pwd,mysqlDB.db,use_unicode=True,charset='utf8')
        cursor = db.cursor()
        cursor.execute(self.createSec%(userpwd,username))
        db.commit()
        cursor.execute(self.getUserid%username)
        data = cursor.fetchone()
        userid = data[0]
        cursor.execute(self.createInfo%(userid,username))
        db.commit()
        #TO DO:错误控制
        cursor.close()
        db.close()
        return userid,200,codes[200]
    
    def getInfo(self,userid):
        db = pymysql.connect(mysqlDB.ip,mysqlDB.user,mysqlDB.pwd,mysqlDB.db,use_unicode=True,charset='utf8')
        cursor = db.cursor()
        cursor.execute(self.getInfos%(userid))
        data = cursor.fetchone()
        #TO DO:错误控制
        tmp = {}
        tmp["userid"] = userid
        tmp["birth"] = str(data[2])
        tmp["city"] = data[3]
        tmp["sex"] = data[4]
        cursor.close()
        db.close()
        print(tmp)
        return tmp
    
    def modifyInfo(self,userid,username,birth,city,sex):
        db = pymysql.connect(mysqlDB.ip,mysqlDB.user,mysqlDB.pwd,mysqlDB.db,use_unicode=True,charset='utf8')
        cursor = db.cursor()
        cursor.execute(self.modifyInfos%(username,birth,city,sex,userid))
        db.commit()
        cursor.close()
        db.close()
        return 200,codes[200]


'''
db = pymysql.connect(mysqlDB.ip,mysqlDB.user,mysqlDB.pwd,mysqlDB.db)
cursor = db.cursor()
cursor.execute("select * from userSecurity;")
data = cursor.fetchall()
print(data)
cursor.close()
db.close()
'''

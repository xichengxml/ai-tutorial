import pymysql
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/3 上午 12:01
# ---------------------------


connect = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python')
cursor = connect.cursor()

sql = ''' update hero set comment='update' where id=3 '''

try:
    cursor.execute(sql)
    connect.commit()
except Exception as e:
    print(e)
    connect.rollback()
finally:
    connect.close()

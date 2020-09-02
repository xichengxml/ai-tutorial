import pymysql
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/2 下午 11:54
# ---------------------------


connect = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python')
cursor = connect.cursor()

sql = ''' select * from hero '''

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    for hero in result:
        print(hero)
except Exception as e:
    print(e)
    connect.rollback()
finally:
    connect.close()


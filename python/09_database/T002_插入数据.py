import pymysql

# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/2 下午 11:35
# ---------------------------


connect = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python')
cursor = connect.cursor()

sql = ''' insert into hero (name, age, point, rank) values (%s, %s, %s, %s) '''

try:
    cursor.execute(sql, ('欧阳锋', 58, 89.5, 15))
    connect.commit()
except Exception as e:
    print(e)
    connect.rollback()
finally:
    connect.close()

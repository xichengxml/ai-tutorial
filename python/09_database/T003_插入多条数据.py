import pymysql
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/2 下午 11:46
# ---------------------------


connect = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python')
cursor = connect.cursor()

sql = ''' insert into hero (name, age, point, rank) values (%s, %s, %s, %s) '''

try:
    datas = [('黄老邪', 56, 88.5, 16), ('一灯大师', 61, 90, 14)]
    cursor.executemany(sql, datas)
    connect.commit()
except Exception as e:
    print(e)
    connect.rollback()
finally:
    connect.close()

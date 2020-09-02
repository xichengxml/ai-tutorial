import pymysql

# ---------------------------
# @description 
# @author xichengxml
# @date 2020/9/2 下午 11:23
# ---------------------------

connect = pymysql.connect(host='localhost', user='root', password='123456', port=3306, database='python')
cursor = connect.cursor()
try:
    sql = '''
            create table hero (
            id int(8) primary key auto_increment,
            name varchar(30) not null,
            point float(3,1) comment '武功分数',
            age int(3),
            rank int(5) comment '武功排行'
            )
        '''

    cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    connect.close()

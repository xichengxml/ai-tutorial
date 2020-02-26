# ---------------------------
# @description  一个关于异常的小例子：输入其他数字继续输出异常；输入88退出程序
# @author xichengxml
# @date 2020/2/26 下午 11:53
# ---------------------------


while True:
    try:
        i = int(input("请输入数字: "))
        if i == 88:
            break
        print("i: ", i)
    except Exception as e:
        print(e)

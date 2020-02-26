# ---------------------------
# @description 异常基础
# @author xichengxml
# @date 2020/2/26 下午 11:51
# ---------------------------


try:
    1 / 0
except BaseException as e:
    print(e)
    print(type(e))
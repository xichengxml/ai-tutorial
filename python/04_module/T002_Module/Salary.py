# ---------------------------
# @description 计算员工工资
# @author xichengxml
# @date 2020/3/8 下午 11:07
# ---------------------------


company = '梦境阁'


def yearSalary(monthSalary):

    """根据传入的月薪计算员工的年薪"""
    return monthSalary * 12


def daySalary(monthSalary):

    """根据传入的月薪计算员工的日薪"""
    return monthSalary / 22.5


if __name__ == "__main__":
    print(yearSalary(35000))
    print(daySalary(35000))
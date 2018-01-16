#  -*- coding:utf-8 -*-

import sys
"""
年终奖税筹计算 -- Year-end Award Tax Planning
输入：salary: 当月工资（扣除五险一金后的金额）
      award: 奖金金额
"""

FREE_LINE = 3500

# 税率表
STEPS = [ [80000, 45, 13505],
          [55000, 35, 5505],
          [35000, 30, 2755],
          [9000,  25, 1005],
          [4500,  20, 555],
          [1500,  10, 105],
          [0,     3,  0] ]

# 查找适用的税率
def findStep(num):
    for step in STEPS:
        if num > step[0]:
            break
    return step


# 计算工资的个税
def getSalaryTax(Salary):
    if Salary <= FREE_LINE:
        return 0
    step = findStep(Salary - FREE_LINE)
    tax = (Salary - FREE_LINE) * step[1] / 100 - step[2]
    return tax


# 计算年终奖的缴税金额
def getAwardTax(Award, Salary):
    if Salary < FREE_LINE:
        base = Award - (3500 - Salary)
    else:
        base = Award
    step = findStep(base/12)
    # print step
    tax = base * step[1]/100 - step[2]
    # print "in getAwardTax:", Award, Salary, tax
    return tax


# 计算缴税最少的方案
def getMinTax(Award, Salary):
    r_steps = STEPS[::]
    r_steps.reverse()
    total = Salary + Award
    min_tax = 99999999
    best_salary = 0
    if total <= FREE_LINE:
        print "You do not need to do tax planning."
    for step in r_steps:
        if step[0] < total-FREE_LINE:
            step_salary = FREE_LINE + step[0]
            s_tax = getSalaryTax(step_salary)
            a_tax = getAwardTax(total-step_salary, step_salary)
            # print total, step_salary, s_tax, a_tax
            if s_tax + a_tax < min_tax:
                min_tax = s_tax + a_tax
                best_salary = step_salary
    print "Best Salary is %d, and min tax is %d" % (best_salary, min_tax)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python TaxPlanning `Award` `Salary`"
    else:
        try:
            Award = int(sys.argv[1])
            Salary = int(sys.argv[2])
            getMinTax(Award, Salary)
        except Exception, e:
            print e.message

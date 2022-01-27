import xlrd
from KDT_MODULE.services.mycases import MyCases

class Parse():
    def __init__(self, xls_path):
        self.xls_path = xls_path
        self.book = None
        self.sheet = None

    def init_book(self):
        try:
            self.book = xlrd.open_workbook(self.xls_path)
        except Exception as e:
            print(e)

    def get_sheet(self, sheet_name="sheet1"):
        try:
            self.init_book()
            self.sheet = self.book.sheet_by_name(sheet_name)
            return self.sheet
        except Exception as e:
            print(e)
            return None

    def get_row_data(self, row):
        if self.sheet == None:
            print("没有找到sheet页面")
            return None
        else:
            if row > 0:
                return self.sheet.row_values(row)
            else:
                print("请输入大于1的正整数")
                return None

    def prepare_tc(self):
        tcs = []
        rows = self.sheet.nrows
        for i in range(1, rows):
            data = self.get_row_data(i)
            tc = MyCases()
            tc.tcno = data[0]
            tc.title = data[1]
            tc.module = data[2]
            tc.tcname = data[3]
            tc.steps = self.deal_step(data[4])
            tc.mark = data[5]
            tcs.append(tc)
        return tcs

    def deal_step(self, stepstr):
        """
        将传入的字符串解析为key, object, param三个数据，保存在字典中，添加进列表
        :param stepstr:
        :return:
        """
        steplist = []
        for item in stepstr.splitlines():
            step = {}
            tmp = item.split(" ")
            if len(tmp) == 2:
                step["key"] = tmp[0]
                step["object"] = tmp[1]
            elif len(tmp) == 3:
                step["key"] = tmp[0]
                step["object"] = tmp[1]
                step["param"] = tmp[2].split("=", 1)[1]
            else:
                print(f"测试用例出现错误! {tmp}")
            steplist.append(step)
        return steplist

if __name__ == '__main__':
    p = Parse("../testdata/case1.xls")
    p.get_sheet("Sheet1")
    tcs = p.prepare_tc()
    print(tcs[0].get_steps(), tcs[1].get_steps())


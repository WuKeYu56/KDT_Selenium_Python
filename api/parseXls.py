import xlrd


class ParseXls:

    def __init__(self, file_path):
        self.path = file_path
        self.book = None
        self.sheet = None

    def init_book(self):
        try:
            self.book = xlrd.open_workbook(self.path)
        except Exception as e:
            print(e)

    def get_sheet(self, sheet_name="woniusales"):
        try:
            self.init_book()
            self.book = xlrd.open_workbook(self.path)
            self.sheet = self.book.sheet_by_name(sheet_name)
            return self.sheet
        except Exception as e:
            print(e)

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
        self.get_sheet()
        rows = self.sheet.nrows
        tcs = []
        for i in range(1, rows):
            tc = {}
            data = self.get_row_data(i)
            tc["id"] = int(data[1])
            tc["title"] = data[2]
            tc["precondition"] = data[3]
            tc["method"] = data[4]
            tc["url"] = data[5]
            tc["param"] = self.deal_param(data[6])
            tc["accept_type"] = data[7]
            if data[7] == "json":
                tc["expect"] = self.deal_json(data[8])
            else:
                tc["expect"] = data[8]
            tcs.append(tc)
        return tcs

    def deal_param(self, param_str):
        param_str = param_str.replace("\n", '", "')
        param_str = param_str.replace("=", '": "')
        param_str = '{"'+param_str+'"}'
        dic = eval(param_str)
        if dic == {''}:
            dic = None
        return dic

    def deal_json(self, result):
        lis = result.split("=", 1)
        return lis

if __name__ == '__main__':
    p = ParseXls("./data/case3.xls")
    tcs = p.prepare_tc()
    for tc in tcs:
        print(tc)
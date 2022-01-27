class Collector:
    def __init__(self):
        self.rs = []  #存放全部用例的执行情况

    def get_data(self, tc):
        rdict = {}
        rdict['tc'] = tc
        return rdict

    def get_result(self, rdict, rlts):
        rdict['result'] = rlts  #用例的执行结果存入字典
        self.rs.append(rdict)

    def print_rltlist(self):
        for item in self.rs:
            print(item)
            print(item['tc'].title)
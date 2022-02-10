class Collector:
    def __init__(self):
        self.rs = []  #存放全部用例的执行情况

    def get_data(self, tc):
        rdict = {}
        rdict['tc'] = tc  #用例的实例化对象存入字典
        return rdict

    def get_result(self, rdict, rlts, rt):
        rdict['result'] = rlts  #用例的执行结果存入字典
        rdict['rt'] = rt
        self.rs.append(rdict)

    def print_rltlist(self):
        """
        功能：打印用例标题
        :return:
        """
        for item in self.rs:
            print(f"{item['tc'].title}: {item['result']}   {item['rt']}")
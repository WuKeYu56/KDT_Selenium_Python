

class MyAssert:
    def __init__(self, driver):
        self.driver = driver

    def should_contain(self, expected, actual):
        if expected in actual:
            return True
        return False

    def should_exist(self, how, what):
        try:
            self.driver.find_element(how, what)
            return True
        except Exception as e:
            print(e)
            return False

    def should_eq(self, expected, actual):
        if expected == actual:
            return True
        return False
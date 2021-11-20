
dic = {"name" : "vadim", "age": 12, "age3": 12}


class Test:

    def func1(self):
        return self
    
    def func2(self):
        return 1


test = Test()
test.func1().func2()
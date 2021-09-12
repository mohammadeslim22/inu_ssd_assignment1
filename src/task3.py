import time
import io
import contextlib
import inspect
import pandas as pd

methods_list = []

import sys

class decorator_2:
    def __init__(self, meth):
        # self.f = open("D:\\err.txt", "a")
        # sys.stderr = self.f
        self.meth = meth
        decorator_2.counter = 0

    def __call__(self, *args, **kwargs):
        decorator_2.counter += 1
        begin = time.perf_counter()
        # ret = []
        # try:
        with contextlib.redirect_stdout(io.StringIO()) as o:
            return_result = self.meth(*args, **kwargs)
        end = time.perf_counter()
        global methods_list
        prints = o.getvalue()
        with open('prints.txt', 'a') as printer:
            printer.writelines(
                f"call {decorator_2.counter} for {self.meth.__name__} seconds excuted {end-begin} sec"+"\n")
            printer.writelines(f"Name : {self.meth.__name__} \n")
            printer.writelines(f"Type :{type(self.meth)} \n")
            printer.writelines(f"Sign:\t{inspect.signature(self.meth)}\n")
            myframe = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(myframe)
            printer.writelines(f"Args : positional {values['args']} \n  \t key=worded : {values['kwargs']}")
            printer.writelines(f"Doc:\t {self.meth.__doc__} \n")

            source = inspect.getsourcelines(self.meth)
            printer.writelines("Source: ")
            for ss in source[0]:
                printer.writelines(ss[0:-1])
            # printer.writelines(
            #     f"Source:{temp.join([line for line in inspect.getsourcelines(self.meth)[0]])}")
            printer.writelines("\n")
            printer.writelines(f"Output:\t {prints}")

        # except:
        #     print("Unexpected error:", sys.exc_info()[1])
        #     raise
        methods_list.append((self.meth.__name__, end-begin))
        return return_result



def printResult():

    methods_list.sort(key=lambda x: x[1]) #sort byt the execution time ( element 2 in the tuple)

    result_table = [[fun[0], i, '{0:.9f}'.format(
        fun[1])+"s"] for i, fun in enumerate(methods_list)]
    df = pd.DataFrame(result_table, columns=["Method", "RANK", "TIME"])
    print(df.to_string(index=False))

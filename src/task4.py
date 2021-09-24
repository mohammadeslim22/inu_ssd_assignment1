import time
import io
import contextlib
import inspect
import pandas as pd


methods_list = []
import sys
import datetime


class decorator_3:
    def __init__(self, function):
        self.f = open("D:\\err.txt", "a")
        sys.stderr = self.f
        self.f.writelines("\n")
        self.f.writelines("mohammad time stamp "+str(datetime.datetime.now()))
        self.f.writelines("\n")


        self.meth = function
        decorator_3.count = 0

    def __call__(self, *args, **kwargs):
        decorator_3.count += 1
        start = time.perf_counter()
        # ret = []
        try:
            with contextlib.redirect_stdout(io.StringIO()) as o:
                return_result = self.meth(*args, **kwargs)
            end = time.perf_counter()
            global methods_list
            prints = o.getvalue()
            with open('prints.txt', 'a') as printer:
                printer.writelines(
                    f"call {decorator_3.count} for {self.meth.__name__} seconds excuted {end-start} sec" + "\n")
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
        except:
            print("Unexpected error:", sys.exc_info()[1]," time stamp :", str(datetime.datetime.now()))
            # self.f.write(str(datetime.datetime.now()))
            # self.f.close()
            raise
        methods_list.append((self.fun.__name__, end-start))
        return return_result




def printOut():
    methods_list.sort(key=lambda x: x[1])  # sort byt the execution time ( element 2 in the tuple)

    result_table = [[fun[0], i, '{0:.9f}'.format(
        fun[1]) + "s"] for i, fun in enumerate(methods_list)]
    df = pd.DataFrame(result_table, columns=["Method", "RANK", "TIME"])
    print(df.to_string(index=False))

import time, io
import contextlib
import inspect

def decorator1(fun):
    def wrapper(*args,**kwargs):
        wrapper.count += 1
        start = time.perf_counter()
        # fun(*args, **kwargs)
        with contextlib.redirect_stdout(io.StringIO()) as f:
            fun(*args,**kwargs)
        end = time.perf_counter()
        myOut = f.getvalue()
        # print("alaa s is ", s)
        # print(f"{fun.__name__} excuted {end-start} sec")
        print(f"call {wrapper.count} for {fun.__name__} seconds excuted {end-start} sec")
        print("Name :" , fun.__name__)
        print("Type :",type(fun))
        print("Sign :", inspect.signature(fun))
        # print("Args :",inspect.signature(fun).)

        myframe = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(myframe)
        print("Args :", "positional ",values['args'] ,"\n\t\t key=worded : ", values["kwargs"])

        # for param in sig.parameters.values():
        #     print("param : ",param)
        print("Doc :",inspect.getdoc(fun))
        source = inspect.getsourcelines(fun)

        print("Source: ")
        for ss in source[0]:
            print(ss[0:-1])
        print("Output :",myOut)
        # print(inspect.isfunction(fun))
        # print(inspect.isfunction(fun))
        # print(inspect.getfullargspec(fun))


    wrapper.count = 0
    return wrapper





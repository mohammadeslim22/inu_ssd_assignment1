import time

def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        start = time.perf_counter()
        f(*args, **kwargs)
        end = time.perf_counter()
        print(f"{f.__name__} call count = {wrapped.calls} executed in " +
              '{0:.4f}'.format(end - start) , " sec")
    wrapped.calls = 0

    return wrapped

class MyList(list):
    @counted
    def poprgf(self, *args, **kwargs):
        return list.pop(self)

    @counted
    def addToList(self, *args, **kwargs):
        return list.append(self,*args)

x = MyList([7, 21, 12, 4, 5])
for i in range(3):
    x.poprgf()
    x.addToList(i)

print(x.poprgf.calls)
print(x.addToList.calls)
class RemoteControl:
    def __init__(s):
        s.channels=["HBO","CN"]
        s.index=-1
    def __iter__(s):
        return s
    def __next__(s):
        s.index+=1
        if s.index==len(s.channels):
            #best way to raise custom exceptions
            raise StopIteration
        return s.channels[s.index]


object1=RemoteControl()
ob=iter(object1)
print(ob)
print(f"Normal Next {ob.__next__()}")
print(f"new type of method call {next(ob)}")
#Exception
print(f"Exception {next(ob)}")


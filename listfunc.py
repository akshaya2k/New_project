import sys
def myfunc(nos):
    for i in nos:
        print(i)
if __name__ == "__main__":
    a = sys.argv[1].split(",")
    myfunc(a)


#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    res = 0
    for y in range(1, n):
        #print("{:d}".format(int(sys.argv[y])))
        res += (int(sys.argv[y]))
    print("{:d}".format(int(res)))

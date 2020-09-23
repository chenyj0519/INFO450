import sys
def add_them_all(filename):
    sum = 0
    with open (filename，"r") as fp:
            for line in fp.readlines():
                sum += int(line)
            fp.close()
            
    return sum
    
if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))

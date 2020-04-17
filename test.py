
import stdin, stdout
import numpy as np

def main():
    #f = open("I_O_file")
    
    res = np.array(stdin.readline().split()).astype(np.float)
        
    while(int(res[0]) >= 0):
        depRates = {}
        for i in range(int(res[-1])):
            k, v = f.readline().split()
            depRates[k] = float(v)

        i = 0
        dep = depRates[str(i)]
        owed = res[2]
        worth = (res[2]+res[1])*(1-dep)
        if(res[0] == 0):
            amount = res[2]
        else:
            amount = res[2]/res[0]
        while(worth < owed and i < res[0]):
            i = i + 1
            if(str(i) in depRates):
                dep = depRates[str(i)]
            
            owed = owed - amount
            worth = worth*(1-dep)
            
            #print("owed {}".format(owed))
            #print("worth {}".format(worth))
            

        if(i == 1):
            print("1 month")
        else:
            print("{} months".format(i))
        
        res = np.array(f.readline().split()).astype(np.float)
    
    #f.close()


if __name__ == "__main__":
    main()

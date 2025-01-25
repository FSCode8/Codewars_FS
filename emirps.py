import math

def find_emirp(n):
    
    number_of_emirps_below_n, largest_emirp_below_n, sum_of_emirps_below_n = 0, 0, 0
    
    log = math.ceil(math.log(n, 10))
    max = int(pow(10, log))

    prime = [True for i in range(max)]
    p = 2
    while (p * p <= max):
    
        if (prime[p] == True):
            for i in range(p * p, max, p):
                prime[i] = False
        p += 1
        
    for numb in range(13, n, 2):
        if prime[numb]:
            reversed = str(numb)[::-1]
            if reversed != str(numb):
                if prime[int(reversed)]:
                    number_of_emirps_below_n+=1
                    largest_emirp_below_n=numb
                    sum_of_emirps_below_n+=numb
        
    return [number_of_emirps_below_n, largest_emirp_below_n, sum_of_emirps_below_n] 
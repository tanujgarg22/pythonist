# ==========================================================
# IIT KHARAGPUR AI4ICPS HUB FOUNDATION
# Hands-on Approach to AI (Cohort 5), September 2026
# Programming Assignment 1
# ==========================================================

import sys

# ----------------------------------------------------------
# Function: frac
# Description: Computes the factorial of a number recursively.
# You are allowed to edit inside this function only.
# ----------------------------------------------------------
def frac(n):
    # TODO: Implement the recursive factorial function and remove the pass statement below.
    result=n
    while not (n==1):
        result = result * (n-1)
        n=n-1

    return result



# ----------------------------------------------------------
# Function: series
# Description: Computes the alternating factorial series
# S = Σ (-1)^k * (k * frac(k)) / (frac(k) + k^2), for k = 1 to ip
# Special rules:
#   - If ip < 0, return -999.0
#   - If ip == 0, return 0.0
#   - The final result must be rounded to two decimal places
# You are allowed to edit inside this function only.
# ----------------------------------------------------------
def series(ip):
    # TODO: Implement the logic for computing the series and remove the pass statement below.
    #factorial_k =frac(ip)
    #square_k=ip ** 2
    result=0
    if ip > 0:
        while not (ip == 0):
            factorial_k =frac(ip)
            square_k=ip ** 2
            kTimes_neg_one= ((-1) ** ip)
            #print(f"kTimes_neg_one {kTimes_neg_one} ip {ip} factorial {factorial_k} square_k {square_k}")
            result += (kTimes_neg_one*((ip *  factorial_k)/(factorial_k + square_k)))
            ip-=1
    elif ip==0:
        return round(0.00,2)
    elif ip <0:
        return (-999.0)
    return round(result,2)




# ----------------------------------------------------------
# Main function: DO NOT MODIFY
# ----------------------------------------------------------
if __name__ == "__main__":
    ip = int(sys.argv[1])
    #print(frac(ip))
    print(series(ip))
#!/bin/python3

import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player

def insert(list, n): 
      
    # Searching for the position 
    for i in range(len(list)): 
        if list[i] > n: 
            index = i 
            break
      
    # Inserting n in the list 
    list = list[:i] + [n] + list[i:] 
    return list

def climbingLeaderboard(ranked, player):
    # Write your code here
    out = []
    ranked = list( dict.fromkeys(ranked))
    ranked.sort(reverse=True)
    for x in player:
        if (x in ranked):
            out.append(ranked.index(x)+1)

        elif ( x not in ranked):
            if (x > ranked[0]):
                out.append(1)
            if (x < ranked[-1]):
                out.append(len(ranked)+1)
                continue
            for y in ranked:
                if ((x >= y) and (x<=ranked[ranked.index(y)-1])):
                    out.append(ranked.index(y)+1)
                

                
                
            
    
    return out



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

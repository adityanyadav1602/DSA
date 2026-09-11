#import saying
import sys

from saying import hello

if len(sys.argv)==2:
    hello(sys.argv[1])

for x in sys.argv[1:]:
    print(x)    

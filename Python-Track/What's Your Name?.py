#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    first_list=list(first)
    last_list=list(last)
    full_name="".join(first)
    full_name=full_name +" "+"".join(last)
    
    print( "Hello " +full_name+"! You just delved into python.")
    
    

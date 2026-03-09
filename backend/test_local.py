import ast
from code_parser import parse_and_comment

code1 = """
def square_numbers():
    for i in range(10):
        print(i*i)
"""

code2 = """
x = 10
if x > 5:
    print("Large number")
"""

try:
    print("Starting parse 1...")
    res1 = parse_and_comment(code1)
    print(res1)
    
    print("\nStarting parse 2...")
    res2 = parse_and_comment(code2)
    print(res2)
    print("SUCCESS")
except Exception as e:
    import traceback
    traceback.print_exc()



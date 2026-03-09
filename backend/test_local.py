import sys
from code_parser import parse_and_comment

code = """
def hello_world():
    print("Hello world")
    for i in range(5):
        print(i)
"""

try:
    print("Starting parse...")
    res = parse_and_comment(code)
    print("SUCCESS")
    print(res)
except Exception as e:
    import traceback
    traceback.print_exc()

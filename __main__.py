#!/usr/bin/python3
import argparse
from quicksearch.quicksearch import QuickSearch

parser = argparse.ArgumentParser(description='Find sting in string (Quicksearch algorithm)')
parser.add_argument('input', nargs="?", type=str, help='a string which should contain the pattern')
parser.add_argument('pattern', nargs="?", type=str, help='a string which is searched in the input')
parser.add_argument('--zh2018', action='store_true', required=False, help='runs the inbuilt test' )
args = parser.parse_args()

if not args.zh2018 and (not args.input or not args.pattern):
    parser.error('You must use either --zh2018 or give input and pattern')

def test(input: str = "BABCDBABACD", pattern: str = "BAC"):
    s = QuickSearch(input, pattern)
    print("""Input: {}
Pattern: {}
Offset: {}
Steps: {}
Jumptable: {}
""".format(
            s.input,
            s.pattern,
            s.offset,
            s.steps,
            s.jumptable
        )
    )

if __name__ == '__main__':
    try:
        if args.zh2018:
            test()
        else:
            test(args.input, args.pattern)
    except QuickSearch.NotFoundException as e:
        print(e.message)

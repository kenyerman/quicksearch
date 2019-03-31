# QuickSearch (Python 3)
Find substring in string

Needed this in uni to learn the algorithm.

Usage:
```
from quicksearch import QuickSearch
s = QuickSearch("find something in this", "something")
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
```
Usage from command line:

```
python -m quicksearch "find something in this" "something"
python -m quicksearch --help
```

# Truck Matching Solution

## Usage
To run the script:
```
python3 truck_matching.py [truck file] [distance file] [load file]
```

To run the unit tests:
```
python3 -m unittest truck_matching_unittest.TestTruckMatcher
```

This was tested with Python 3.7.3 on Mac OSX El Capitan 10.11.6

## Original solution
The original solution to this problem is given in the first commit in this repository.  It is something like I might have produced if this problem were given in person during a fixed time frame.

## Subsequent commits
I figured it might also be worth seeing what my style is when working, so I made further commits with improvements.  I am a firm believer in commit-early-commit-often.  One minor thing to note is that if this were the real world I would be working in a branch, not in master.  Commits would then be squashed and merged to master when all improvements were completed.

In subsequent commits, I made the original script into a more reusable class, created some unit tests, moved input files into a structure more useable by the tests, and added golden files for testing the output of the match_loads function.  I tried to make the unit test for the match\_loads function very easy to add test data to.  I view this to be important because when an edge case is detected and fixed, the original input that caused problems can simply be added to the test\_input directory, the expected output can be added to the test\_output directory, and correctness is tested from that point onwards with no code changes to the unit test itself.  I did not venture into adding negative tests, but that would be a good improvement to make in the future.

## Design decisions
My immediate thought when I saw this problem was that this was a classic single-source shortest-path problem.  If a load required multiple trucks to get to its destination creating a graph with origins and destinations as nodes and the distances provided as edges would be the way I would proceed.  Upon clarification I was told I could assume a single truck, so using dictionaries as simple lookups seemed to be the simplest solution.  Performance of dictionaries in Python is good, and most of the processing time of the script is going to be spent in parsing the input files.

I started by asking what kind of interface I would want given the inputs to get the desired results.  I came up with:

```python
truck_dict[origin][destination][equipment] = truck
distance_dict[origin][destination] = distance
```

I considered a single dictionary with a tuple of (truck, distance) as a value, but I didn't think it would add much, and the additional complexity of parsing data as given in the input into this structure outweighed the benefit of a single dictionary lookup for output.  If, for some reason, the input was different and different trucks with the same origin and destination had different distances (took different routes or something) this might be worth revisiting (but this requires different inputs so I viewed it as out of scope given the problem statement).

From there, knowing what kind of interface I wanted, I worked backwards to come up with the necessary data structures (which are obvious from the interface).  I parsed data into the data structures from the input format.  I chose CSV because the problem statment lists the data in a format that resembles a spreadsheet, and I thought given the problem space a CSV was not unlikely as an input format.  I used defaultdict to simplify the usage of a dictionary even further, and chose to use Python's csv module with a DictReader so that the lookups in the input would be human readable.

I chose to output both to the console and to a file.  I did this because I wanted to persist output, and I didn't view this as much as a library who's output would be further process as I did a standalone utility that produced final output.  Were it a library that generated data to be further processed I would have returned values from the match\_loads function rather than persisting output to disk and returning to the console.

## Final notes

There is still a lot of work that could be done here.  Input is assumed to be well formatted, for instance.  Negative unit tests could be added.  A lot of assumptions are made that may or may not be true.

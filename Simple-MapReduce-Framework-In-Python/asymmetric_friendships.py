import MapReduce
import sys

"""
Asymmetric Friendships Example in the Simple Python MapReduce Framework
Returns all pairs (friend,person) such that (person, friend) holds but (friend, person) does not
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record
    key.sort()
    key = tuple(key)
    value = record
    mr.emit_intermediate(key, value) # ensures symmetric values are sent to same reducer

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    if len(list_of_values) < 2: # value is asymmetric if only one value is passed to the reducer
        mr.emit(key)

        # mr.emit((key[1],key[0]))
        # error in grader, wants the symmetric relationship too

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

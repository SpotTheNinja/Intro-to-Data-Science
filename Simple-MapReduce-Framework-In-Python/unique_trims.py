import MapReduce
import sys

"""
Unique Trim Example in the Simple Python MapReduce Framework
Trims off the end of a sequence and returns all unique sequences
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence
    # value: dummy value
    key = record[1]
    key = key[:-10]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

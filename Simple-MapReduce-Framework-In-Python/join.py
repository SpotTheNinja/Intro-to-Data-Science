import MapReduce
import sys

"""
SQL Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: join attribute
    # value: all attributes -> the record
    key = record[1]

    mr.emit_intermediate(key,record)


def reducer(key, list_of_values):
    # key: join attribute
    # value: list of all attributes
    cross_dict = {}

    for v in list_of_values:

        if cross_dict.has_key(v[0]):
            cross_dict[v[0]].append(v)
        else:
            cross_dict[v[0]] = []
            cross_dict[v[0]].append(v)

    source_one = cross_dict.keys()[0]
    source_two = cross_dict.keys()[1]

    for i in cross_dict[source_two]:
       for j in cross_dict[source_one]:
           mr.emit(i+j)






# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

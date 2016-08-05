import MapReduce
import sys

"""
Sparse Matrix Multiplication Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    row_dim = 5
    col_dim = 5
    #outer dimension of matrix A and matrix B, respectively

    if record[0] == "a":
        for i in range(0,col_dim):
            key = (record[1],i)
            value = [record[0],record[2],record[3]]

            mr.emit_intermediate(key, value)

    elif record[0] == "b":
        for i in range(0,row_dim):
            key = (i, record[2])
            value = [record[0],record[1],record[3]]

            mr.emit_intermediate(key, value)


def reducer(key, list_of_values):

    row_dim = 5
    col_dim = 5
    nonzero_col = []
    nonzero_row = []

    a_values = filter(lambda x: x[0] == "a", list_of_values)
    b_values = filter(lambda x: x[0] == "b", list_of_values)

    a_set = set(map(lambda x: x[1], a_values))
    b_set = set(map(lambda x: x[1], b_values))
    a_b_intersect = a_set.intersection(b_set)
    # now we have a set of all indices row a and col b have in common

    # now grab the row/cols that have such an index
    a_mult = filter(lambda x: x[1] in a_b_intersect, a_values)
    b_mult = filter(lambda x: x[1] in a_b_intersect, b_values)

    # and multiply and sum them (# note the values we dont use are multiplied by zero and are not included in the sum)

    a_b_mult = map(lambda x,y: x[2]*y[2], a_mult,b_mult)

    mr.emit((key[0], key[1], sum(a_b_mult)))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Default Example
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#d1: 나는 파이썬이 좋다
#d2: 나는 스칼라가 좋다
#d3: 나는 스칼라가 좋다 스칼라가 좋다
####|나는|스칼라|파이썬|좋다
d1 = [1,0,1,1]     
d2 = [1,1,0,1]     
d3 = [1,2,0,2]     

def vector_inner_product(a, b):
    s = 0
    for i in range(len(a)):
        s += (a[i]*b[i])
    return s

def vector_size(v):
    s = 0
    for i in range(len(v)):
        s += v[i]**2
    return s**0.5

def cosine_similarity(a, b):
    numerator = vector_inner_product(a,b)
    denominator = vector_size(a) * vector_size(b)
    print( "> numerator   : %.10f" % numerator )
    print( "> denominator : %.10f" % denominator )
    return numerator/denominator

if __name__ == "__main__":
    print( "\n*** Cosine Similarity ***\n" )
    print( "%.10f\n" % cosine_similarity(a,b) )
    print( "%.10f\n" % cosine_similarity(d1,d2) )
    print( "%.10f\n" % cosine_similarity(d1,d3) )
    print( "%.10f\n" % cosine_similarity(d2,d3) )

# End of File

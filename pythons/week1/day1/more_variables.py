# -*- coding: utf-8 -*-

# x has to be assigned first for us
# to use it later in the computation
# let's set x to 3
x = 3

# stored value, x
print(x) # 3

# computation with x
print(3.9 * x * ( 1 - x )) # -23.4

# re-assignment of x with computation using x
# another way of thinking of = here is as 
# "update x to this new value, using prior x"
x = 3.9 * x * ( 1 - x )

print(x) # -23.4

x = 40
y = 41

print( x == y )
print( x == (y-1))
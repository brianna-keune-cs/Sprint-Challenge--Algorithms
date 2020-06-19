#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

the while loop is O(n ^ 3) but we add n ^ 2
to a each time we loop so 
O(n ^ 3)/O(n ^ 2) = O(n ^ 1) -> O(n)


b) O(n log n)

the for loop is O(n)
    because i has to go the length of n
and the while loop is O(log n)
    because j gets closer to n twice as fast
and then you multiply them



c) O(2 ^ n)

because we're returning 2 by how many bunnies there are

## Exercise II

Have a friend to count the broken eggs on level one. 
This friend also has a basket to collect and count non broken eggs.
While no eggs have broken I would continue to toss 1 egg from
each floor.
    If an egg breaks my friend calls me up 
        and tell me to stop tossing eggs.
We'd then count the eggs in the basket to determine
the amount of floors until eggs will start breaking.

Oh and this is linear search, O(n) because I count each floor until I find a broken egg.

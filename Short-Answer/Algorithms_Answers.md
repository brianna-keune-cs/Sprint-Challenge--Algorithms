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

linear search

Have a friend to count the broken eggs on level one. 
This friend also has a basket to collect and count non broken eggs.
While no eggs have broken I would continue to toss 1 egg from
each floor.
    If an egg breaks my friend calls me up 
        and tell me to stop tossing eggs.
We'd then count the eggs in the basket to determine
the amount of floors until eggs will start breaking.

Oh and this is linear search, O(n) because I count each floor until I find a broken egg.

binary search

I could also go to the middle story, which would be the amount of 
stories divided by two.
Throw an egg, and see if it broke.
If it did, I would then check the middle story number divided by two, so the middle stories middle, and if that broke. I would repeat dividing my current story by two until I was at the first story. If the egg broke at the first story I would have found f.
If the egg did not break on the original middle story I would find the middle floor between the nth story, and my current middle floor, and test another egg there.
I would repeat this process until I found the story right above where the egg does not break.

This runtime should be O(log n) because I'm finding where the egg doesn't break while only testing a max of half of the stories.

It's funny how doing a binary search in this problem, could cause more broken eggs, and would be more of a work out for me but it's easier for a computer while the linear search saves more eggs and could potentially be less of a work out for me.

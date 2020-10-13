#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
(line)  (code)
(1)     a = 0 - intializes the variable: O(1)
(2)     while (a < n * n * n): - if a is less n^3: O(1)  
(3)         a = a + n * n - var a is a + n^2: O(1)
    *Note( lines two and 3 make this alg an O(n)-constant time)



b)
(line)  (code)
(1)        sum = 0 O(1)
(2)        for i in range(n): \
                                O(1)
(3)            j = 1          / 
(4)            while j < n: \
(5)                j *= 2     O(n) 
(6)                sum += 1 /
    *Note(The nestesd O(n) loops makes this algorithm O(n log n)




c)
(line)  (code)
(1)     def bunnyEars(bunnies):
(2)         if bunnies == 0:\
                              O(1)
(3)             return 0    /
(4)
(5)         return 2 + bunnyEars(bunnies-1) ( makes the func O(n))
        *Note(At first glance this apears to be O(1) however the recursive return makes it O(n))


## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.



    Since the floors of a building have to be sorted in order, I would implement a binary search algorithm to determine the floor of F at which an egg breaks. - Next, I would slice the number of floors(f) in half, and drop an egg at that middle floor.

    If the egg breaks at this middle floor, we have one broken egg, one dropped egg, and eliminated the floors above that middle floor.

    After this, I would start making my way down on the floors until I reach the point where the eggs no longer break.

    If the egg did not break at the half way point when first tested, reverse the steps and work your way up the floors until the egg breaks.

    -This provides a blanace of eggs dropped and eggs broken. It also brings us a efficient runtime complexity of O(log N), which is faster than O(N)


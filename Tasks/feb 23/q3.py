"""

3. Given a tuple of integers, create a new tuple with only even numbers.

"""

tup = (1,2,3,4,5,6,7,8,9,10)

even = ()

for num in tup:

    if num % 2 == 0:

        even = even + (num,)

        """
        Without comma: even + num → TypeError (tuple + int doesn't work)

        With comma: even + (num,) → Works perfectly (tuple + tuple = new tuple)
        """

print(even)

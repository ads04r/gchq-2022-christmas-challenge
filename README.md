2022 GCHQ Christmas Challenge
=============================

https://www.gchq.gov.uk/news/xmaschallenge2022

I do this every year, and this year there was a question specifically
categorised as 'coding'. I could have solved it just using a pen and paper,
but I'm a programmer, and programmers do what programmers do. I took the
'coding' heading literally.

The challenge
-------------

```
F O R
M A T
I O N
```

1. Replace all the blue cells (O in the first row, M in the second and I in the third) with a letter from PART
2. Replace all the green cells (A in the second row and N in the third) with a letter from EYES
3. Replace all the gold cells (F on the first row, T in the second and O in the third) with a letter from UNCURL

After each step you should have three 3-letter words in the rows of the grid,
and you need to finish with a 9-letter word in the same formation as FORMATION.

My code
-------

My code basically does a brute force, starting with the 'FORMATION' grid
and generating every single possible valid exit point of the first step,
feeds each of these into the second step, again returning every possible
permutation, and then the same with the third.

Using a word list in the file words.txt ensures every step conforms to
the restrictions in the challenge, and it turns out there is just one
possible outcome, which is the correct answer.

Running this code will simply return that answer. It's how the code gets
to that answer that's interesting.

Why?
----

Why not?! I don't want to give away the answer, so
I have deliberately not put it in any of this text, you need to
actually run the code to get it.
I'm not trying to show off either, it's not a particularly nice piece
of code, I just found it fun to write, and I open
source my code unless there's a good reason not to do so.
The very best I can hope for is to encourage someone else to do
it better than me.

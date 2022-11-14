When memoizing a function, you make a note each time you call that function of a) the parameters and b) the result. Then next when you want to call the function again, you check in your notes whether you've called that function before with the parameters you want to use this time. If you have, you don't need to call the function again, because you already have the result. This way the function is called only as many times as you have distinct parameters: if you want to call it with parameters you've used already, you save having to call it.

This approach works well where a) the function is deterministic, i.e. returns the same value each time it is called with the same paramters, and b) the function is expensive compared to the cost of memoization.

The example you cite says this:

```
In the previous approach, many recursive calls had to made again and again with the same parameters. This redundancy can be eliminated by storing the results obtained for a particular call in a 2-d memorization array
```

Here the function in question is called O(2^n) times, but with only O(n^2) different sets of parameters. Using memoization, the function is called once only for each different parameter set (O(n^2)) rather than each time the algorithm needs the answer (O(2^n)).
# Stack Min

### Question:
How would you design a stack which, in additon to push and
pop, has a function min which returns the minimum element?

Push, pop, and min should all operate in *O(1)* time.


### Answer:

You could keep track of the smallest element in the stack
during all of the pushes and pops.

When an item is pushed to the top of the stack, check if it
is smaller than the current smallest. If so mark it as the 
smallest. 

If an item is popped there is an additional challenge. If 
the smallest item is popped off the stack their must be some
means of knowing the 2nd smallest item in the stack. If the 
2nd smallest item is popped the 3rd smallest must be known 
and so on.

One solution may be for each Node on the stack to store which
node below it is the smallest in the stack. If the smallest, node
is then equal to the node that is being popped, then the 
updated smallest node will be the smallest node beneath the
node being popped.

Ex. leftmost value is the Node value, 
- 0 is the smallest below it, 
- and Min is the smallest value so far.

```
-1 - 0, Min = -1
 0 - 1, MIN = 0
 2 - 1, MIN = 0
 3 - 1, MIN = 0
 2 - 1, MIN = 0
 1 - None, MIN = 0
```


**Insert whiteboard photos from overview**

![initial plan for project](plan1.jpg)

![](plan2.jpg)


Use MSPrime to run neutral coalescent simulation first
Then, use python script to overlay 





SLiM simulation for European population output is tree sequences:

These can be interpreted with pyslim package in Python.

For output of euro slim in python script (using packages tskit, pyslim, possibly msprime):
- generate _500 discrete pairs of 20 females, 20 males_
- mate them together, get pools of 1000 individuals (offspring of the groups of 20m, 20f)
- For each of these groups of 1000 (all isolated from each other), mate for 10 weeks (5 generations)
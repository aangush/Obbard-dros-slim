# Obbard-dros-slim

This is the repo for a SLiM evolutionary genetics simulation project

### Overview ###
Below is a description of each part of this project and what it does, I will do my best to keep this overview updated as I add new features.

The two important directories are `input` and `output`. `input` contains several SLiM simulation scripts (.txt or .slim files), as well as supporting python scripts, and `output` contains several different types of outputs from different scripts.

##### WF_euro.txt #####

The file `WF_euro.txt` is the SLiM script that is run to simulate the British/European Drosophila population. Many of the parameters set in this file can be changed (and probably will be when it is actually used), but here is a basic overview:

* this is a WF simulation, with separate sexes (though not sex chromosomes -- yet), with genome sizes of 100kb, and one single type of selected mutation 
* one initial subpopulation of 10k individuals is created (p1), and at the very end 500 subpops -- each with 2 individuals -- 1 male and 1 female is created with which to perform the crossing
* this script generates two output files 1) the default full SLiM output `euro_out.txt`, and more importantly 2) a tree sequence output `euro_trees.trees`

One slight issue with this file is that when the 500 subpops are split off from the main p1 to form the cross pairs, it is done **with** replacement


##### euro_convert.py #####

This python file is used to:

1. convert the WF tree sequence output from the `WF_euro.txt` simulation so it is compatible with a nonWF simulation.
2. assign sexes to the crossing pairs such that each pair ends up with 1 female and 1 male in the correct order

This file uses the python packages `pyslim` and `tskit`, and loads the tree sequence `euro_trees.trees` as an input
The output of this file is the `euro_processed.trees` tree sequence file, which is now ready to be used in a nonWF simulation 





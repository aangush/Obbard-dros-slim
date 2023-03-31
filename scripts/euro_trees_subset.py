import tskit

euro_ts = tskit.load("../output/euro_trees.trees")

print(f"The tree sequence has {euro_ts.num_trees} trees\n"
      f"on a genome of length {euro_ts.sequence_length},\n"
      f"{euro_ts.num_individuals} individuals, {euro_ts.num_samples} 'sample' genomes,\n"
      f"and {euro_ts.num_mutations} mutations.")


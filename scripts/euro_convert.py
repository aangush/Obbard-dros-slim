import pyslim, random, tskit

# load the WF euro tree sequences
ts = tskit.load("euro_trees.trees")

# unpack tree seqs to modifiable tables, necessary bc tree sequences are by default immutable
tables = ts.dump_tables()

# annotate the tables in a nonWF-style as SLiM expects for nonWF simulations
pyslim.annotate_tables(tables, model_type="nonWF", tick=1)

# randomly assign sexes to each individual (might not be necessary because the euro sim includes sexes?)
individual_metadata = [ind.metadata for ind in tables.individuals]
for md in individual_metadata:
  md["sex"] = random.choice(
    [pyslim.INDIVIDUAL_TYPE_FEMALE, pyslim.INDIVIDUAL_TYPE_MALE]
  )

# not quite sure what this is doing, it is included in the recipe SLiM manual pg 487
ims = tables.individuals.metadata_schema
tables.individuals.packset_metadata(
  [ims.validate_and_encode_row(md) for md in individual_metadata]
)

# convert the tables back into tree sequences, output new ts file
slim_ts = tables.tree_sequence()
slim_ts.dump("euro_processed.trees")
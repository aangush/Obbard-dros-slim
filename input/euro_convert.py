import pyslim, tskit

# load the WF euro tree sequences
ts = tskit.load("euro_trees.trees")

# unpack tree seqs to modifiable tables, necessary bc tree sequences are by default immutable
tables = ts.dump_tables()

# annotate the tables in a nonWF-style as SLiM expects for nonWF simulations,
# don't replace old mutations (annotate_mutations)
pyslim.annotate_tables(tables, model_type="nonWF", tick=1, annotate_mutations=False)

# assign sexes to all individuals so that small subpops each get 1 male, 1 female
individual_metadata = [ind.metadata for ind in tables.individuals]
for index, value in enumerate(individual_metadata, start=1):
    if index % 2 == 0:
        value["sex"] = pyslim.INDIVIDUAL_TYPE_FEMALE
    else:
        value["sex"] = pyslim.INDIVIDUAL_TYPE_MALE

# not quite sure what this is specifically doing, it is included in the recipe SLiM manual pg 487
ims = tables.individuals.metadata_schema
tables.individuals.packset_metadata(
    [ims.validate_and_encode_row(md) for md in individual_metadata]
)

# convert the tables back into tree sequences, output new ts file
slim_ts = tables.tree_sequence()
slim_ts.dump("euro_processed.trees")
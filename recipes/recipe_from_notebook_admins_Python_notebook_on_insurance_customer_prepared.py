# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read the dataset as a Pandas dataframe in memory
# Note: here, we only read the first 100K rows. Other sampling options are available
dataset_insurance_customer_prepared = dataiku.Dataset("insurance_customer_prepared")
df = dataset_insurance_customer_prepared.get_dataframe(limit=100000)
df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Get some simple descriptive statistics
pdu.audit(df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
insurance_customer_modeling = dataiku.Dataset("insurance_customer_modeling")
insurance_customer_modeling.write_with_schema(df)
# This is a comment
"""This
is
also
a
comment
"""

# We assign a string to a variable
message = "This is an object"

# Strings as built in types they are objects and as such have
# methods attached to them that operatate on the underlying data
# (the string)
message.split()
message.replace(" ", "-")

# With import or from/import we can include code from other files
from sklearn.datasets import load_wine

# load_wine is a function, we call it with arguments and catch its 
# return value
dataset = load_wine(as_frame=True)

# It is a dict. Calling .keys() gets us the keys for the key-value pairs
dataset.keys()

# That's a pandas dataframe
df = dataset.frame

# It is a tabular format. The table has some columns describing the data
df.columns

# We can access all the samples for one column (data "type") like that
df["alcohol"]
df[["alcohol", "magnesium", "target"]]

# Values gets us the numerical array - it is a numpy array
arr = df[["alcohol", "magnesium", "target"]].values

# E.g. a shape (100, 10) means 100 rows and 10 columns
arr.shape
# We can index any dimension with as single integer
arr[0].shape
# : means everything and comma is used to pass the next dimension indexer
arr[:, 0].shape

# :N means until N (the opposite also works)
arr[:10].shape
# Select first 10 items and first 2 columns
arr[:10, :2].shape

# Get items where the third colum (0, 1, 2, so the third) is 0 (class 0)
arr[arr[:, 2] == 0]

# Get mean values for these individually
arr[arr[:, 2] == 0][:, :2].mean(0)
arr[arr[:, 2] == 1][:, :2].mean(0)
arr[arr[:, 2] == 2][:, :2].mean(0)

# Transpose is "flipping" / "mirroring" the array diagonally
arr = arr.T
arr[:, arr[2] == 0][:2].mean(0)

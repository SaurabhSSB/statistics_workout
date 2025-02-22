from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
cosine_similarity([[3,1]],[[6,2]])
cosine_distances([[3,1]],[[6,2]])
cosine_similarity([[3,1]],[[3,2]])

doc1= """
Right way to enter the unknown is through the know, to find the unknown stead fast.
"""
doc2= """
The unknown can only be known through the known as known is the foundation.
"""
doc3= """
What's unknown might be known in the coming future so don't underestimate the unknown for known.
"""

import pandas as pd
df= pd.DataFrame([
  {'unknown': 2,"known": 1},
  {'unknown': 1,"known": 2},
  {'unknown': 2,"known": 2}
  ], 
  index=[
    "doc1", "doc2", "doc3"
  ]
)
df
cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc2":"doc2"])
cosine_similarity(df.loc["doc1":"doc1"],df.loc["doc3":"doc3"])
cosine_similarity(df.loc["doc3":"doc3"],df.loc["doc2":"doc2"])

cosine_distances(df.loc["doc1":"doc1"],df.loc["doc2":"doc2"])
cosine_distances(df.loc["doc1":"doc1"],df.loc["doc3":"doc3"])
cosine_distances(df.loc["doc3":"doc3"],df.loc["doc2":"doc2"])

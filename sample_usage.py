from wrappers.Index import Index
from wrappers.Data import Data
from wrappers.VectorDBWrapper import VectorDBWrapper
import pinecone

print("Getting the pinecone instance")
VectorDBWrapper().get_instance(pinecone)

print("Creating the index")
index = Index(pinecone)
index_name = "quickstart"
index.create_index(index_name, dimension=8, metric="euclidean")

print("Getting the index stats")
index.describe_index_stats(index_name)

print("Upserting the data")
data = Data(pinecone)
data.upsert(index_name, [
    ("A", [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),
    ("B", [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]),
    ("C", [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
    ("D", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]),
    ("E", [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
])

print("Querying the index")
print(data.query(index_name,
  vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.2, 1.0],
  top_k=3
))
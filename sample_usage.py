import pinecone
from wrappers.PineConeWrapper import PineConeWrapper
from wrappers.Index import Index
from wrappers.Data import Data

print("Getting the pinecone instance")
pinecone = PineConeWrapper().get_instance()

print("Creating the index")
index = Index(pinecone)
index_name = "quickstart"
index.create_index(index_name, dimension=8, metric="euclidean")

print("Getting the index stats")
index.describe_index_stats()

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
print(index.query(
  vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.2, 1.0],
  top_k=3
))
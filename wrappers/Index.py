
class Index:
    def __init__(self, pinecone):
        self.pinecone = pinecone

    def create_index(self, index_name, dimension, metric):
        self.pinecone.create_index(index_name, dimension=dimension, metric=metric)

    def describe_index(self, index_name):
        self.pinecone.describe_index(index_name)

    def describe_index_stats(self, index_name):
        self.pinecone.Index(index_name).describe_index_stats()
    
    def delete_index(self, index_name):
        self.pinecone.delete_index(index_name)

    def list_indexes(self):
        self.pinecone.list_indexes()
import pinecone

class Index:
    def __init__(self, pinecone_instance = pinecone):
        self.pinecone_instance = pinecone_instance

    def create_index(self, index_name, dimension, metric):
        self.pinecone_instance.create_index(index_name, dimension, metric)

    def describe_index(self, index_name):
        self.pinecone_instance.describe_index(index_name)

    def describe_index_stats(self, index_name):
        self.pinecone_instance.Index(index_name).describe_index_stats()
    
    def delete_index(self, index_name):
        self.pinecone_instance.delete_index(index_name)

    def list_indexes(self):
        self.pinecone_instance.list_indexes()
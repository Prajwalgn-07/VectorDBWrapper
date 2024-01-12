import pinecone

class Data:
    def __init__(self, pinecone_instance = pinecone):
        self.pinecone_instance = pinecone_instance

    def upsert(self, index_name, data):
        self.pinecone_instance.Index(index_name).upsert(data)
        
    def query(self, index_name, vector, top_k, include_values=True):
        return self.pinecone_instance.Index(index_name).query(vector, top_k, include_values)
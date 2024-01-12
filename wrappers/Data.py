class Data:
    def __init__(self,pinecone):
        self.pinecone = pinecone

    def upsert(self, index_name, data):
        self.pinecone.Index(index_name).upsert(data)
        
    def query(self, index_name, vector, top_k, include_values=True):
        return self.pinecone.Index(index_name).query(vector=vector,top_k = top_k, include_values = include_values)
from wrappers.Config import Config

class VectorDBWrapper:

    def  __init__(self):
      self.config = Config()


    def get_instance(self,pinecone):
      pinecone.init(api_key=self.config.api_key, environment=self.config.environment)
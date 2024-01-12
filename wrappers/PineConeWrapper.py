from wrappers.Config import Config
import pinecone

class PineConeWrapper:

    def  _init_(self):
        self.config = Config()
    

    def get_instance(self):
        return pinecone.init(api_key=self.config.api_key, environment=self.config.environment)
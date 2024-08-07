from dotenv import load_dotenv
import os
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from pinecone.core.grpc.protos.vector_service_pb2 import UpsertResponse
from pinecone.grpc.future import PineconeGrpcFuture
from rapid_law.components.cohere_utils import cohere_embed
from rapid_law.components.ollama_utils import ollama_embed

load_dotenv()

# Access environment variables
pinecone_api_key = os.getenv('PINECONE_API_KEY')


pc = Pinecone(api_key=pinecone_api_key)

def create_index(
    index_name : str,
    dimension : int,
    cloud : str = 'aws',
    region : str = 'us-east-1',
    metric : str = "cosine"
):
    try:
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=dimension,
                metric=metric,
                spec=ServerlessSpec(
                    cloud=cloud, 
                    region=region
                ) 
            ) 
    except Exception as e:
        print(f"An error occurred in create_index function: {e}")
    

def pinecone_upsert(
    index_name : str,
    title : str,
    text : str,
    metadata : dict,
    namespace : str = "ns1"
):

    index = pc.Index(index_name)
    print(text)
    
    value = ollama_embed(text=text,)
    # value = cohere_embed(text=text,)
    
    index.upsert(
        vectors=[
            {
                "id": title, 
                "values": value, 
                "metadata": metadata
            }
        ],
        namespace=namespace
    )


def pinecone_query(
    index_name : str,
    query : str,
    namespace : str = "ns1",
    top_k : int = 3,
    include_values : bool = False,
    include_metadata : bool = True,
):
    index = pc.Index(index_name)

    value = ollama_embed(text=query,)
    # value = cohere_embed(text=query,)
    response = index.query(
        namespace=namespace,
        vector=value,
        top_k=top_k,
        include_values=include_values,
        include_metadata=include_metadata,
    )
    print(response)
    return response

# x = pinecone_query("rapid-laws", "What's your name?", include_values=False)
# print(x)
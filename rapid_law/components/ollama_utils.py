import ollama
from ollama._types import Options

def ollama_embed(
    text : str,
    model : str = 'snowflake-arctic-embed'
):
 
    embedding = ollama.embeddings(
        model = model,
        prompt = text,
    )
    return embedding['embedding']



def ollama_text_generation(
    query : str,
    model_name : str = 'phi3',
    temperature : float = 0.5,
    stream : bool = False
):
    if stream:
        values = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': query}],
            stream=stream
        )

        response = ''.join([item['message']['content'] for item in values if 'content' in item['message']])
        return response
    
    else:
        response = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': query}],
            stream=stream,
            options=Options(temperature=temperature)
        )

        return response['message']['content']

# values = ollama_text_generation(query="Who are you?",stream=True)
# sentence = ''.join([item['message']['content'] for item in values if 'content' in item['message']])
# print(sentence)

# values = ollama_text_generation(query="Who are you?")
# print(values)
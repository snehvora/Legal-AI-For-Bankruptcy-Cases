import cohere
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)

def gemini_embed(
    text : str,
    model : str = 'models/embedding-001',
    input_type : str = "retrieval_document"
):
 
    response = genai.embed_content(model=model,
                                content=text,
                                task_type=input_type)
    return response['embedding']



def gemini_text_generation(
    query : str,
    model_name : str = "gemini-1.5-flash",
    temperature : float = 0.0,
    stream : bool = False
):
    if stream:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            query,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
            ),
            stream=True
        )

        return response
    
    else:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(
            query,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
            )
        )

        return response.text

# x = gemini_embed("Tell me the overview of bankcurrency")
# print(len(x))
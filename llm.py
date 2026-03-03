from openai import OpenAI

# Initialize the client 
client = OpenAI(
    base_url="http://100.66.150.89:8080/v1",
    api_key="nothing" 
)

def generate_explanation(facts, evaluation):   

    eval = "White" if evaluation/100 > 0 else "Black"


    prompt = f"""
    You are a Natural Langauge Generator. You take in queries and translate them into natural language.
    You must follow all the rules listed below, without any deviation.

    RULES: 
    - You do not infer, think, or make any information outside of the scope of the facts given.
    - You always use all the facts given
    - You only output the template shown below.
    
    ON-BOARD FACTS:
    {facts}
    
    TASK:
    Translate the facts given into natural language. 
    
    OUTPUT:
    Your ouput should always follow this exact template:

   " The evaluation is: {(evaluation/100)}. This means that {eval} is winning.
    The description of the position is as follows: 
    {{your translated facts}}


    """

    response = client.chat.completions.create(
        model="Meta-Llama-3.1-8B-Instruct.Q4_K_M.gguf",
        messages=[
            {"role": "system", "content": "You are a Natural Language Generator Bot. Follow all instructions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
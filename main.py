from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

input_text = '''
Software modeling is the process of creating abstract representations of a software system. These models serve as blueprints that guide developers, designers, and stakeholders through the system’s structure, behavior, and functionality.

By using diagrams and various modeling languages, software modeling helps in visualizing and understanding the complex aspects of the software, making it easier to plan, develop, and manage the system.
'''

def main():
    print ("Hello from briefly")
    llm = ChatOllama(
        model="deepseek-r1:latest", 
        temperature=0, 
        verbose=True,     
        validate_model_on_init=True,
    )
    
    print("llm")

    
    prompt = ChatPromptTemplate.from_template(
        "You are a concise summarizer. Summarize the following text in 5-8 bullet points:\n{input_text}"
    )
    
    print("prompt")

    chain = prompt | llm
    
    print("chain")
    print("invoked")

    response = chain.invoke(
        {
            "input_text": f"{input_text}"
        }
    )
    print("invoked")
    print(response.content)
    


if __name__ == "__main__":
    main()

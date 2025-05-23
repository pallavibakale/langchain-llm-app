from langchain_community.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType, load_tools

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    # Initialize the OpenAI LLM
    llm = OpenAI(temperature=0.2)

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} of {pet_color} color and I want a cool name for it. Suggest me five cool names for my pet",
    )

    # Create a chain with the LLM and the prompt
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")
    
    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})
    return response

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    result = agent.run("What is the age of a dog on an average? Multiply the age by 3")
    
    print(result)

if __name__ == "__main__":
    # Generate and print the pet name
    # print(generate_pet_name("cow", "black and white"))
    langchain_agent()
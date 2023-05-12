from langchain.llms import OpenAI
from langchain import PromptTemplate

def get_llm(openai_apikey, item, price):

    template = """

    You are a helpful chatbot and act like a salesman to find the best option for your user.
    Your goal is:
    -to understand what your user wants to purchase with the desired price range,
    -search for the best options for your user,
    -narrow down the best options to 3 items,
    -list the all without any further question to your user,
    -ask your user's permission to purchase the one indicated by the user.

    Your user tells you:
    REQUEST: {item}
    PRICE RANGE: \${price[0]} to \${price[1]}.

    YOUR RESPONSE:
    """

    prompt = PromptTemplate(
        input_variables=['item', 'price'],
        template=template,
    )

    def load_llm():
        llm = OpenAI(temperature=0.2, openai_api_key=openai_apikey)
        return llm

    llm = load_llm()

    item_prompt = prompt.format(item=item, price=price)
    response = llm(item_prompt)

    return response
from google.adk.agents.llm_agent import Agent

def get_bank_information(user_query: str) -> dict:
    """
        Retrieve information related to Bank and its products, services and processes. 
        The information is available as a static object with FAQ as keys and their responses as values. 
        
        Args:
            User query that needs to be answered.

        Returns:
            dict: status and result or error message. 
    """
    faq = {
        "how do i open a new savings account": "Opening a savings account with our Bank is simple. You can apply online through our website in about 10 minutes, or visit any local branch. You will need two forms of identification (such as a Driver's License and a Social Security Card) and an initial deposit of at least $25.00.",
        "what should i do if i lost my credit card": "If your card is lost or stolen, please log in to the Bank Mobile App immediately and select 'Lock Card' to prevent unauthorized transactions. Afterward, call our 24/7 fraud support line at 1-800-XXX-XXXX to request a replacement card, which will arrive in 5-7 business days.",
        "what types of vehicle loans do you offer": "The Bank offers loans for new and used car purchases, as well as refinancing options for existing auto loans. We also offer specialized financing for recreational vehicles (RVs) and motorcycles. Loan terms typically range from 36 to 72 months depending on the vehicle age.",
        "do i really need a demat account to buy stocks": "Yes. In today's market, shares are held in electronic format rather than as physical paper certificates. The Bank Demat account acts like a digital wallet for your securities, allowing you to hold shares, bonds, and mutual funds safely and securely.",
        "what is the interest rate for a 1 year fixed deposit": "For a standard 1-year Fixed Deposit, the Bank currently offers an interest rate of 6.50% p.a. for general citizens and 7.00% p.a. for Senior Citizens. Rates are subject to change, so please check our 'Rates' page on the website for the most current figures." 
    }

    user_query = user_query.lower().replace("?","")
    print(user_query)
    if user_query in faq:
        print("Match with FAQ")
        result = faq.get(user_query)
    else:
        print("Couldnt Match with FAQ")
        result = "Please find information related to this query on the Bank's website or talk to our agent at 1-800-XXX-XXXX who can assist on it."
    
    return {
        "status": "success",
        "result": result
    }


root_agent = Agent(
    model='gemini-2.5-flash',
    name='customer_service_representative',
    description='A helpful assistant that answers Bank customer queries and provide them information on its products, and services',
    instruction='Answer user questions related to bank and provide them information about its services, products and processes',
    tools=[get_bank_information]
)

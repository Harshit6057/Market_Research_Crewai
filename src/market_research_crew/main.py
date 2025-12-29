

from market_research_crew.crew import MarketResearchCrew



def run():
    """
    Run the crew.
    """
    inputs = {
        'product_idea': 'An AI powered tool that summarizes youtube videos on my channel and posts the summary on various social media plateforms like LinkedIn, Whatsapp, Instagram, X'
    }
    try:
        
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occured while running the crew: {e}")



from crewai import Crew, Process
from textwrap import dedent
from brad_analysis_agents import BradAnalysisAgents
from brad_analysis_tasks import BradAnalysisTasks
import signal
import sys



from langchain_openai import ChatOpenAI

from langchain_groq import ChatGroq

from langchain_google_genai import ChatGoogleGenerativeAI




from dotenv import load_dotenv
load_dotenv()


def signal_handler(sig, frame):
    print('Received shutdown signal, exiting...')
    sys.exit(0)

# Register signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)




class FinancialCrew3o1:
  def __init__(self, company):
    self.company = company
    self.llm = ChatGroq(
                    temperature=0.01, 
                    groq_api_key="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", 
                    model_name="gemma-7b-it"
                )


    
    
    
  def run(self):
   
    
    agents = BradAnalysisAgents()
    tasks = BradAnalysisTasks()

    self.llm = ChatGroq(
                    temperature=0.01, 
                    groq_api_key="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", 
                    model_name="gemma-7b-it"
                )



    
    
    
    
    banner_brands_researcher=agents.sup_banner_brands_researcher()
    
    

    

    
   
    find_banner_brands = tasks.find_banner_brands(banner_brands_researcher, self.company)
    
    

    crew = Crew(
      agents=[
        
        banner_brands_researcher,
      
      ],
      
      tasks=[
        
        find_banner_brands,

      ],
      verbose=True,
      function_calling_llm=self.llm,
      process=Process.sequential,
      max_rpm=1,
      manager_llm=self.llm
    )

    result = crew.kickoff()
    return result
  


if __name__ == "__main__":
  print("## Welcome to Brad's AICrew")
  print('-------------------------------')
  company = input(
    dedent("""
      What is the company you want to analyze?
    """))
  
  financial_crew = FinancialCrew3o1(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

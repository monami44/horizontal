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





class FinancialCrew00:
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


    
    
    
    

    
    
    
    headquaters_researcher = agents.headquaters_researcher()
    
    

    
    
    
    find_headquaters = tasks.find_headquaters(headquaters_researcher, self.company)

    
    

    crew = Crew(
      agents=[
        
        headquaters_researcher,
      
      ],
      
      tasks=[
        
        find_headquaters,

      ],
      verbose=True,
      function_calling_llm=self.llm,
      max_rpm=1,
      max_tokens=1428,
      process=Process.sequential,
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
  
  financial_crew = FinancialCrew00(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)


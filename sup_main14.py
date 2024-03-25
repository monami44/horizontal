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



class FinancialCrew8o1:
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

    
    
    
    
    
    top_5_strategic_initiatives_researcher=agents.sup_top_5_strategic_initiatives_researcher()
    
    

    

    
    
    find_top_5_strategic_initiatives = tasks.find_top_5_strategic_initiatives(top_5_strategic_initiatives_researcher, self.company)
    

    crew = Crew(
      agents=[
        
        top_5_strategic_initiatives_researcher,
      
      ],
      
      tasks=[
        
        find_top_5_strategic_initiatives,

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
  
  financial_crew = FinancialCrew8o1(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

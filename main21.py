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




class FinancialCrew14:
  def __init__(self, company):
    self.company = company
    self.llm = ChatGroq(
                    temperature=0.01, 
                    groq_api_key="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", 
                    model_name="mixtral-8x7b-32768"
                )

    
    
    
  def run(self):
    
    
    agents = BradAnalysisAgents()
    tasks = BradAnalysisTasks()

    self.llm = ChatGroq(
                    temperature=0.01, 
                    groq_api_key="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", 
                    model_name="mixtral-8x7b-32768"
                )

    
    
    
    
    executive_moves_researcher=agents.executive_moves_researcher()
    
    

    

    
    search_executive_moves= tasks.search_executive_moves(executive_moves_researcher, self.company)
    
    

    crew = Crew(
      agents=[
       
        executive_moves_researcher,
      
      ],
      
      tasks=[
       
        search_executive_moves,

      ],
      verbose=True,
      function_calling_llm=self.llm,
      process=Process.sequential,
      max_rpm=1,
      max_tokens=1428,
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
  
  financial_crew = FinancialCrew14(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

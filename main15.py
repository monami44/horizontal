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



class FinancialCrew9:
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

    
    
    
    
    worries_risks_and_concerns_researcher=agents.worries_risks_and_concerns_researcher()
    
    
    

    

    
    find_worries_risks_and_concerns = tasks.find_worries_risks_concerns(worries_risks_and_concerns_researcher, self.company)
    

    
    

    crew = Crew(
      agents=[
        worries_risks_and_concerns_researcher,
        
      
      ],
      
      tasks=[
        find_worries_risks_and_concerns,
        

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
  
  financial_crew = FinancialCrew9(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

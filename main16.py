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




class FinancialCrew10:
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

    
    
    
    
    
    main_competitors_researcher=agents.main_competitors_researcher()
    
    

    

    
    
    find_main_competitors = tasks.find_main_competitors(main_competitors_researcher, self.company)

    
    

    crew = Crew(
      agents=[
    
        main_competitors_researcher,
      
      ],
      
      tasks=[
  
        find_main_competitors,

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
  
  financial_crew = FinancialCrew10(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

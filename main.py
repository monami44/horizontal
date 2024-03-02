from crewai import Crew, Process
from textwrap import dedent
from brad_analysis_agents import BradAnalysisAgents
from brad_analysis_tasks import BradAnalysisTasks
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()



class FinancialCrew:
  def __init__(self, company):
    self.company = company
    
  def run(self):
    
    agents = BradAnalysisAgents()
    tasks = BradAnalysisTasks()

    self.llm = ChatOpenAI(model='gpt-4-0125-preview')
    
    
    legal_company_name_researcher = agents.legal_company_name_researcher()
    headquaters_researcher = agents.headquaters_researcher()
    year_incorporated_researcher = agents.year_incorporated_researcher()
    lines_of_business_researcher = agents.lines_of_business_researcher()
    brief_synopsis_of_company_researcher = agents.brief_synopsis_researcher()
    banner_brands_researcher = agents.banner_brands_researcher()
    target_market_researcher = agents.target_market_researcher()
    revenue_researcher = agents.revenue_researcher()
    financial_performance_2023_researcher = agents.financial_performance_2023_researcher()
    market_capitalization_researcher = agents.market_capitalization_researcher()
    company_owner_researcher = agents.company_owner_researcher()
    founding_story_researcher = agents.founding_story_researcher()
    key_points_of_difference_researcher = agents.key_points_of_difference_researcher()
    top_5_strategic_initiatives_researcher = agents.top_5_strategic_initiatives_researcher()
    worries_risks_and_concerns_researcher = agents.worries_risks_and_concerns_researcher()
    main_competitors_researcher = agents.main_competitors_researcher()
    swot_analysis_expert = agents.swot_analysis_expert()
    store_designer_researcher = agents.store_designer_researcher()
    lead_visual_market_analist= agents.lead_visual_market_analist()
    news_researcher = agents.news_researcher()
    market_research_manager = agents.market_research_manager()
    

    

    
    find_legal_company_name = tasks.find_legal_company_name(legal_company_name_researcher, self.company)
    find_headquaters = tasks.find_headquaters(headquaters_researcher, self.company)
    find_year_incorporated = tasks.find_year_incorporated(year_incorporated_researcher, self.company)
    find_line_of_business = tasks.find_line_of_business(lines_of_business_researcher, self.company)
    find_brief_synopsis = tasks.find_brief_synopsis(brief_synopsis_of_company_researcher, self.company)
    find_banner_brands = tasks.find_banner_brands(banner_brands_researcher, self.company)
    find_target_market = tasks.find_target_market(target_market_researcher, self.company)
    find_revenue = tasks.find_revenue(revenue_researcher, self.company)
    find_financial_performance_2023 = tasks.find_financial_performance_2023(financial_performance_2023_researcher, self.company)
    find_market_capitalization = tasks.find_market_capitalization(market_capitalization_researcher, self.company)
    find_company_owner = tasks.find_company_owner(company_owner_researcher, self.company)
    find_founding_story = tasks.find_founding_story(founding_story_researcher, self.company)
    find_key_points_of_difference = tasks.find_key_points_of_difference(key_points_of_difference_researcher, self.company)
    find_top_5_strategic_initiatives = tasks.find_top_5_strategic_initiatives(top_5_strategic_initiatives_researcher, self.company)
    find_worries_risks_concerns = tasks.find_worries_risks_concerns(worries_risks_and_concerns_researcher, self.company)
    find_main_competitors = tasks.find_main_competitors(main_competitors_researcher, self.company)
    create_swot_analysis = tasks.create_swot_analysis(swot_analysis_expert, self.company)
    find_store_designer_agency = tasks.find_store_designer_agency(store_designer_researcher, self.company)
    analyse_visual_market = tasks.analyse_visual_market(lead_visual_market_analist, self.company)
    search_news = tasks.search_news(news_researcher, self.company)
    manage_market_research = tasks.manage_market_research(market_research_manager, self.company, [find_legal_company_name, find_headquaters, find_year_incorporated, find_line_of_business, find_brief_synopsis, find_banner_brands, find_target_market, find_revenue, find_financial_performance_2023, find_market_capitalization, find_company_owner, find_founding_story, find_key_points_of_difference, find_top_5_strategic_initiatives, find_worries_risks_concerns, find_main_competitors, create_swot_analysis, find_store_designer_agency, analyse_visual_market, search_news])
    

    crew = Crew(
      agents=[
        legal_company_name_researcher,
        headquaters_researcher,
        year_incorporated_researcher,
        lines_of_business_researcher,
        brief_synopsis_of_company_researcher,
        banner_brands_researcher,
        target_market_researcher,
        revenue_researcher,
        financial_performance_2023_researcher,
        company_owner_researcher,
        founding_story_researcher,
        key_points_of_difference_researcher,
        top_5_strategic_initiatives_researcher,
        worries_risks_and_concerns_researcher,
        main_competitors_researcher,
        swot_analysis_expert,
        store_designer_researcher,
        lead_visual_market_analist,
        news_researcher,
        market_research_manager  
      ],
      
      tasks=[
        find_legal_company_name,
        find_headquaters,
        find_year_incorporated, 
        find_line_of_business, 
        find_brief_synopsis,
        find_banner_brands,
        find_target_market,
        find_revenue,
        find_financial_performance_2023, 
        find_market_capitalization,   
        find_company_owner, 
        find_founding_story, 
        find_key_points_of_difference, 
        find_top_5_strategic_initiatives, 
        find_worries_risks_concerns, 
        find_main_competitors, 
        create_swot_analysis, 
        find_store_designer_agency, 
        analyse_visual_market,
        search_news,
        manage_market_research

      ],
      verbose=True,
      process=Process.hierarchical,
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
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)

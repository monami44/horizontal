from crewai import Task
from textwrap import dedent



class BradAnalysisTasks():
    
  def find_legal_company_name(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is singular but critical: to find the legal company name of the specified company. This information is crucial for all subsequent analyses and decisions, serving as the foundation for our strategic planning.

Specific Instructions:

Research:

Conduct thorough investigations into corporate filings, legal documents, and public records related to the target company. Utilize databases such as EDGAR (for U.S.-based companies), Companies House (for U.K.-based companies), and other national and international corporate registries.
Employ advanced search techniques and queries to sift through digital and physical archives, ensuring no stone is left unturned in the quest for the company's legal name.
Verification:

Verify the authenticity and accuracy of the found information through cross-referencing with multiple sources. This may include checking against recent legal filings, press releases, official company communications, and regulatory body announcements.
Ensure that the legal name identified is current and reflects any recent changes due to mergers, acquisitions, rebranding, or other corporate restructuring events.

Deliverables:

A concise report detailing the legal company name of the target company, supported by evidence and a clear explanation of the research process and verification methods employed.

Objective:
Your primary objective is to deliver precise and verified information regarding the legal name of the target company. This foundational data is critical for enabling further strategic analysis and decision-making, affirming the importance of accuracy, thoroughness, and attention to detail in your research. Your expertise and diligence in this task reinforce your role as a key player in the team, setting the stage for comprehensive market analyses that rely on the solid groundwork you provide.
                                   

                                    Helpful Tips:
                - To find the legal company name, perform searches on Google such like the following:
                    - "{company} legal company name"
                                   
                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
Parameters:
                - Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_legal_company_name.txt",
            expected_output=dedent(
                """


                Example Output:
                {
                    legal company name: "The legal company name of Walmart Inc"
               }
                """
            )
        )
 
  
  def find_headquaters(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is clear: Find the headquarters address of the company provided by the user. This task is crucial, as the location of a company's headquarters can reveal much about its operational focus, logistical capabilities, and regional influence.

Specific Instructions:

Geospatial Analysis:

Employ advanced geospatial analysis techniques to locate the headquarters of the specified company. This may involve utilizing satellite imagery, GIS databases, and other geolocation tools to verify the physical address.
Cross-reference findings with official corporate documents, regulatory filings, and credible business directories to ensure accuracy.
Verification Process:

Conduct a thorough verification process to confirm the headquarters address. This could involve cross-checking with multiple authoritative sources, including company websites, business registration authorities, and recent press releases or company announcements.
Pay particular attention to any recent relocations, expansions, or other changes that could affect the current validity of the headquarters address.
Strategic Insights:

Deliverables:

A comprehensive report detailing the headquarters address of the specified company.
                                   
Objective:
Your primary objective is to deliver an accurate and verified headquarters address for the specified company, providing a critical foundation for further strategic analysis. Through your expert geospatial analysis and meticulous verification process, you will offer invaluable insights that enhance the strategic planning capabilities of your team, reinforcing your role as a pivotal asset in the intelligence community.

                                    Helpful Tips:
                - To find the headquaters address, perform searches on Google such like the following:
                    - "{company} headquaters address"


                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
  - Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_headquaters.txt",
            expected_output=dedent(
                """
              

                Example Output:
                {
                   Headquarters adress: "The headquarters of Walmart  are located in Bentonville, Arkansas, USA."
               }
                """
            )
        )
   

  def find_year_incorporated(self, agent, company):
    return Task(description=dedent(f"""
Your mission is to pinpoint the exact year of incorporation for the company specified by the user. This information is vital for a comprehensive understanding of the company's history and foundational context.

Specific Instructions:

Historical Research:

Conduct a deep dive into corporate archives, legal documents, and public registries to locate the original incorporation documents of the specified company. Utilize both digital and physical sources, including national and state archives, corporate registries, and historical business databases.
Document Analysis:

Analyze the found incorporation documents with a forensic approach, focusing on extracting the official date of incorporation. Pay attention to any amendments or re-incorporations that might have occurred, ensuring the date reflects the company's original establishment.
Verification Process:

Verify the accuracy of the incorporation year through cross-referencing with multiple authoritative sources. This may include historical business records, government databases, and other legal documents that confirm the company's registration date.
Report Compilation:

Compile your findings into a concise report that details the year of incorporation.
Ensure the report is clear, well-organized, and professional, suitable for inclusion in broader strategic analyses.
Deliverables:

A detailed report presenting the year of incorporation for the specified company.
Objective:
Your primary objective is to provide an accurate and verified year of incorporation for the specified company, enriching the strategic analysis with a foundational understanding of its origins. Through your expert historical research and meticulous documentation, you will illuminate the company's inception, offering a critical piece of the puzzle in understanding its evolution and strategic positioning. Your work is not just an exercise in historical retrieval but a vital contribution to the strategic forecasting and planning efforts of your team.

                                 

- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_year_incorporated.txt",
            expected_output=dedent(
                """
                

                Example Output:
                {
                    Year of incorporation: "Walmart was incorporated on October 31, 1969, as Wal-Mart Stores, Inc."
               }
                """
            )
        )
 
  
  def find_line_of_business(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to identify and analyze the lines of business for the company provided by the user. This task is essential for understanding the breadth of the company's operations, its market focus, and strategic direction.

Specific Instructions:

Research and Identification:

Conduct comprehensive research to identify the company's current lines of business. Utilize a variety of sources, including company websites, annual reports, industry analyses, and market research databases.
Pay special attention to the company's product and service offerings, market segments, and any publicly announced plans for future expansions or diversifications.
Analysis:

Analyze the identified lines of business to understand their role in the company's overall strategy and their contribution to the company's revenue and market position.

Strategic Overview:

Provide an overview of how the lines of business fit into the company's broader strategic objectives. This should include insights into any synergies between different lines of business, strategic partnerships, and the company's approach to innovation and market expansion.
Report Compilation:

Compile your findings into a detailed report that outlines the company's lines of business, your analysis of each, and their strategic implications. The report should be clear, concise, and structured to facilitate easy comprehension of the company's business landscape.
Highlight any areas of opportunity or risk identified during your analysis, providing a solid foundation for strategic planning and decision-making.
Deliverables:

A comprehensive report detailing the lines of business for the specified company, including an analysis of their strategic significance, competitive positioning, and potential for growth or expansion.
Objective:
Your primary objective is to provide a detailed and insightful overview of the company's lines of business, drawing on your exceptional analytical skills and deep market knowledge. Through this analysis, you will illuminate the company's operational domains and strategic endeavors, offering valuable insights that contribute to informed strategic planning and decision-making. Your work will not only delineate the current business landscape but also identify potential areas for future exploration and development, reinforcing your role as a critical asset in shaping the company's strategic direction.

                                     Helpful Tips:
                - To find the lines of business, perform searches on Google such like the following:
                    - "{company} lines of business"

                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_line_of_business.txt",
            expected_output=dedent(
                """
              

                Example Output:
                {
                    Walmart has a  broad range of business lines, but here are the primary ones:

- Retail Stores: This is the core of Walmart's business.

     - Walmart Supercenters: Large stores offering a vast selection of groceries, general merchandise, and often additional services like pharmacies and vision centers.

   - Walmart Discount Stores:  Smaller stores than Supercenters, focusing more on general merchandise than groceries.

   - Walmart Neighborhood Markets: Primarily focused on grocery items for quick and convenient shopping.

   -**Sam's Club:** Membership-based warehouse clubs offering bulk purchases at discounted prices. 

   - E-commerce:  Walmart.com and other online platforms allowing customers to shop from home. This includes:
    - Online shopping for pickup or delivery
    - Walmart+ membership program 

    - International Operations:  Walmart operates in numerous countries around the world under various names and store formats. 

Other Notable Business Lines

   - Walmart Logistics: The company's transportation and supply chain network.
   - Walmart Health: Offering pharmacy, vision, and basic health services.
   - Financial Services:  Money transfers, check cashing, and limited banking products.
   - Advertising: A growing business where brands can place ads on Walmart's websites and in stores.
               }
                """
            )
        )
 

  def find_brief_synopsis(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to craft a brief synopsis of the specified company, offering a narrative that captures its essence in a way that is both engaging and informative.

Specific Instructions:

Research:

Conduct thorough research to gather comprehensive information about the company, including its history, mission, core values, and key milestones. Utilize official company documents, credible news articles, industry reports, and interviews to ensure a rich and accurate representation of the company.
Narrative Development:

Develop a narrative that succinctly encapsulates the company's journey, highlighting its founding, evolution, mission, and the core values that drive its operations. Include significant milestones that showcase the company's achievements and challenges overcome.
Engagement and Clarity:

Ensure that the synopsis is engaging, employing storytelling techniques that draw the reader in while conveying the company's essence clearly and concisely. The narrative should be accessible to stakeholders with varying degrees of familiarity with the company.
Strategic Insight:

Embed insights into the company's strategic direction within the narrative, illuminating how its history, mission, and values inform its current and future endeavors. This aspect should provide stakeholders with a deeper understanding of the company's strategic positioning and aspirations.
Report Compilation:

Compile your narrative into a polished brief synopsis. The document should be well-organized and professionally presented, reflecting the high standards of your role as a Master Business Storyteller.
Deliverables:

A compelling brief synopsis of the company that integrates its history, mission, core values, and key milestones into a narrative designed to engage and inform stakeholders.
Objective:
Your primary objective is to deliver a narrative that not only recounts the company's factual history but also captures the essence of its identity and strategic direction. Through your exceptional narrative and research skills, you aim to provide stakeholders with a vivid understanding of the company, its foundational principles, and its trajectory, thereby enhancing their connection to and understanding of the company's mission and values. Your work as a Master Business Storyteller is not just about creating a document; it's about crafting a narrative that becomes a vital tool in communicating the company's essence and guiding its strategic messaging.
                                   
                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_brief_synopsis.txt",
            expected_output=dedent(
                """
                Example Output:
               
                {
                   brief synopsis: Walmart Inc. is a multinational retail giant known for its low-price strategy and vast selection of goods.  The company operates a variety of store formats, including Supercenters, Discount Stores, and Neighborhood Markets, alongside its membership-based Sam's Club warehouses. Walmart has aggressively expanded its e-commerce presence to compete in the online retail space. Its global reach and focus on cost-efficiency have made it one of the world's largest and most influential corporations.
               }
                """
            )
        )
   
  

  def find_banner_brands(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to identify and analyze the banner brands of the specified company. These brands are pivotal in representing the company's strategic market identity and its engagement with consumers.

Specific Instructions:

Research and Identification:

Conduct in-depth research to identify the company’s banner brands. Utilize a range of sources, including the company’s official website, industry reports, market analyses, and consumer feedback platforms.
Focus on brands that are strategically positioned by the company as key drivers of its market identity and consumer engagement.
Brand Analysis:

Analyze each identified banner brand to understand its market positioning, target audience, unique value proposition, and the role it plays in the company's overall brand strategy.
Evaluate how these brands contribute to the company’s market identity, considering factors such as consumer perception, brand loyalty, and competitive differentiation.
Strategic Contribution:

Assess the strategic contribution of each banner brand to the company’s market presence and consumer engagement. Identify how these brands embody the company’s core values, mission, and strategic objectives.
Highlight the stories these brands tell and their significance in reinforcing the company’s market positioning and brand identity.
Report Compilation:

Compile your findings into a comprehensive report that provides a detailed analysis of the company’s banner brands. The report should articulate the strategic significance of these brands in shaping the company’s market identity and consumer engagement.
Ensure the report is well-structured, clear, and insightful, serving as a valuable resource for understanding the strategic pillars of the company’s brand strategy.
Deliverables:

A detailed report on the banner brands of the specified company, including an evaluation of their market positioning, strategic contribution to the company’s identity, and their role in consumer engagement.
Objective:
Your primary objective is to deliver an insightful analysis that not only identifies the banner brands of the company but also elucidates their strategic importance in the broader context of the company’s market positioning and brand identity. Through your expert analysis, you aim to provide a comprehensive overview that highlights the strategic pillars of the company’s brand strategy, offering critical insights into its strengths and market opportunities. Your work will serve as an instrumental guide in understanding the essence and strategic trajectory of the company’s branding efforts.



                                  
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_banner_brands.txt",
            expected_output=dedent(
                """
               
               The list of banner brands for the specified company.

               """
            )
        )
  
  

    
  def find_target_market(self, agent, company: str):
   return Task(description=dedent(f"""
Your mission is to delineate the target market of the specified company, providing a comprehensive understanding of its demographic, psychographic, and behavioral characteristics.

Specific Instructions:

Data Collection:

Gather data relevant to the company's market positioning, including industry reports, consumer surveys, social media analytics, and competitor analysis. Focus on information that sheds light on consumer preferences, behaviors, and trends within the company's industry.
Market Segmentation:

Conduct market segmentation analysis to identify distinct groups within the broader market that the company targets or could potentially target. Analyze demographic data (e.g., age, gender, income), psychographic data (e.g., interests, values, lifestyles), and behavioral data (e.g., purchasing habits, brand interactions).
Target Market Definition:

Synthesize your findings to define the target market(s) of the company. Provide detailed descriptions of the demographic, psychographic, and behavioral characteristics that distinguish the company's target customers.
Highlight the needs, preferences, and pain points of these target segments, explaining why the company targets these specific groups and how its product offerings align with their expectations.
Strategic Implications:

Discuss the strategic implications of your target market analysis for the company. Suggest how the insights gained can inform product development, marketing strategies, and customer engagement initiatives.
Offer recommendations on how the company can better align its offerings with the needs and expectations of its target market, potentially identifying untapped opportunities for growth and engagement.
Report Compilation:

Compile your analysis into a comprehensive report that clearly identifies and describes the company's target market. The report should be structured to provide a clear overview of your research, analysis, and strategic recommendations.
Ensure the report is accessible, engaging, and actionable, providing the company with a valuable tool for strategic planning and decision-making.
Deliverables:

A detailed report outlining the target market of the specified company, including demographic, psychographic, and behavioral characteristics, along with strategic recommendations informed by your analysis.
Objective:
Your primary objective is to equip the company with an in-depth understanding of its target market, leveraging your advanced analytical skills and market insights. Through your meticulous research and strategic analysis, you aim to provide actionable insights that can guide the company's strategic decision-making, enhancing its market positioning and customer engagement strategies. Your work will serve as a critical component of the company's strategic planning, offering a comprehensive lens through which to view its current and potential customer base.


                                   Helpful Tips:
                - To find the target market, perform searches on Google such like the following:
                    - "{company} target market"

                                  Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_target_market.txt",
            expected_output=dedent(
                """
              

                Example Output:
                {
                   Here's a bit more detail on some of the demographics:

                    * Age: Walmart appeals to a wide age range, although families with children and older adults tend to be frequent shoppers. 
                    * Gender:  While they cater to both genders, women tend to be the primary shoppers for households.
                    * Education:  Walmart doesn't specifically target a particular education level.
               }
                """
            )
        )
  

  def find_revenue(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to determine the annual revenue for the years 2023 and 2022 for the company specified by the user. This information is vital for assessing the company's financial health and operational success.

Specific Instructions:

Data Collection:

Gather financial reports, earnings releases, and relevant market insights for the years 2023 and 2022. Utilize official corporate filings, including 10-K and 10-Q reports from EDGAR (for U.S.-based companies) or equivalent databases for companies based in other jurisdictions.
Ensure access to credible financial databases and analytical tools for accurate data retrieval and analysis.
Financial Analysis:

Analyze the collected financial documents to extract the annual revenue figures for 2023 and 2022. Pay close attention to revenue breakdowns, if available, to provide a more detailed view of income sources and growth drivers.
Employ analytical techniques to adjust for any accounting changes, one-time events, or other factors that might influence a straightforward year-over-year comparison.
Trend Identification:


Report Compilation:

Compile your findings into a comprehensive report detailing the annual revenues for 2023 and 2022.

Deliverables:

A detailed report on the annual revenue for 2023 and 2022.
Objective:
Your primary objective is to provide a clear, accurate determination of the annual revenues for 2023 and 2022, leveraging your financial analytical expertise to offer critical insights into the company's fiscal performance. Through rigorous analysis and strategic interpretation of financial data, your work will serve as a foundational element for assessing the company's growth, identifying opportunities and challenges, and informing strategic decisions by stakeholders. Your role as the Chief Financial Data Analyst is pivotal in ensuring stakeholders have a transparent and nuanced understanding of the company's economic standing, guiding them through complex financial landscapes with precision and insight.


                                    Helpful Tips:
                - To find the revenue, perform searches on Google such like the following:
                    - "{company} 2022 / 2023 revenue"

                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_revenue.txt",
            expected_output=dedent(
                """
               
                Example Output:
                {
                    Reveue: revenue of 2022 and 2023:

                    2022 Revenue: $572.75 billion
                    2023 Revenue: $611.29 billion
               }
                """
            )
        )
  

  def find_financial_performance_2023(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to analyze and summarize the financial performance of the specified company for the year 2023, crafting a headline summary and providing hyperlinks to the original sources of information.

Specific Instructions:

Research and Data Collection:

Utilize digital research techniques to gather data on the company's financial performance for the year 2023. This should include, but not be limited to, annual reports, quarterly earnings reports, and other relevant financial disclosures.
Ensure the use of reputable sources, prioritizing information directly from the company's official website, financial news platforms, and regulatory bodies' databases.
Financial Analysis:

Analyze key financial metrics such as revenue, profit margins, earnings per share (EPS), and other relevant indicators of financial health and performance.
Assess the company's financial outcomes in the context of its industry, market conditions, and its own historical performance.
Headline Summary Creation:

Craft a concise, compelling headline summary that encapsulates the essence of the company's financial performance in 2023. This summary should be accessible to a broad audience, including those without a deep background in finance.
Highlight significant financial achievements or concerns, ensuring the summary is balanced and informative.
Source Citation and Hyperlinking:

Provide a hyperlink to the original source(s) of financial information. This link should direct stakeholders to the authoritative document or webpage where the financial data was obtained, ensuring verifiability and transparency.
Ensure all hyperlinks are active and direct users to reputable, official content.
Report Compilation:

Compile your analysis and headline summary into a clear, professional document. The report should not only present the financial performance succinctly but also guide readers to explore the original sources via provided hyperlinks.
Format the document for ease of reading, with a clean layout and logical organization.
Deliverables:

A comprehensive report that includes a headline summary of the company's financial performance for 2023, alongside hyperlinks to the original sources of financial data.
Objective:
Your primary objective is to distill the 2023 financial performance of the specified company into an accessible, accurate summary, supplemented by direct links to the source material. Through this task, you aim to bridge the gap between complex financial data and stakeholder comprehension, ensuring the information is not only insightful but also verifiable. Your role as the Director of Financial Communications is crucial in promoting transparency, credibility, and informed decision-making among stakeholders by making pivotal financial information readily accessible and understandable.

                                    Helpful Tips:
                - To find the financial performance 2023, perform searches on Google such like the following:
                    - "{company} 2023 financial performance"

                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_financial_performance_2023.txt",
            expected_output=dedent(
                """
             

                Example Output:
                {
                   Financial Performance: Walmart Posts Record $611 Billion Revenue in 2023, Net Income Surges 12%
                  Walmart Delivers Strong 2023: Revenue Up 7%, Operating Income Climbs 9%, and Share Buybacks Exceed $10 Billion
                  Walmart's 2023 Success Story: E-commerce Sales Up 15%, Gross Profit Margin Expands, and Inventory Levels Improve
                  Source: https://corporate.walmart.com/content/dam/corporate/documents/esgreport/reporting-data/tcfd/walmart-inc-2023-annual-report.pdf
               }
                """
            )
        )
 

  def find_market_capitalization(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to ascertain the market capitalization of the company specified by the user, provided that the company is publicly traded.

Specific Instructions:

Verification of Public Status:

Initially, confirm that the company in question is publicly traded. This can involve checking major stock exchanges and financial databases to ensure the company's shares are listed and actively traded.
Data Collection:

Gather the most recent stock price data for the company from reputable financial news websites, stock market databases, or directly from the stock exchange where the company's shares are listed.
Retrieve the total number of outstanding shares for the company, which is often available in the company’s latest financial reports or through financial market databases.
Market Capitalization Calculation:

Calculate the market capitalization by multiplying the current stock price by the total number of outstanding shares. This computation will yield the company's current market valuation.
Analysis and Reporting:

Provide the calculated market capitalization figure.
Deliverables:

The exact market capitalization of the company.
Objective:
Your primary objective is to leverage your expert knowledge in equity markets and valuation techniques to deliver an accurate and insightful assessment of the company's market capitalization. Through this task, you aim to illuminate the company's financial standing within the broader market, providing investors and stakeholders with a key metric that encapsulates its size, potential for growth, and competitive positioning. Your role as the Head of Equity Research is crucial in equipping stakeholders with the information needed to make informed decisions, thereby enhancing their understanding of the company's value in the financial markets.
                                   

                                    Helpful Tips:
                - To find the number of outstanding shares, perform searches on Google such like the following:
                    - "{company} number of outstanding shares"
                    - To find the stock price, perform searches on Google such like the following:
                    - "{company} stock price"

                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_market_capitalization.txt",
            expected_output=dedent(
                """
              
                Example Output:
                {
                 market capitalization: As of February 2024, Walmart's market capitalization is approximately $472.24 billion, making it the 17th most valuable company by market cap globally
               }
                """
            )
        )
   

  def find_company_owner(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to identify the owner of the company specified by the user, distinguishing between public and private entities to provide the appropriate information based on the company's status.

Specific Instructions:

Preliminary Verification:

Ascertain whether the specified company is publicly traded or privately held. This may involve consulting financial databases, stock exchange listings, and regulatory filings.
For Public Companies:

If the company is public, locate the stock ticker symbol. Utilize financial news platforms, stock market databases, and the company's investor relations page to find this information.
Briefly describe the company's major shareholders, if applicable, including institutional investors and significant equity holders, using the latest available public disclosures and shareholder reports.
For Private Companies:

If the company is private, investigate to outline the ownership structure. This may require analyzing business registries, legal filings, and, when available, company-released information to identify key individuals or entities that hold ownership stakes.
Provide insights into the ownership hierarchy, noting any notable investors, parent companies, or ownership groups.
Ownership Analysis:

Offer an analysis of the identified ownership structure, discussing its implications for corporate governance, strategic decision-making, and investor relations.
Highlight any interesting findings about the ownership, such as family ownership, cross-holdings, or conglomerate structures, and their potential impact on the company's operations and governance.
Report Compilation:

Compile your findings into a detailed report that clearly states the ownership status of the company, the stock ticker (for public companies), or the ownership structure (for private companies). Ensure the report is well-organized, concise, and provides actionable insights into the company's governance and strategic direction.
Include any relevant hyperlinks or references to public disclosures, regulatory filings, or official documents that support your analysis.
Deliverables:

A comprehensive report detailing the ownership of the specified company, including the stock ticker for public companies or a description of the ownership structure for private companies, accompanied by an analysis of its implications for corporate governance and strategy.
Objective:
Your primary objective is to deliver a clear and insightful analysis of the company's ownership, utilizing your expertise in corporate governance and structures. By distinguishing between public and private entities and providing detailed information on ownership or stock tickers, your work will significantly contribute to understanding the company's governance framework and strategic direction. Your role as a Corporate Governance Expert is pivotal in illuminating the mechanisms of control and influence within the company, offering stakeholders a deeper grasp of its operational and governance dynamics.


        - To find the company owner, perform searches on Google such like the following:
                    - "{company} ownership structure"                        
                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_company_owner.txt",
            expected_output=dedent(
                """
            

                Example Output:
                {
                    owners: "
                    Walmart Inc. is a publicly traded company, meaning its ownership is distributed among the public shareholders who own its stock. The Walton family, founders of Walmart, remains the largest shareholder group, controlling a significant portion of the company through their holding company, Walton Enterprises, and individual family members' holdings. The ticker symbol for Walmart on the New York Stock Exchange (NYSE) is "WMT." "
               }
                """
            )
        )
   

  def find_founding_story(self, agent, company: str):
    return Task(description=dedent(f"""
Your mission is to uncover and succinctly summarize the founding story of the company specified by the user, distilling its essence into a single, compelling paragraph.

Specific Instructions:

Research:

Engage in thorough research to gather information about the company's origins. Utilize a variety of sources, including the company's own historical archives, interviews with founders or early employees, business history publications, and credible online resources.
Storytelling:

Craft a narrative that encapsulates the company's founding story. Focus on the vision that sparked its creation, the challenges faced in its early days, and the pivotal decisions that set it on its path to success. Aim to convey the essence of the company's beginnings in a manner that is both informative and inspiring.
Concision and Clarity:

Ensure the narrative is concise, limiting the summary to one paragraph. Despite the brevity, strive for clarity and vividness in your storytelling, capturing the spirit of the company's origins and the ambition of its founders.
Engagement:

Use engaging language and a narrative style that draws the reader in, making the founding story not just a recounting of facts but a story that resonates with and inspires the audience.
Finalization:

Review the paragraph for accuracy, coherence, and narrative flow. Ensure that it stands as a testament to your expertise as a Master Business Historian, effectively communicating the company's founding story in a manner that is both captivating and succinct.
Deliverables:

A one-paragraph narrative that vividly and concisely summarizes the founding story of the specified company, showcasing your skill in historical research and storytelling.
Objective:
Your primary objective is to illuminate the origins of the specified company through a narrative that is as informative as it is inspiring. By drawing on your extensive historical research and storytelling prowess, you aim to provide a narrative that not only encapsulates the company's visionary beginnings but also engages and resonates with the audience, offering a glimpse into the passion and perseverance that underpin its establishment. Your work as a Master Business Historian is crucial in bridging the past with the present, offering insights into the foundational moments that have shaped the company's identity and strategic direction.


         - To find the founding story, perform searches on Google such like the following:
                    - "{company} founding story"                                  
                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_founding_story.txt",
            expected_output=dedent(
                """
           

                Example Output:
                {
                    Founding story: 
                    Walmart was founded by Sam Walton in 1962, with the opening of the first Walmart store in Rogers, Arkansas. Walton's vision was to offer consumers lower prices and better service by keeping costs low and passing the savings on to customers. This principle of value for money and a focus on customer satisfaction became the cornerstone of Walmart's business model. The company's success led to rapid expansion, and it has grown to become the largest retail chain in the world, maintaining its commitment to low prices, wide product selection, and community involvement.
               }
                """
            )
        )
  
    
  def find_key_points_of_difference(self, agent, company: str):
   return Task(description=dedent(f"""
Your mission is to determine the 3 key points of difference for the company specified by the user, spotlighting its unique positioning and competitive edge in the market.

Specific Instructions:

Market Analysis:

Conduct a thorough market analysis to understand the competitive landscape in which the company operates. This includes reviewing industry reports, competitor offerings, and market trends that influence consumer preferences and behavior.
Company Offering Review:

Examine the company's products or services in detail. Focus on aspects such as design, technology, customer service, brand perception, and pricing strategy. Identify features or attributes that are distinct compared to competitors.
Value Proposition Identification:

Identify and articulate the company's unique value propositions. Determine how these offerings solve specific customer problems or meet particular customer needs in ways that competitors do not.
Competitive Advantage Analysis:

Analyze the company's competitive advantages. This might involve assessing its operational efficiencies, technological innovations, supply chain management, or customer engagement strategies that contribute to its unique market position.
Synthesis and Articulation:

Synthesize your findings to pinpoint the 3 key points of difference for the company. Articulate these points clearly, emphasizing how they contribute to the company's unique positioning and competitive edge in the market.
Report Compilation:

Compile your analysis into a concise report that outlines the 3 key points of difference for the company. The report should provide a clear rationale for each point, supported by data and insights derived from your analysis.
Ensure the report is structured in a way that is accessible and engaging for stakeholders, highlighting the strategic implications of these differentiators.
Deliverables:

A comprehensive report detailing the 3 key points of difference for the specified company, including a clear articulation of its unique value propositions and competitive advantages in the marketplace.
Objective:
Your primary objective is to illuminate the unique factors that set the specified company apart from its competitors, using your analytical prowess to identify and articulate its key points of difference. Through this analysis, you aim to provide actionable insights that can further refine the company's strategic positioning and narrative, ensuring it effectively communicates its unique strengths to the target audience. Your role as a Strategic Differentiation Analyst is instrumental in guiding the company to leverage its distinct advantages, fostering sustained competitive success in its industry.      


  - To find the key points of difference, perform searches on Google such like the following:
                    - "{company} key points of difference"                        

                                  Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_key_points_of_difference.txt",
            expected_output=dedent(
                """
             

                Example Output:
                {
                   3 key point of difference walmart: Walmart distinguishes itself in the retail industry through several key points of difference:

                  Everyday Low Prices (EDLP) Strategy: Walmart's business model is built around offering customers low prices on a wide variety of goods every day, without the need for special promotions or sales. 
                  Vast Product Selection and Convenience: Walmart offers an extensive range of products, including groceries, apparel, electronics, and home goods, making it a one-stop shop for consumers. 
                  Global Supply Chain and Distribution Efficiency: Walmart's sophisticated supply chain and distribution network are unmatched in the retail industry.
               }
                """
            )
        )
    

  def find_top_5_strategic_initiatives(self, agent, company:str):
    return Task(description=dedent(f"""
Your mission is to unearth the top 5 strategic initiatives of the company specified by the user, utilizing public statements and financial filings, and to provide hyperlinks to these original sources for validation.

Specific Instructions:

Digital Research and Data Collection:

Conduct comprehensive digital research to collect information on the company's strategic initiatives. Focus on public statements, press releases, and, for public companies, 10-K and 10-Q filings available through the SEC's EDGAR system or equivalent regulatory bodies outside the U.S.
Analysis of Strategic Initiatives:

Analyze the gathered data to identify strategic initiatives, focusing on those highlighted as priorities by the company's leadership. Look for recurring themes or projects emphasized in multiple sources, including earnings calls, investor presentations, and annual reports.
Prioritization and Selection:

Determine the top 5 strategic initiatives based on their significance, potential impact on the company's future, and alignment with the company's long-term strategic goals. Consider the resources allocated to each initiative and any expected outcomes or benchmarks for success.
Verification and Sourcing:


Compilation and Reporting:

Compile your findings into a concise report that clearly outlines the top 5 strategic initiatives, including a brief description of each and its strategic importance.
Strategic Implications:

Offer a brief analysis of the strategic implications of these initiatives, discussing how they align with the company's broader strategic vision and potential impact on the company's positioning in its industry.
Deliverables:

A detailed report on the top 5 strategic initiatives of the specified company, complete with descriptions and strategic importance
Objective:
Your primary objective is to provide stakeholders with a well-researched and articulated report on the top 5 strategic initiatives of the specified company. Through this report, you aim to offer a clear view of the company's strategic direction, enabling stakeholders to understand the initiatives' significance and potential impact on the company's future. Your role as the Chief Strategy Insights Officer is crucial in navigating the intersection of corporate strategy and data analysis, providing stakeholders with actionable insights that inform understanding and strategic decision-making.

      - To find the top 5 strategic initiatives, perform searches on Google such like the following:
                    - "{company} top 5 strategic initiatives"                          
                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_top_5_strategic_initiatives.txt",
            expected_output=dedent(
                """
           

                Example Output:
                {
                    Walmart top 5 strategic innitiatives: Supply Chain Innovation and Automation: Walmart is investing in a next-generation supply chain network that includes stores, clubs, and fulfillment centers to improve customer and associate experiences while increasing productivity. This involves reengineering the supply chain with more intelligent and connected omnichannel networks enabled by data, software, and automation. By the end of Fiscal Year 2026, Walmart aims for about 65% of its stores to be serviced by automation, improving inventory accuracy, in-stock levels, and delivery services​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)

                    Omnichannel Retail and Tech-Powered Services: Walmart emphasizes its role as a people-led, tech-powered omnichannel retailer, focusing on providing opportunities for associates and enhancing customer service. The strategy includes creating a more connected and automated supply chain, improving operating margin through productivity advancements, and driving returns through operating margin expansion and capital prioritization. This approach aims to serve customers however they wish to shop, fueling continued growth​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)

                    Engagement and Brand Equity: Walmart is actively working to engage customers and build brand equity, particularly among younger consumers, through innovative marketing strategies. This includes leveraging platforms like TikTok to present Walmart in a new light, fostering customer engagement and loyalty through initiatives like Walmart Creator for content sharing, and embedding commerce features into marketing campaigns to make the brand more relatable and integrated into pop culture. Examples include a Walmart-produced holiday rom-com and a Black Friday ad series featuring the cast from the 2004 teen film "Mean Girls"​​. (https://www.mytotalretail.com/article/walmarts-cmo-outlines-3-key-2024-initiatives/)                                                              Diversification of Earnings Streams: Walmart is diversifying its earnings through an improved category and business mix and scaling proven, high-return investments that drive operating leverage. This strategic move involves focusing on high-value initiatives such as advertising, data, memberships, and marketplace services. These efforts are expected to contribute to mid-single-digit sales growth targets and enhance operating income growth, positioning Walmart for steady and sustained growth at higher margins over the next 3-5 years​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)

                    Customer-Facing Technology Investments: Walmart plans to maintain or slightly increase capital expenditures with a focus on technology, supply chain, and customer-facing initiatives. This strategic direction underscores Walmart's commitment to enhancing the shopping experience through digital innovation, including improvements to its online platforms and in-store technology. By investing in technology that enhances the customer experience, Walmart aims to further integrate its physical and digital retail offerings, ensuring a seamless omnichannel shopping experience for its customers​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)
               }
                """
            )
        )
  

  def find_worries_risks_concerns(self, agent, company: str):
   return Task(description=dedent(f"""
Your mission is to unearth the worries, risks, and concerns facing the specified company, drawing from its public statements and financial filings, and to furnish hyperlinks to these original sources for validation.

Specific Instructions:

Data Collection:

Gather data from the company's latest 10-K and 10-Q filings, press releases, and other relevant public disclosures. Focus on sections that typically contain risk factors, management's discussion and analysis (MD&A), and any notes that detail potential threats or concerns.
Risk Identification:

Identify and categorize the key risks disclosed by the company. This includes operational risks, financial risks, market-related risks, regulatory risks, and any emerging threats that could impact the company's future performance.
Analysis and Articulation:

Analyze the identified risks to understand their potential impact on the company's operations, strategies, and financial health. Articulate these risks clearly, explaining their significance and the underlying factors contributing to their emergence.
Hyperlink Incorporation:

For each identified risk, provide hyperlinks to the original sources where these risks were disclosed. Ensure these links are accurate, functional, and direct stakeholders to the official documents or statements for further review.
Report Compilation:

Compile your findings into a comprehensive report that outlines the worries, risks, and concerns of the company, supported by hyperlinks to the original sources. The report should be structured to facilitate easy navigation, with risks categorized and detailed insightfully.
Strategic Insights:

Offer strategic insights based on your risk assessment, suggesting potential risk mitigation strategies or considerations for stakeholders. Highlight any patterns or thematic concerns that emerge from the analysis, providing a forward-looking perspective on risk management.
Deliverables:

A detailed report highlighting the worries, risks, and concerns of the specified company, categorized and articulated with precision, and supported by hyperlinks to the original sources of information.
Objective:
Your primary objective is to provide stakeholders with a nuanced understanding of the specified company's risk landscape, leveraging your expert analytical capabilities to highlight critical threats and concerns. Through a meticulous examination of public disclosures and financial filings, complemented by direct links to source materials, your work aims to inform strategic decision-making, enhancing the company's preparedness and resilience against potential risks. Your role as the Chief Risk Intelligence Analyst is crucial in equipping stakeholders with the insights needed to navigate the complexities of corporate risk, ensuring informed, strategic responses to the challenges ahead.


     - To find the worries risks and concerns, perform searches on Google such like the following:
                    - "{company} risks, worries and concerns"                     
                                  Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_worries_risks_concerns.txt",
            expected_output=dedent(
                """
           

                Example Output:
                {
                    Worries, risks and concerns: Walmart's worries stem from managing the complex dynamics of global operations amid fluctuating economic conditions and consumer behaviors. The company is concerned with navigating the risks associated with currency fluctuations and interest rate changes, given its significant international presence​​. (https://www.sec.gov/Archives/edgar/data/104169/000010416922000012/wmt-20220131.htm)

                    Risks for Walmart include the volatility in currency exchange rates and the potential impact on financial performance due to its extensive international operations. Additionally, the company faces investment risks related to changes in stock prices of equity investments, which could significantly affect its financial position​​. (https://www.sec.gov/Archives/edgar/data/104169/000010416922000012/wmt-20220131.htm)

                    Concerns for Walmart also revolve around the evolving retail landscape, with a strong emphasis on enhancing its eCommerce capabilities and managing the competitive pressures from both online and traditional retailers. There is also an underlying concern about the ability to sustain growth and market share gains in the face of increasing operational costs and regulatory challenges​​​​ (https://last10k.com/sec-filings/wmt/0000104169-22-000012.htm)
               }
                """
            )
        )
  

  def find_main_competitors(self, agent, company: str):
    return Task(
            description=dedent(f"""
Your mission is to identify at least five main competitors of the specified company, enriching the strategic planning process with a nuanced understanding of the competitive landscape.

Specific Instructions:

Market Research:

Conduct comprehensive market research to identify the company's main competitors. Utilize a variety of sources including industry reports, financial statements, market surveys, and digital analytics to ensure a broad and informed perspective.
Competitor Analysis:

Analyze the identified competitors, focusing on their market share, product offerings, customer base, and recent strategic moves. Pay close attention to any competitive advantages or weaknesses that could impact their market position relative to the specified company.
Strategic Positioning:

Evaluate the strategic positioning of each competitor within the industry. Consider factors such as brand strength, technological innovation, distribution networks, and customer loyalty.
Insights and Implications:

Derive insights from the competitor analysis that are pertinent to the specified company's strategic planning. Highlight potential threats and opportunities, suggesting areas where the company can leverage its strengths or address vulnerabilities.
Report Compilation:

Compile your findings into a comprehensive report that details the competitive landscape. The report should include profiles of at least five main competitors, summarizing their key attributes, market positioning, and strategic focus.
Ensure the report is structured in a manner that is both informative and accessible, facilitating strategic decision-making processes.
Recommendations:

Based on your analysis, offer strategic recommendations for the specified company. Suggest how it can differentiate itself from competitors or capitalize on market opportunities.
Deliverables:

A detailed report identifying at least five main competitors of the specified company, including an analysis of their strengths, weaknesses, and strategic focus, accompanied by strategic recommendations for navigating the competitive landscape.
Objective:
Your primary objective is to furnish the specified company with a profound understanding of its competitive environment, identifying key competitors and dissecting their strategic dispositions. Through meticulous market research and competitive analysis, your work aims to illuminate the competitive dynamics at play, offering actionable insights that can significantly enhance the company's strategic planning efforts. Your role as the Lead Competitive Intelligence Analyst is pivotal in equipping the company with the knowledge and strategic foresight required to thrive in a competitive market landscape.
                               
                        Helpful Tips:
                - To find the main competitors, perform searches on Google such like the following:
                    - "{company} main competitors"
                               
                               Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/find_main_competitors.txt",
            expected_output=dedent(
                """
        

                Example Output:
                {
                  Walmart's top 5 competitors: 
                  Kroger.
                  Costco.
                  Target. 
                  Kauftland.
                  Lidl.
               }
                """
            )
        )
   
  
  def create_swot_analysis(self, agent, company: str):
    return Task(description=dedent(f"""
 Your mission is to perform a SWOT analysis for the specified company, drawing on information provided by other agents or your independent research. The analysis should be concise and informative, with each section—Strengths, Weaknesses, Opportunities, Threats—encapsulated in a paragraph.

Specific Instructions:


Strengths Analysis:

Identify and articulate the company's core strengths. These might include unique resources, competitive advantages, strong market positions, innovative capabilities, or effective leadership. Summarize these strengths in a paragraph, highlighting how they contribute to the company's success.
Weaknesses Analysis:

Determine the company's internal weaknesses or areas for improvement. Consider factors such as resource limitations, gaps in capabilities, market challenges, or operational inefficiencies. Provide a paragraph summarizing these weaknesses, emphasizing their impact on the company's performance.
Opportunities Analysis:

Analyze the external opportunities available to the company. This could involve emerging markets, technological advancements, shifts in consumer preferences, or regulatory changes. Craft a paragraph detailing these opportunities, underlining how the company can capitalize on them.
Threats Analysis:

Identify external threats that could pose challenges to the company. Look for competitive pressures, market volatility, technological disruptions, or adverse regulatory developments. Summarize these threats in a paragraph, discussing their potential to affect the company's future.
SWOT Synthesis:

Synthesize the findings into a coherent SWOT analysis. Ensure that each section is clear, concise, and provides strategic insights into the company's position and potential strategies for growth, improvement, and risk mitigation.
Report Compilation:

Compile the SWOT analysis into a structured report. The report should be formatted professionally, making it accessible and valuable for strategic decision-making.
Deliverables:

A SWOT analysis report for the specified company, containing insightful paragraphs for each section—Strengths, Weaknesses, Opportunities, Threats—that together offer a comprehensive view of the company's strategic landscape.
Objective:
Your primary objective is to deliver a SWOT analysis that not only identifies the key strategic elements of the company's internal and external environment but also provides actionable insights for future planning. Through this analysis, you aim to furnish the foundation for developing effective growth strategies and risk management plans, reinforcing your role as a pivotal figure in strategic planning and decision-making processes.          

                                    Helpful Tips:
                - To find the strength, perform searches on Google such like the following:
                    - "{company} strenghts" 
                    - To find the weaknesses, perform searches on Google such like the following:
                    - "{company} weaknesses" 
                    - To find the opportunities, perform searches on Google such like the following:
                    - "{company} opportunities"
                    - To find the threats, perform searches on Google such like the following:
                    - "{company} threats"       
                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
- Company Name: {company}
                Note: {self.__tip_section()}

                """
            ),
            agent=agent,
            max_iterations=30,
            allow_delegation=False,
            output_file="output/create_swot_analysis.txt",
            expected_output=dedent(
                """
          

                Example Output:
                {
                    Strengths
                    Global Scale and Market Presence: Walmart operates more than 10,500 stores in 20 countries, showcasing its vast global footprint and market dominance. This extensive network allows Walmart to reach a broad customer base and leverage economies of scale​​​​​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)

                    Weaknesses
                    Public Image and Labor Relations: Walmart has faced criticism related to its labor practices, including wages, working conditions, and unionization efforts, which could impact its public image and employee satisfaction​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)

                    Opportunities
                    E-commerce and Digital Expansion: Investing in online platforms and omnichannel retailing offers Walmart the opportunity to capture a larger share of the growing e-commerce market and compete more effectively with online retailers like Amazon and Alibaba​​​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)

                    Threats
                    Intense Competition: Walmart faces stiff competition from both brick-and-mortar and online retailers, including Amazon, Costco, and Target, which continually challenge its market share​​​​. (https://litcommerce.com/blog/walmart-competitors/)
               }
                """
            )
        )

  def analyse_visual_market(self, agent, company):
        return Task(description=dedent(f"""
              Objective: Gather 10 recent photographs of {company}'s stores from the years 2023-2024 to provide a visual overview of the brand's physical retail presence.
              1. Research and Image Collection
              • Digital Scouting: Utilize online resources such as the company’s official website, social media platforms (Instagram, Facebook, LinkedIn), Google Maps images, and reputable retail design publications to find high-quality images of the company's stores. Focus on content published within the 2023-2024 timeframe.
              • Image Selection Criteria: Choose images that clearly depict the latest design concepts and branding elements.
              2. Image Verification
              • Confirm Authenticity: Ensure the images are genuine representations of {company}’s stores. Cross-reference with multiple sources when possible to verify the store location and the design's recency.
              • Date Verification: Verify the images correspond to the 2023-2024 period. Look for date stamps, related news articles, or social media posts that can confirm the timeframe.
              Expected Deliverables:
              • 10 carefully selected photographs with URLs for reference, as direct printing of images from 2023-2024 is not possible.
              
              As the Lead Visual Market Analyst, your role is pivotal in capturing the essence of {company}'s latest retail design innovations. This task supports the strategic visualization of the brand's retail environment, serving as a foundation for future design and marketing strategies.
                                       
            This task is independent and requires utilizing the internet to find the most recent store design images for {company}. Leverage any web resources, news platforms, and official company announcements to gather the latest data. Your findings will be a valuable asset for understanding the current market and setting directions for future developments.


                                    Helpful Tips:
            - To find the 10 recent retail design pictures, perform searches on Google such like the following:
                    - "{company} recent store design images" 
            Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
                                       
            - Company Name: {company}
             Note: Focus on thoroughness and quality in your search to ensure the visuals accurately represent the brand's current design ethos and market positioning.
                    """
                ),
                agent=agent,
                max_iterations=30,
                allow_delegation=False,
                output_file="output/analyse_visual_market.txt",
                expected_output=dedent(
                    """
               
                   {
                    "images": [
                        "URL1", "URL2", "URL3", "URL4", "URL5",
                        "URL6", "URL7", "URL8", "URL9", "URL10"
                    ]
                   }
                    """
                )
            )


  def find_store_designer_agency(self, agent, company: str):
    return Task(description=dedent(f"""
        Retail Design Agency Identification:

        Conduct additional web searches to identify the retail design agency responsible for the company’s most recent store designs. This involves scrutinizing press releases, news articles, and official announcements that mention collaborations or partnerships with design agencies.
        Provide a brief overview of the identified agency, including its name, a brief background, and any relevant links to its official website or portfolio showcasing its work with the specified company.
        Deliverables:
        Identification of the retail design agency: A concise summary about the agency responsible for the latest store designs, including its name, background, and a hyperlink to its professional portfolio or website.
        Objective:
        Your primary goal is to offer stakeholders a  rich and verifiable insight into the agency that was responsible for the company's latest store design. Your role is pivotal in the possible future collaboration with the agency and the company.
                                    Helpful Tips:
         - To find the store design agency, perform searches on Google such like the following:
                    - "{company} recent store design agency"                    
                                   Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.

        - Company Name: {company}
                        Note: {self.__tip_section()}

                        """
                    ),
                    agent=agent,
                    max_iterations=30,
                    allow_delegation=False,
                    output_file="output/find_store_designer_agency.txt",
                    expected_output=dedent(
                        """
                      

                        Example Output:
                        {
                        
                        Walmart design agency is: 

                        Lippincott:  A well-known branding and design agency that notably redesigned Walmart's in-store signage, graphics, and overall retail environment.
                    }
                        """
                    )
                )
        
  
  def search_news(self, agent, company: str):
    return Task(
        description=dedent(f"""
            Task Execution Blueprint:

            - **Elite Research and Discovery:**
              - Focus on the use of high-efficiency search algorithms and targeted deep-web searches to quickly locate the 5 most recent and impactful pieces of company news.
              - Prioritize news for its strategic relevance and potential to influence company direction.

            - **Analytical Deep Dive:**
              - Apply streamlined analysis techniques to assess the strategic implications of each news item, emphasizing speed and accuracy.
              - Utilize quick predictive insights to gauge the immediate effects on the company's position and operations.

            - **Strategic Synthesis and Reporting:**
              - Produce a concise strategic report that synthesizes findings into actionable insights, prioritizing rapid delivery to inform decision-making processes.

            - **Executive Engagement and Influence:**
              - Prepare a succinct executive briefing that highlights key findings and recommendations, designed for immediate strategic impact.

            **Expected Deliverables**
            A strategic intelligence report, including 5 recent pieces of relevant company news, with URLs to the references. Each piece of news should be quickly analyzed for strategic implications, synthesized into actionable insights, and presented in a format that facilitates swift executive decision-making.
                           
                           This task emphasizes speed and clarity in gathering the most up-to-date executive moves, requiring no further analysis or strategic recommendations.
                           
                           If you are unable to find 5 company news, please provide as many as you can locate within the specified timeframe.

                           Always provide hyperlinks to the original sources for validation.
            
                           
                             Helpful Tips:
         - To find the most recent company news, perform searches on Google such like the following:
                    - "{company} most recent company news"  
            Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.


        - Company Name: {company}
         Note: {self.__tip_section()}
                           
                            """),
        agent=agent,
        max_iterations=30,  
        allow_delegation=False,
        output_file="output/search_news.txt",
        expected_output=dedent(
          """
        

                Example Output:
                {
                 COMPANY NEWS: 
                  Walmart Q4 and FY24 Earnings: Walmart reported significant growth in its fourth quarter and full fiscal year 2024 earnings, highlighting a total revenue of $173.4 billion in Q4, marking a 5.7% increase from the previous year. The company surpassed $100 billion in eCommerce sales and emphasized its commitment to improving customer experience and reducing prices​​. (https://corporate.walmart.com/news/2024/02/20/walmart-releases-q4-and-fy24-earnings)

                  Growth Strategy and Supply Chain Innovation: At the 2023 Investment Community Meeting, Walmart outlined its growth strategy, focusing on leveraging its omnichannel business model and integrating automation across its operations. By the end of Fiscal Year 2026, approximately 65% of Walmart stores are expected to be serviced by automation, aiming to enhance efficiency and customer service​​. (https://corporate.walmart.com/news/2023/04/04/walmart-outlines-growth-strategy-unveils-next-generation-supply-chain-at-2023-investment-community-meeting)

                  Global Tech Expansion: Walmart announced plans to accelerate the expansion of its Global Tech division by hiring more than 5,000 associates globally within the fiscal year. This expansion includes adding new hubs in Toronto and Atlanta, highlighting the company's focus on becoming a tech-powered, people-led retailer​​. (https://corporate.walmart.com/news/2022/03/15/walmart-global-tech-accelerates-expansion-with-plans-to-hire-thousands-of-technologists-and-add-new-locations)

                  $9 Billion Investment in Store Upgrades: Walmart is investing more than $9 billion over two years to modernize 1,400 stores across the U.S. This investment aims to improve store layouts, product selections, and incorporate new technologies, enhancing the shopping experience and adapting stores to better meet consumer needs​​. (https://www.reuters.com/business/retail-consumer/walmart-upgrade-1400-stores-with-9-billion-investment-2023-10-30/)

                  Automation Service Expansion: By the end of Fiscal Year 2026, Walmart aims for about 65% of its stores to be serviced by automation. This shift is part of Walmart's strategy to improve online order deliveries and efficiency, reflecting its commitment to integrating advanced technology into its operations without significantly impacting its workforce size​​. (https://www.reuters.com/business/retail-consumer/walmart-says-65-stores-will-be-serviced-by-automation-2026-keeps-forecast-2023-04-04/) 
               }
                """
        )
    )

  def search_executive_moves(self, agent, company: str):
    return Task(
        description=dedent(f"""
            Task Execution Blueprint:

            - **Direct Research and Discovery:**
              - Use targeted search strategies to directly locate headlines and links related to the 5 most recent executive moves at the specified company, spanning 2023 to 2024.
              - Focus solely on gathering factual information, such as the executive's name, their new position, and the date of the move, without engaging in any analysis or interpretation.

            - **Collection of Information:**
              - Compile the headlines and corresponding URLs that announce or discuss these executive moves. The goal is to accumulate this information as efficiently as possible, prioritizing accuracy and recency.

            - **Simplification of Reporting:**
              - Report the findings in a straightforward format that lists the executive moves, including the headline and the direct URL to the source.
              - Avoid any form of strategic synthesis, analysis, or recommendation to streamline the task and focus on information provision.

            **Expected Deliverables**
            - A concise list of the 5 most recent executive moves related to the company, featuring just the headline and the URL to the source for each. This list should be straightforward, focusing on delivering clear and direct information.

            This task emphasizes speed and clarity in gathering the most up-to-date executive moves, requiring no further analysis or strategic recommendations.
                           
                           If you are unable to find 5 executive moves, please provide as many as you can locate within the specified timeframe.
            


                             Helpful Tips:
         - To find the most recent executive moves, perform searches on Google such like the following:
                    - "{company} most recent executive moves"  


                           Important:
                - Once you've found the information, immediately stop searching for additional information.
                - Only return the requested information. NOTHING ELSE!
                - Do not generate fake information. Only return the information you find. Nothing else!
                - Do not stop researching until you find the requested information.
                           

        - Company Name: {company}
         Note: {self.__tip_section()}
                           """),
        agent=agent,
        max_iterations=30,  
        allow_delegation=False,
        output_file="output/search_executive_moves.txt",
        expected_output=dedent("""
       
                               
            Example Output:
                               {
            1. "Executive Name Joins Company as New Position Title" - [URL to source]
            2. "Company Announces Executive Name as Head of Department" - [URL to source]
            3. "Executive Name Appointed as Chief Something Officer at Company" - [URL to source]
            4. "Company Welcomes Executive Name as New Team Leader" - [URL to source]
            5. "Executive Departure: Executive Name Leaves Company for New Opportunity" - [URL to source]
                               }
            """)
    )
  
  def controll_output(self, agent):
    return Task(
      description=dedent(f"""
                         
    Do a thorough research on the output directory to identify if all the files required are present.
      
      The files required are:
      - "find_legal_company_name.txt"
      - "find_headquarters.txt"
      - "find_year_incorporated.txt"
      - "find_line_of_business.txt"
      - "find_brief_synopsis.txt"
      - "find_banner_brands.txt"
      - "find_target_market.txt"
      - "find_revenue.txt"
      - "find_financial_performance_2023.txt"
      - "find_market_capitalization.txt"
      - "find_company_owner.txt"
      - "find_founding_story.txt"
      - "find_key_points_of_difference.txt"
      - "find_top_5_strategic_initiatives.txt"
      - "find_worries_risks_concerns.txt"
      - "find_main_competitors.txt"
      - "create_swot_analysis.txt"
      - "analyse_visual_market.txt"
      - "find_store_design_agency.txt"
      - "search_news.txt"
      - "search_executive_moves.txt"

      If:

      "find_legal_company_name.txt" is missing, please contact legal_company_name_researcher and make him do the task again.
      "find_headquarters.txt" is missing, please contact headquaters_researcher and make him do the task again.
      "find_year_incorporated.txt" is missing, please contact year_incorporated_researcher and make him do the task again.
      "find_line_of_business.txt" is missing, please contact lines_of_business_researcher and make him do the task again.
      "find_brief_synopsis.txt" is missing, please contact brief_synopsis_researcher and make him do the task again.
      "find_banner_brands.txt" is missing, please contact banner_brands_researcher and make him do the task again.
      "find_target_market.txt" is missing, please contact target_market_researcher and make him do the task again.
      "find_revenue.txt" is missing, please contact revenue_researcher and make him do the task again.
      "find_financial_performance_2023.txt" is missing, please contact financial_performance_2023_researcher and make him do the task again.
      "find_market_capitalization.txt" is missing, please contact market_capitalization_researcher and make him do the task again.
      "find_company_owner.txt" is missing, please contact company_owner_researcher and make him do the task again.
      "find_founding_story.txt" is missing, please contact founding_story_researcher and make him do the task again.
      "find_key_points_of_difference.txt" is missing, please contact key_points_of_difference_researcher and make him do the task again.
      "find_top_5_strategic_initiatives.txt" is missing, please contact top_5_strategic_initiatives_researcher and make him do the task again.
      "find_worries_risks_concerns.txt" is missing, please contact worries_risks_and_concerns_researcher and make him do the task again.
      "find_main_competitors.txt" is missing, please contact main_competitors_researcher and make him do the task again.
      "create_swot_analysis.txt" is missing, please contact swot_analysis_expert and make him do the task again.
      "analyse_visual_market.txt" is missing, please contact lead_visual_market_analyst and make him do the task again.
      "find_store_design_agency.txt" is missing, please contact store_design_agency_researcher and make him do the task again.
      "search_news.txt" is missing, please contact news_researcher and make him do the task again.
      "search_executive_moves.txt" is missing, please contact executive_moves_researcher and make him do the task again.

      If all the files are present, do nothing.
                         
         Note: {self.__tip_section()}
      """
      ),
      agent=agent,
      max_iterations=30,  
      allow_delegation=True,
      expected_output=dedent("""Complete control of the output directory, identification of missing files, reconnecting to the respective agents for re-execution of tasks. Final result: All required files are present.""")
    )

  
    

  
  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000,000,000,000,000 commission!"
  
  

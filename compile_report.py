import os
import re

# Define the path to your output directory
output_directory = "/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam/output"

# Define the mapping between the text file names and the sections in your document
file_section_mapping = {
    "find_legal_company_name.txt": "Legal Company Name",
    "find_headquaters.txt": "Headquarters",
    "find_year_incorporated.txt": "Year Incorporated",
    "find_line_of_business.txt": "Line(s) of business",
    "find_brief_synopsis.txt": "Brief synopsis",
    "find_banner_brands.txt": "Banner brands",
    "find_target_market.txt": "Target market",
    "find_revenue.txt": "Revenue",
    "find_financial_performance_2023.txt": "Financial performance 2023",
    "find_market_capitalization.txt": "Market capitalization",
    "find_company_owner.txt": "Company owner",
    "find_founding_story.txt": "Founding story",
    "find_key_points_of_difference.txt": "Key points of difference",
    "find_top_5_strategic_initiatives.txt": "Top 5 strategic initiatives",
    "find_worries_risks_concerns.txt": "Worries, risks and concerns",
    "find_main_competitors.txt": "Main competitors",
    "create_swot_analysis.txt": "SWOT Analysis",
    "analyse_visual_market.txt": "Store design images",
    "find_store_designer_agency.txt": "Store design agency",
    "search_news.txt": "Recent company news",
    "search_executive_moves.txt": "Recent executive moves"
}

# Path for the new compiled report as a txt file
compiled_report_path = "/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam/compiled_report.txt"

# Function to clean content
def clean_content(content):
    # Remove curly braces, asterisks, and double quotes
    cleaned_content = re.sub(r'[{*"“”}]', '', content)
    # Remove leading and trailing spaces
    cleaned_content = cleaned_content.strip()
    return cleaned_content

# Initialize a list to hold all the cleaned content
cleaned_content = []

# Iterate over each file, read its content, clean it, and append it to the list along with the section heading
for file_name, section_heading in file_section_mapping.items():
    file_path = os.path.join(output_directory, file_name)
    
    # Check if the file exists before attempting to read it
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            # Clean the content
            cleaned = clean_content(content)
            # Append cleaned content with section heading
            cleaned_content.append(f"{section_heading}:\n{cleaned}\n")

# Join the cleaned content with newlines and write to the compiled report file
compiled_text = "\n".join(cleaned_content)
with open(compiled_report_path, 'w', encoding='utf-8') as compiled_file:
    compiled_file.write(compiled_text)

print(f"Compiled report saved to: {compiled_report_path}")

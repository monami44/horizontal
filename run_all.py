import concurrent.futures
import subprocess
import os
import re

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

# Function to run each main file, passing the company name as a command-line argument
def run_script(script_name, company):
    subprocess.run(['python3', script_name], input=company, text=True, check=True)

def execute_scripts_in_batches(batches, company):
    for batch in batches:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(run_script, script, company) for script in batch]
            concurrent.futures.wait(futures)

def check_required_files_and_trigger(directory, files_required, sup_main_py_directory, company):
    files_present = os.listdir(directory)
    missing_files = [file for file in files_required if file not in files_present]
    
    if missing_files:
        print(f"Missing files for company: {company}")
        for file in missing_files:
            print(f"- {file}")
            sup_main_py_file = f"sup_main{files_required.index(file) + 1}.py"
            sup_main_py_path = os.path.join(sup_main_py_directory, sup_main_py_file)
            print(f"Triggering {sup_main_py_file} for missing file...")
            subprocess.run(["python3", sup_main_py_path], input=company, text=True, check=True)
    else:
        print("All required files are present.")

def compile_and_clean_report(output_directory):
    compiled_report_path = os.path.join(output_directory, "compiled_and_cleaned_report.txt")
    
    def clean_content(content):
        cleaned_content = re.sub(r'[{*"“”}]', '', content)
        cleaned_content = cleaned_content.strip()
        return cleaned_content
    
    cleaned_content = []
    for file_name, section_heading in file_section_mapping.items():
        file_path = os.path.join(output_directory, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                cleaned = clean_content(content)
                cleaned_content.append(f"**{section_heading}:**\n{cleaned}\n")
    
    compiled_text = "\n".join(cleaned_content)
    with open(compiled_report_path, 'w', encoding='utf-8') as compiled_file:
        compiled_file.write(compiled_text)

    print(f"Compiled and cleaned report saved to: {compiled_report_path}")

if __name__ == "__main__":
    company = input("Enter the company name you want to analyze: ")
    output_directory = "/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam/output"
    sup_main_py_directory = output_directory
    
    scripts = ['main1.py', 'main2.py', 'main3.py', 'main4.py', 'main5.py', 
               'main6.py', 'main7.py', 'main8.py', 'main9.py', 'main10.py', 
               'main11.py', 'main12.py', 'main13.py', 'main14.py', 'main15.py', 
               'main16.py', 'main17.py', 'main18.py', 'main19.py', 'main20.py', 'main21.py']
    


    required_files = [
        "find_legal_company_name.txt",
        "find_headquaters.txt",
        "find_year_incorporated.txt",
        "find_line_of_business.txt",
        "find_brief_synopsis.txt",
        "find_banner_brands.txt",
        "find_target_market.txt",
        "find_revenue.txt",
        "find_financial_performance_2023.txt",
        "find_market_capitalization.txt",
        "find_company_owner.txt",
        "find_founding_story.txt",
        "find_key_points_of_difference.txt",
        "find_top_5_strategic_initiatives.txt",
        "find_worries_risks_concerns.txt",
        "find_main_competitors.txt",
        "create_swot_analysis.txt",
        "analyse_visual_market.txt",
        "find_store_designer_agency.txt",
        "search_news.txt",
        "search_executive_moves.txt"
    ]

    # Divide the scripts into batches for execution
    batch1 = scripts[0:5]   # Scripts 1-5
    batch2 = scripts[5:10]  # Scripts 6-10
    batch3 = scripts[10:15] # Scripts 11-15
    batch4 = scripts[15:]   # Scripts 16-21

    # Execute the scripts in batches
    execute_scripts_in_batches([batch1, batch2, batch3, batch4], company)

    # Directory paths for checking file presence
    directory_path = "/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam/output"
    sup_main_py_directory = "/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam"

    # After executing all scripts, check for missing files
    print("Checking for missing files...")
    check_required_files_and_trigger(directory_path, required_files, sup_main_py_directory, company)

    # Now, compile and clean the report after all scripts have been executed
    compile_and_clean_report(directory_path)

    print("All scripts have been executed, file presence checked, and report compiled and cleaned.")

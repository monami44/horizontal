import os
import subprocess
import sys

# Directory to check
directory_path = "/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam/output"

# Directory where the sup_main.py files are located
sup_main_py_directory = "/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam"

# List of required files
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

def check_required_files_and_trigger(directory, files_required, sup_main_py_dir, company):
    files_present = os.listdir(directory)
    missing_files = [file for file in files_required if file not in files_present]
    
    if missing_files:
        print(f"Missing files for company: {company}")
        for file in missing_files:
            print(f"- {file}")
            # Calculate which sup_main.py should be executed based on missing file's index
            sup_main_py_file = f"sup_main{files_required.index(file) + 1}.py"
            sup_main_py_path = os.path.join(sup_main_py_dir, sup_main_py_file)
            
            # Execute the respective sup_main.py
            print(f"Triggering {sup_main_py_file} for missing file...")
            subprocess.run(["python3", sup_main_py_path, company], check=True)
    else:
        print("All required files are present.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Company name not provided. Please provide the company name as a command-line argument.")
        sys.exit(1)  # Exit if no company name is provided
    company = sys.argv[1]
    check_required_files_and_trigger(directory_path, required_files, sup_main_py_directory, company)

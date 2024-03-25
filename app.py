from flask import Flask, request, jsonify, render_template
import concurrent.futures
import subprocess
import os
import re
import time

app = Flask(__name__)

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

def check_required_files_and_trigger(directory, files_required, sup_main_py_directory, company, retries=3):
    for attempt in range(retries):
        files_present = os.listdir(directory)
        missing_files = [file for file in files_required if file not in files_present]
        
        if not missing_files:
            print("All required files are present.")
            return True
        
        print(f"Attempt {attempt + 1} of {retries}: Missing files for company: {company}")
        for file in missing_files:
            print(f"- {file}")
            sup_main_py_file = f"sup_main{files_required.index(file) + 1}.py"
            sup_main_py_path = os.path.join(sup_main_py_directory, sup_main_py_file)
            print(f"Triggering {sup_main_py_file} for missing file...")
            result = subprocess.run(["python3", sup_main_py_path], input=company, text=True, check=True)

            if result.returncode != 0:
                print(f"Error running {sup_main_py_file}: {result.stderr}")
                time.sleep(10)  # Sleep for 10 seconds before retrying
                break
        else:
            print("All missing files processed on this attempt.")
            return True  # All missing files processed successfully
        print("Some files failed to process, retrying...")
    return False  # Failed to process all missing files after retries


def compile_and_clean_report(output_directory):
    compiled_report_path = os.path.join(output_directory, "compiled_and_cleaned_report.html")  # Change to .html
    try:
        cleaned_content = []
        for file_name, section_heading in file_section_mapping.items():
            file_path = os.path.join(output_directory, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    # Add HTML tags for bold text and convert URLs to clickable links
                    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)  # Bold
                    content = re.sub(r'https?://\S+', r'<a href="\g<0>">\g<0></a>', content)  # URLs
                    cleaned_content.append(f"<strong>{section_heading}:</strong><br>{content}<br><br>")
        
        compiled_text = "\n".join(cleaned_content)
        with open(compiled_report_path, 'w', encoding='utf-8') as compiled_file:
            compiled_file.write(compiled_text)
        print(f"Compiled and cleaned report saved to: {compiled_report_path}")
        return True
    except Exception as e:
        print(f"Failed to compile and clean the report: {e}")
        return False



@app.route('/')
def index():
    # Serve the HTML file
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def handle_run_script():
    company = request.json['company']

    # Assuming the output and supplementary script directories are correct
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

    success = compile_and_clean_report(directory_path)

    compiled_report_path = os.path.join(directory_path, "compiled_and_cleaned_report.html")

    report_content = ""

    if success and os.path.exists(compiled_report_path):
        with open(compiled_report_path, 'r', encoding='utf-8') as file:
            report_content = file.read()
        message = f"Report successfully compiled for {company}"
    else:
        message = f"Failed to compile the report for {company}"
    
    # Return both the message and the report content
    return jsonify(message=message, reportContent=report_content)

    
    


if __name__ == '__main__':
    app.run(debug=True)

import os
import json

def replace_patterns_and_backslashes_in_ipynb(file_path):
    # Load the notebook JSON
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Define the replacement function for patterns and backslashes
    def replace_patterns_in_string(s):
        # Replace label=' with label=r'
        s = s.replace("label='", "label=r'")
        # Replace label(' with label(r'
        s = s.replace("label('", "label(r'")
        # Replace label="" with label=r"
        s = s.replace('label="', 'label=r"')
        # Replace label(" with label(r"
        s = s.replace('label("', 'label(r"')
        
        # Replace description=' with description=r'
        s = s.replace("description='", "description=r'")
        # Replace description="" with description=r"
        s = s.replace('description="', 'description=r"')
        
        # Replace annotate(' with annotate(r'
        s = s.replace("annotate('", "annotate(r'")
        # Replace annotate(" with annotate(r"
        s = s.replace('annotate("', 'annotate(r"')

        # Replace double backslashes \\ with single backslash \
        s = s.replace('\\\\', '\\')
        return s

    # Recursively apply the replacements to all cells
    def transform_cell(cell):
        if isinstance(cell, str):
            # Apply the string replacements to each string
            return replace_patterns_in_string(cell)
        elif isinstance(cell, list):
            return [transform_cell(item) for item in cell]
        elif isinstance(cell, dict):
            return {key: transform_cell(value) for key, value in cell.items()}
        else:
            return cell

    # Apply the transformation to the entire notebook
    notebook = transform_cell(notebook)

    # Save the modified notebook back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)
    
    print(f"All replacements have been made successfully in {file_path}.")

# Function to apply the script to all .ipynb files in the current folder
def process_all_ipynb_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.ipynb'):
            file_path = os.path.join(folder_path, file_name)
            replace_patterns_and_backslashes_in_ipynb(file_path)

# Run the script for all .ipynb files in the current directory
#folder_path = '.'  # You can specify another folder path if needed
#process_all_ipynb_files_in_folder(folder_path)

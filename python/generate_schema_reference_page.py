#!/usr/bin/env python3

import os
import json

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
SCHEMA_REFERENCE_PAGE = "../docs/schema_reference.md" # schema reference page file, relative to this script
SCHEMAS_FOLDER = "../schema/" # Schema folder to look in, relative to this script
REFERENCE_PAGE_TOKEN = "{{insert_schema_reference_tables}}" # This is the token that will be replaced in the reference page by the directives to build a table

def build_directives_string_from_schema_directory(path):
    output = "" # String to return

    print(f"Looking for schemas in \"{path}\"…")
    
    directory = os.fsencode(path)

    for the_file in os.listdir(directory):
        print(f"Found:\t {os.fsdecode(the_file)}")
         
        # Only open files, not the directories inside this folder and also ignore openapi.json
        if os.path.isfile(os.path.join(directory,the_file)) and os.fsdecode(the_file) != "openapi.json":
            with open(os.path.join(directory,the_file), 'r') as schema_file:
                schema_name = json.loads(schema_file.read())['name']
                output += f"### {schema_name}\n\n```{{jsonschema}} ../schema/{schema_name}.json\n```\n" ## Build to sphinx directive here

    return output

def replace_token_in_reference_page_with_directive_string(reference_page_path, token,  directive_string):

    # First read the file and build a string representing the edited file
    new_contents = ""

    with open(reference_page_path,'r') as reference_page_file:
        for line in reference_page_file.readlines():
            if line.strip() == token:
                new_contents += directive_string
            else:
                new_contents += line

    # Now re-open in write mode and overwrite the entire file
    with open(reference_page_path,'w') as reference_page_file:
        reference_page_file.write(new_contents)


directives_string = build_directives_string_from_schema_directory(os.path.join(SCRIPT_DIR,SCHEMAS_FOLDER))
replace_token_in_reference_page_with_directive_string(os.path.join(SCRIPT_DIR,SCHEMA_REFERENCE_PAGE), REFERENCE_PAGE_TOKEN, directives_string)

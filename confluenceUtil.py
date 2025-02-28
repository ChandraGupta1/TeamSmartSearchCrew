import Insert_data_ai as data
from atlassian import Confluence
from transformers import pipeline
import configparser

# Read configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

def search_confluence(query):
    print("Connecting to Confluence...")
    confluence = Confluence(
        url=config['Confluence']['url'],
        username=config['Confluence']['username'],
        password=config['Confluence']['password']
    )
    print("Searching Confluence...")

    results = confluence.cql(f'text ~ "{query}"')

    answer =  data.generate_answer_from_natural_language(query, results)
    return answer


# results = search_confluence("Automation Testing")
# print(results)

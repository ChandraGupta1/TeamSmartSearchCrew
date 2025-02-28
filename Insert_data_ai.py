import requests
def generate_answer_from_natural_language(natural_query, sql_result):
    try:
        # Prepare the prompt similar to what we did with OpenAI GPT
        prompt = f"""
        You need to provide an answer to the following question:
 
        {natural_query}
 
        Based on the Confluence data provider below:
 
        {sql_result}
 
        Get me the top appropriate results.
        """
 
        # Define the endpoint for the Gemini API (Hypothetical endpoint)
        gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyD8CxchOBzq6_S22BR4GGup6K0be4nMRqI"  # Adjust with actual Gemini endpoint
 
        headers = {
           # "Authorization": f"Bearer {gemini_api_key}",
            "Content-Type": "application/json"
        }
 
        # The payload structure might be different for Gemini, so this is hypothetical
        # data = {
        #     "model": "gemini-2.0-flash",  # Replace with the appropriate model version
        #     "prompt": prompt,
        #     "max_tokens": 200,
        #     "temperature": 0.7
        # }
 
        data = {
            "contents": [{
            "parts":[{"text": prompt}]
        }]
        }
 
        # Sending request to Gemini API
        response = requests.post(gemini_url, headers=headers, json=data)
        # sql_keywords = r"\b(sql)\b"
 
        # Check if the response is successful
        if response.status_code == 200:
            response_data = response.json()
            #print(f"Error: {response_data['candidates'][0]['content']['parts'][0]['text']}")
            answer = response_data['candidates'][0]['content']['parts'][0]['text'].strip()
            # sql_query = re.sub(r'\s+', ' ', sql_query.strip())  # Replace multiple spaces with one
            # sql_query = re.sub(r'\s*([,;()])\s*', r'\1', sql_query)  # Remove spaces around commas, semicolons, and parentheses
            # sql_query = re.sub(r'`', '', sql_query)  # Remove all backticks
            # sql_query = re.sub(r'`', '', sql_query)  # Remove all backticks
            # cleaned_query = re.sub(sql_keywords, '', sql_query, flags=re.IGNORECASE)
 
            return answer
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Error generating SQL from natural language: {e}")
        return None
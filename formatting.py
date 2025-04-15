import json

def format_gemini_response(response):
    return response.replace('\n', '<br>')

def format_gemini_response_nope(response):

    if response is None:
        return "Error: Empty response received."

    try:
        
        if isinstance(response, str):
            return response

        if hasattr(response, 'text'):
            return response.text

        # Check for 'candidates' (common for chat/completion responses)
        if hasattr(response, 'candidates'):
            if isinstance(response.candidates, list) and len(response.candidates) > 0:
                # Get the first candidate's content.
                first_candidate = response.candidates[0]
                if hasattr(first_candidate, 'content') and hasattr(first_candidate.content, 'parts'):
                    parts = first_candidate.content.parts
                    text_parts = [part.text for part in parts if hasattr(part, 'text')] #extract text
                    return "\n".join(text_parts) #join all text parts.
                elif hasattr(first_candidate, 'content'):
                    return str(first_candidate.content)
                else:
                  return "No text content found in candidates."
            else:
                return "No candidates found in response."

        #If the response is a dict, try to format it as JSON.
        if isinstance(response, dict) or isinstance(response, list):
            return json.dumps(response, indent=2, ensure_ascii=False) # added ensure_ascii
        # If it's not a string, dict, or list, convert it to a string.
        return str(response)

    except json.JSONDecodeError:
        return "Error: Could not decode JSON response.  Returning raw string."
    except AttributeError as e:
        return f"Error: Response is not in expected format.  Details: {e}.  Returning raw string."
    except Exception as e:
        return f"Error processing response: {e}.  Returning raw string."
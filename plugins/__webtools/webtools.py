import requests
from cat.mad_hatter.decorators import tool, hook

@tool
def get_page(tool_input, cat):
    """Retrieves html of a webpage to get info and the content about that webpage. Use it when asked to go to an url or webpage. Input is the url of the webpage to get the html from."""
    r = requests.get(tool_input)
    return r.text

@tool
def get_info(tool_input, cat):
    """Retrieves more info about an argument, use it whenever not sure about something or when asked. Input is the topic to get info about."""
    blob = ''
    search = requests.get("https://ddg-api.herokuapp.com/search", params= {"query": tool_input, "limit": 5})
    for result in search.json():
        blob += f"{result['snippet']}\n\n"
    return blob
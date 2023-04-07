import re as r

class re:
    
    # Get the payload in the home page
    get_home_data = r.compile(r'name=\"(.*?)\".*value=\"(.*?)\"')
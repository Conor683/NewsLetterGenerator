import requests
import json
from HNDTs import Story
from win11toast import toast


def GetStoryIDs(endpoint):
    """Takes in an endpoint from the hacker news API and returns the ten top items from the endpoint as a list of IDs"""
    response = requests.get(endpoint)
    if response.status_code != 200:
        raise Exception(f"Unexpected response code: {response.status_code}")
    
    ids = response.json()

    return ids[:10]

def GetStory(id):
    """Takes in an ID for a hacker news story and returns a story object"""
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?")
    if response.status_code != 200:
            raise Exception(f"Unexpected response code: {response.status_code}")
    
    responseContent = response.json()

    #If there is no title return nothing
    if "title" in responseContent:
        pass
    else:
        return ""
    
    #Some stories don't have a URL
    if "url" in responseContent:
        url = responseContent["url"]
    else:
        url = ""

    S = Story(
        responseContent["title"],
        url,
        responseContent["by"],
        responseContent["score"],
        responseContent["time"]
        )

    return S

def LoadEndpoints(Path):
    """Takes in a file path and loads an endpoints dictionary from there."""
    with open(Path, "r") as f:
        EPs = json.load(f)

    return EPs

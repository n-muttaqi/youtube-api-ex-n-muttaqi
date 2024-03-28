# youtube.py
import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=query_term,
        part="snippet",
        type="video",
        maxResults=max_results
    ).execute()

    videos = search_response.get("items", [])

    return videos

if __name__ == "__main__":
    query_term = input("Enter the search query: ")
    max_results = int(input("Enter the maximum number of results: "))
    video_list = youtube_search(query_term, max_results)
    
    print(video_list)
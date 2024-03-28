# youtube.py
import sys
import config
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    all_videos = []

    next_page_token = None
    for _ in range(5): 
        search_response = youtube.search().list(
            q=query_term,
            part="snippet",
            type="video",
            maxResults=max_results,
            pageToken=next_page_token 
        ).execute()

        videos = search_response.get("items", [])
        all_videos.extend(videos)

        next_page_token = search_response.get("nextPageToken")
        if not next_page_token:
            break 

    return all_videos

if __name__ == "__main__":
    query_term = input("Enter the search query: ")
    max_results = int(input("Enter the maximum number of results per page: "))
    all_videos = youtube_search(query_term, max_results)

    print(json.dumps(all_videos, indent=2))
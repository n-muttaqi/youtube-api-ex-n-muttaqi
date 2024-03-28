import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results, page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=query_term,
        part="snippet",
        type="video",
        maxResults=max_results,
        pageToken=page_token  
    ).execute()

    videos = search_response.get("items", [])
    next_page_token = search_response.get("nextPageToken")

    return videos, next_page_token

if __name__ == "__main__":

    query_term = input("Enter the search query: ")
    max_results = int(input("Enter the maximum number of results: "))

    first_page_videos, next_page_token = youtube_search(query_term, max_results)

    print("First Page Results:")
    for video in first_page_videos:
        print(video)

    if next_page_token:

        second_page_videos, _ = youtube_search(query_term, max_results, next_page_token)

        print("\nSecond Page Results:")
        for video in second_page_videos:
            print(video)
"""
youtube_example.py

A usage example of YouTube Data API v3

The quota cost of this example is 101 quota units.
"""

import json
import requests
from pprint import pprint

API_KEY = "AIzaSyDgLXdyRnJwVLBX6xtsDgkrXrYuJnGRhLM"
SEARCH_LIST_ENDPOINT = "https://www.googleapis.com/youtube/v3/search"
VIDEO_LIST_ENDPOINT = "https://www.googleapis.com/youtube/v3/videos"

def get_video_ids(search_string: str, num_videos: int = 5) -> list:
    """Return ids of the most relevant videos associated with the search string.

    Parameters
    ----------
    search_string : str
        a search string for finding the videos
    num_videos : int
        number of returned ids of videos

    Returns
    -------
    list of strings - list of ids of the most relevant videos that are associated with the passed
    in search string. 
    """
    params = {"q": search_string, "key": API_KEY, "maxResults": num_videos, "type": "video"}
    response = requests.get(url=SEARCH_LIST_ENDPOINT, params=params).json()
    video_ids = [item['id']['videoId'] for item in response['items']]

    num_videos_left = num_videos - len(video_ids)

    while num_videos_left > 0:
        params['pageToken'] = response['nextPageToken']
        response = requests.get(url=SEARCH_LIST_ENDPOINT, params=params).json()
        video_ids.extend([item['id']['videoId'] for item in response['items']])
        num_videos_left = num_videos - len(video_ids)

    return video_ids[:num_videos]


def get_video_info(videoId: str) -> dict:
    """Return information about the video with passed in video id.

    Parameters
    ----------
    videoId : str
        Id of the video to return information about

    Returns
    -------
    dict
        A dictionary containing the following keys:
            - channelTitle
            - commentCount
            - description
            - dislikeCount
            - duration
            - likeCount
            - publishedAt
            - thumbnail
            - title
            - viewCount
    """
    params = {'id': video_id, 'key': API_KEY, 'part': 'snippet,statistics,contentDetails'}
    response = requests.get(url=VIDEO_LIST_ENDPOINT, params=params).json()
    needed_data = {}

    try:
        needed_data['duration'] = response['items'][0]['contentDetails']['duration']
        needed_data['channelTitle'] = response['items'][0]['snippet']['channelTitle']
        needed_data['description'] = response['items'][0]['snippet']['description']
        needed_data['publishedAt'] = response['items'][0]['snippet']['publishedAt']
        needed_data['thumbnail'] = response['items'][0]['snippet']['thumbnails']['default']['url']
        needed_data['title'] = response['items'][0]['snippet']['title']
        needed_data['commentCount'] = response['items'][0]['statistics']['commentCount']
        needed_data['dislikeCount'] = response['items'][0]['statistics']['dislikeCount']
        needed_data['likeCount'] = response['items'][0]['statistics']['likeCount']
        needed_data['viewCount'] = response['items'][0]['statistics']['viewCount']
    except (IndexError, KeyError) as err:
        print("This is dumb code or passed in videoId is invalid.")
        raise err

    return needed_data


if __name__ == '__main__':
    video_ids = get_video_ids("the catcher in the rye review", 1)

    for video_id in video_ids:
        pprint(get_video_info(video_id))

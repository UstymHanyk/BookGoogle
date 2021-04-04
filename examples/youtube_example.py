"""
youtube_example.py

A usage example of YouTube Data API v3

The quota cost of this example is 101 quota units.
"""

import json
from pprint import pprint

import requests

API_KEY = "YOUR_KEY"
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
    list of strings - list of video ids
    """
    params = {"q": search_string, "key": API_KEY, "maxResults": num_videos, "type": "video"}

    video_ids = []
    num_videos_left = num_videos

    while num_videos_left > 0:
        response = requests.get(url=SEARCH_LIST_ENDPOINT, params=params).json()
        if 'error' in response:
            print("An error occured. Check if the API key is valid.")
            break

        if 'items' not in response or len(response['items']) == 0:
            break

        video_ids.extend([item['id']['videoId'] for item in response['items']])
        num_videos_left = num_videos - len(video_ids)

        try:
            params['pageToken'] = response['nextPageToken']
        except KeyError:
            break

    return video_ids[:num_videos]


def get_video_info(video_id: str) -> dict:
    """Return information about the video with passed in video id.

    Parameters
    ----------
    videoId : str
        Id of the video to return information about

    Returns
    -------
    dict
        A dictionary with the following keys:
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
        needed_data['duration'] = response['items'][0]['contentDetails'].get('duration')
        needed_data['channelTitle'] = response['items'][0]['snippet'].get('channelTitle')
        needed_data['description'] = response['items'][0]['snippet'].get('description')
        needed_data['publishedAt'] = response['items'][0]['snippet'].get('publishedAt')
        needed_data['thumbnail'] = response['items'][0]['snippet']['thumbnails'].get('default', {}).get('url')
        needed_data['title'] = response['items'][0]['snippet'].get('title')
        needed_data['commentCount'] = response['items'][0]['statistics'].get('commentCount')
        needed_data['dislikeCount'] = response['items'][0]['statistics'].get('dislikeCount')
        needed_data['likeCount'] = response['items'][0]['statistics'].get('likeCount')
        needed_data['viewCount'] = response['items'][0]['statistics'].get('viewCount')
    except (IndexError, KeyError) as err:
        print("This is dumb code or passed in videoId is invalid.")
        raise err

    return needed_data


if __name__ == '__main__':
    video_ids = get_video_ids("the catcher in the rye", 21)

    for video_id in video_ids:
        pprint(get_video_info(video_id))

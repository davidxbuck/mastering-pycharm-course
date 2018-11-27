from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title link pubDate show_id')
episode_data = {}


def download_info():
    url = "http://talkpython.fm/rss"

    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall('channel/item')
    episode_count = len(items)
    for idx, item in enumerate(items):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode


def get_episode(show_id: int) -> Episode:
    """
    The get_episode method is to get an episode details
    :param show_id:
    :return:
    """
    return episode_data.get(show_id)

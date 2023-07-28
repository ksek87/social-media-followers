"""
File: social-media-followers/main.py
Program Description:
    This script will provide a user with the list accounts that do not follow them back on social media. This can be
    used to track who's unfollowing you, or to help you clear out your social media feed.
Author: @Keelin Sekerka
"""

import json
import numpy as np


def parse_followers(followers_json):
    """
    method to parse json of followers into a list of usernames
    :param followers_json:
    :return: usernames_followers
    """
    usernames_followers = []
    for follower in followers_json["relationships_followers"]:
        user = follower['string_list_data'][0]['value']
        usernames_followers.append(user)

    return usernames_followers


def parse_following(following_json):
    """
    method to parse json from following list into a list of usernames
    :param following_json:
    :return:
    """
    usernames_following = []
    for user in following_json["relationships_following"]:
        user = user['string_list_data'][0]['value']
        usernames_following.append(user)

    return usernames_following


def compare_lists(followers_li, following_li):
    """
    method to compare list of followers to following list, returning a list of users that do not follow back
    :param followers_li:
    :param following_li:
    :return: difference
    """
    difference = np.setdiff1d(following_li, followers_li).tolist()
    return difference


followers = json.load(open('data/followers.json'))
following = json.load(open('data/following.json'))

followers_list = parse_followers(followers)
following_list = parse_following(following)

diff = compare_lists(followers_list, following_list)

for i in diff:
    print(i)

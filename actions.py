# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk.knowladge_base import actions
from rasa_sdk.events import SlotSet
import praw
class ActionWeather(Action):


        reddit = praw.Reddit(client_id = 'M0r2Lz_sW0GAig',
            client_secret = 'P8lCAp8i6UG2SAah8FvBUElDLbg',
            user_agent = 'image-collector',
            username = "thsnersy" ,
            password = "thsnreddit1001" )


        subreddit = reddit.subreddit('gonewild')

        hot_python = subreddit.hot(limit=5)

        for submission in hot_python:
                if not submission.stickied:
                    print(submission.shortlink)


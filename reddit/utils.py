import praw
import os
from django.conf import settings
import re
import requests
from urllib.request import Request,urlopen
import asyncio
from datetime import datetime
from .serializers import *
from dateutil.relativedelta import relativedelta
from django.db.models import Count
from rq import Queue
from worker import conn
#const

try:
#read-only
    reddit = praw.Reddit(
    client_id=settings.REDDIT_CLIENT_ID,
    client_secret=settings.REDDIT_CLIENT_SECRET,
    user_agent=settings.REDDIT_USER_AGENT
    )
except:
    pass
f = open('reddit/tickers.txt','r')
string = f.read()
f.close()
ticker_list = string.split()



"""
DIR of reddit submissions

sh__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_chunk', '_comments_by_id', '_fetch', '_fetch_data', '_fetch_info', 
 '_fetched', '_kind', '_reddit', '_reset_attributes', '_safely_add_arguments', '_url_parts', '_vote', 'all_awardings', 'allow_live_comments', 'approved_at_utc', 
 'approved_by', 'archived', 'author', 'author_flair_background_color', 'author_flair_css_class', 'author_flair_richtext', 'author_flair_template_id', 'author_flair_text', 
 'author_flair_text_color', 'author_flair_type', 'author_fullname', 'author_patreon_flair', 'author_premium', 'award', 'awarders', 'banned_at_utc', 'banned_by', 
 'can_gild', 'can_mod_post', 
'category', 'clear_vote', 'clicked', 'comment_limit', 'comment_sort', 'comments', 'content_categories', 'contest_mode',
 'created', 'created_utc', 'crosspost', 'delete', 'disable_inbox_replies', 'discussion_type', 'distinguished', 
'domain', 'downs', 'downvote', 'duplicates', 'edit', 'edited', 'enable_inbox_replies', 'flair', 'fullname', 'gild',
'gilded', 'gildings', 'hidden', 'hide', 'hide_score', 'id', 'id_from_url', 'is_crosspostable', 'is_meta', 'is_original_content', 
'is_reddit_media_domain', 'is_robot_indexable', 'is_self', 'is_video', 'likes', 'link_flair_background_color', 'link_flair_css_class', 
'link_flair_richtext', 'link_fsh__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__lair_template_id', 'link_flair_text', 'link_flair_text_color', 'link_flair_type', 'locked',
'mark_visited', 'media', 'media_embed', 'media_only', 'mod', 'mod_notributes', '_safely_add_arguments', '_url_parts', '_vote', 'all_awardings',
'allow_live_comments', 'approved_at_utc', 'approved_by', 'archived', 'author', 'author_fte', 'mod_reason_by', 'mod_reason_title', 'mod_reports',
'name', 'no_follow', 'num_comments', 'num_crossposts', 'num_reports', 'over_18', 'parent_whitelist_statlair_type', 'author_fullname', 'author_patreon_flair',
'author_premium', 'award', 'awarders', 'banned_at_utc', 'banned_by', 'can_gild', 'can_mod_post', 'category', us', 'parse', 'permalink', 'pinned', 'pwls', 'quarantine', 
'removal_reason', 'removed_by', 'removed_by_category', 'reply', 'report', 'report_reasons', 'save', 'sable_inbox_replies', 'discussion_type', 'distinguished', 'domain', 
'downs', 'downvote', 'duplicates', 'edit', 'edited', 'enable_inbox_replies', 'flair', 'fullname'saved', 'score', 'secure_media', 'secure_media_embed', 'selftext',
'selftext_html', 'send_replies', 'shortlink', 'spoiler', 'stickied', 'subreddit', 'subreddit_in', 'is_robot_indexable', 'is_self', 'is_video', 'likes', 
'link_flair_background_color', 'link_flair_css_class', 'link_flair_richtext', 'link_flair_template_id', 'id', 'subreddit_name_prefixed', 'subreddit_subscribers',
'subreddit_type', 'suggested_sort', 'thumbnail', 'thumbnail_height', 'thumbnail_width', 'title', 'top_a, 'mod_reason_title', 'mod_reports', 'name', 'no_follow', 
'num_comments', 'num_crossposts', 'num_reports', 'over_18', 'parent_whitelist_status', 'parse', 'permalinkwarded_type', 'total_awards_received', 'treatment_tags', 
'unhide', 'unsave', 'ups', 'upvote', 'upvote_ratio', 'url', 'user_reports', 'view_count', 'visited', 'w_media', 'secure_media_embed', 'selftext', 'selftext_html', 
'send_replies', 'shortlink', 'spoiler', 'stickied', 'subreddit', 'subreddit_id', 'subreddit_name_prefixehitelist_status', 'wls'] 




dir comment forest

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', '_comments', '_gather_more_comments', '_insert_comment', '_submission', '_update', 'list', 'replace_more']


dir comments
['MISSING_COMMENT_MESSAGE', 'STR_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_extract_submission_id', 
'_fetch', '_fetch_data', '_fetch_info', '_fetched', '_kind', '_reddit', '_replies', '_reset_attributes', '_safely_add_arguments', '_submission', '_url_parts', 
'_vote', 'all_awardings', 'approved_at_utc', 'approved_by', 'archived', 
'associated_award', 'author', 'author_flair_background_color', 'author_flair_css_class', 
'author_flair_richtext', 'author_flair_template_id', 'author_flair_text', 
'author_flair_text_color', 'author_flair_type', 'author_fullname', 'author_patreon_flair', 
'author_premium', 'award', 'awarders', 'banned_at_utc', 'banned_by', 'block', 'body', 'body_html', 'can_gild', 'can_mod_post', 'clear_vote', 'collapse', 'collapsed', 
'collapsed_because_crowd_control', 'collapsed_reason', 'comment_type', 'controversiality', 
'created', 'created_utc', 'delete', 'depth', 'disable_inbox_replies', 'distinguished', 
'downs', 'downvote', 'edit', 'edited', 'enable_inbox_replies', 'fullname', 'gild', 'gilded', 'gildings', 'id', 'id_from_url', 'is_root', 'is_submitter', 'likes', 'link_id', 'locked', 
'mark_read', 'mark_unread', 'mod', 'mod_note', 'mod_reason_by', 'mod_reason_title', 'mod_reports', 'name', 'no_follow', 'num_reports', 'parent', 'parent_id', 'parse', 
'permalink', 'refresh', 
'removal_reason', 'replies', 'reply', 'report', 'report_reasons', 'save', 'saved', 'score', 'score_hidden', 'send_replies', 'stickied', 'submission', 'subreddit', 'subreddit_id', 'subreddit_name_prefixed', 
'subreddit_type', 'top_awarded_type', 'total_awards_received', 'treatment_tags', 'uncollapse', 'unsave', 'ups', 'upvote', 'user_reports']
"""



def listen_subreddit_stream(subreddit):
    for comment in reddit.subreddit(subreddit).stream.comments(skip_existing=True):
        parse_comment(comment)
    
def parse_comment(comment):
    try:
        data={
            'body':comment.body,
            'created':datetime.utcfromtimestamp(comment.created),
            'ups':comment.ups,
            'downs':comment.downs,
            'name':comment.name
        }
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        tickers = re.findall(r'\b\w{3,5}\b',comment.body.lower())
        parse_tickers(tickers,obj)
    except Exception as e:
        print(e)

def parse_tickers(tickers,comment):
    for ticker in tickers:
        if ticker in ticker_list:
            try:
                data={
                    'ticker':ticker,
                    'comment':comment.id
                }
                serializer = TickerWriteSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                obj = serializer.save()
                print(f'ticker saved {obj}')
            except Exception as e:
                print(e)
    return True

def aggregate_tickers(start=datetime.now()-relativedelta(days=1),end=datetime.now()):
    return Ticker.objects.values('ticker').order_by('ticker').annotate(count=Count('ticker')).order_by('-count')




q = Queue(connection=conn)
result = q.enqueue(listen_subreddit_stream,'wallstreetbets')

##parsing all depths of comments
# submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     ##TODO parse
#     print(comment.body)
#     ##naive finding tickers
#     # re.findall(r'[$][A-Za-z][\S]*',comment.body)

#     ##all boundary with 3 letters \b\w{3}\b
#     # re.findall(r'\b\w{3}\b',comment.body)

from operator import itemgetter

import requests
import plotly.express as px


# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

# Process data for plotting.
article_links, comment_counts = [], []
for submission_dict in submission_dicts:
    # Shorten long article titles.
    title = submission_dict['title'][:30]
    discussion_link = submission_dict['hn_link']
    article_link = f"<a href={discussion_link}>{title}</a>"
    comment_count = submission_dict['comments']

    article_links.append(article_link)
    comment_counts.append(comment_count)

print(len(article_links), len(comment_counts))
print(article_links)
print(comment_counts)

# Make visualization.
title = "Most active discussions on Hacker News"
labels = {'x': 'Article', 'y': 'Comment count'}
fig = px.bar(x=article_links, y=comment_counts)#, title=title,
        # labels=labels) #, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
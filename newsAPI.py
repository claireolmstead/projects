from newsapi import NewsApiClient


Input = input("Search a sports topic:\n")
# Init
newsapi = NewsApiClient(api_key='8aac93d6a52b4e69b0d1fe72f526afe5')

# /v2/top-headlines
"""top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')
"""
# /v2/everything
all_articles = newsapi.get_everything(q=Input,
                                      sources='fox-sports,espn',
                                      domains='foxsports.com,espn.com',
                                      from_param='2018-10-02',
                                      to='2018-10-15',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/sources
sources = newsapi.get_sources()

print("Article from: ", all_articles['articles'][1]["source"]["name"], "\n")

print("Link to image: ", all_articles['articles'][1]["urlToImage"], "\n")

print("Description: ", all_articles['articles'][1]['description'], "\n")

print("Article text: ", all_articles['articles'][1]['content'], "\n")
from flask import Flask,render_template,request
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
def home():
    api_key = '2ee1c7bb9d31470fb388358b0bc41d27'
    
    newsapi = NewsApiClient(api_key=api_key)

    country = request.args.get('country')
    category = request.args.get('category')

    if country and category:
         top_headlines = newsapi.get_top_headlines(country=country,category=category)
    elif country:
        top_headlines = newsapi.get_top_headlines(country=country)
    elif category:
        top_headlines = newsapi.get_top_headlines(category=category)
    else:
        top_headlines = newsapi.get_top_headlines()


    t_articles = top_headlines['articles']
    news = []
    desc = []
    img = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        url.append(main_article['url'])

        contents = zip(news,desc,img,url)

    return render_template('main.html',contents=contents)


if __name__ == '__main__':
    app.run(debug=True)

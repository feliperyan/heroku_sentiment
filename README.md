#Heroku Sentiment Scoring

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/feliperyan/heroku_sentiment)

Deploy to Heroku by clicking the button above then use cURL (or another tool) to issue a HTTP POST. Here's an example:

```
$ curl -X POST -H 'Content-Type: application/json' -d '{"data":"Are you kidding me? This is GREAT!"}' https://YOURAPPNAME.herokuapp.com/api/v1.0/sentiment
```

##Todo:

Add an index.html so showcase the sentiment analysis without having to issue a POST request from somewhere else.
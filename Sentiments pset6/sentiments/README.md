
Sentiments

smile.py : a program that categorizes a word as positive or negative

[![sentiments.png](https://s2.postimg.org/7n0kt9ggp/sentiments.png)](https://postimg.org/image/t9flaaf11/)

tweets.py categorizes a user’s recent 50 tweets as positive or negative (uses Twitter API)

Usage: 

1- Sign up for Twitter at twitter.com/signup if you don’t already have an account.

2- Visit apps.twitter.com, logging in if prompted, and click Create New App. Go to your keys and Tokens and copy the values.


3- Using Cloud9: 

```javascript
~/workspace/sentiments/ (master) $ export API_KEY=<API_KEY from Twitter here>
~/workspace/sentiments/ (master) $ export API_SECRET=<API_SECRET from Twitter here>
~/workspace/sentiments/ (master) $ export FLASK_APP=application.py
~/workspace/sentiments/ (master) $ flask run
```


Last 3 projects implemented in CS50 course:

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





Finance

Implement a website via which users can "buy" and "sell" stocks, a la the below.

[![finance.png](https://s2.postimg.org/imls4ymc9/finance.png)](https://postimg.org/image/vdzybgw45/)

Requirements & Dependencies:
```javascript
cd ~/workspace/pset7/finance/
pip3 install --user -r requirements.txt
```
Usage: 
```javascript
~/workspace/pset7/finance/ (master) $ flask run
~/workspace/pset7/finance/ (master) $ phpliteadmin finance.db
```

Mashup
Implement a website that lets users search for articles atop a map (using Google's API)

[![mashup.png](https://s2.postimg.org/tm6zgmxcp/mashup.png)](https://postimg.org/image/yxlw1cjf9/)

Requirements & Dependencies:
```javascript
cd ~/workspace/pse8/mashup/
pip3 install --user -r requirements.txt
```
Usage: 
```javascript
~/workspace/pset8/mashup/ (master) $ export API_KEY=<API_KEY from Google Maps API>
~/workspace/pset8/mashup/ (master) $ flask run
~/workspace/pset8/mashup/ (master) $ phpliteadmin mashup.db
```


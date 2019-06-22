-Kevin and I predict engagement from news headlines-

Is there a trend in the text of news headlines that people like the most, and 
the headlines that people interact with the most?

In the realm of reddit's r/worldnews, can the score of a post be 
predicted using the text? Can the number of comments??

The score and comments are very dependent on how long a post has been on the web.
Other paramaters that might influece a post are the time it was posted as 
well as the day of the week.

The default setting for reddit's webpage is to show items that they identify as 'Hot',
using their own algorithm. 
There are multiple ways to view the page. Reddit implemented a new user interface, that
has fewer items per page (with out scrolling down). 'Old reddit' retains a more densely
dislpayed page layout.

To collect data related, we began exploring the PRAW reddit API wrapper 
for python. The submissions retrieveable were limited to 1000 for a particular topic.
To retrieve more data we elected to scrape archive.org's captures of reddit over the past
year. Archived captures of 'new reddit' had more days archived but only had 8 posts per page,
since the archives do not include the everscroll implemented by reddit. There are less
archived captures of old reddit but the captures included.

We elected to utilize old reddit to get submissions that were farther from the top, to get
a wider distribution of 'hot' headlines. Ultimately our model did not perform well, with the
predictions changing very little with respect to the headline input.

We trained two seperate models, one to predict score, and one to predict comments.

To explore we applied Tf-Idf(Term Frequency - Inverse Document Frequency) transformations,
as well as word embeddings from GloVe. Our test set was the most recent 20 % of our raw data
set. Ultimately Tf-IDF combined with GloVe performed best for score and just GloVe performed
best for comments. Our models had a mean absolute error of approximately 6600 predicting score,
and approximately 550 predicting comments. We intially failed to tokenize the text pre-GloVe,
and once applying tokenize did not see model improvement.


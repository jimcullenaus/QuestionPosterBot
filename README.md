# QuestionPosterBot

A bot which reposts top-level comments from one thread and posts them as individual comments to another thread.

The intended use of this bot is to allow posting an announcement of an AMA where users can submit questions ahead of time,
and have their questions delivered to the participant automatically when the AMA begins.

The bot is run as a standalone Python script as follows:

```python
python question_poster_bot.py <source-thread-id> <destination-thread-id>
```

Bot is written targeting PRAW 7.5 and Python 3.8.

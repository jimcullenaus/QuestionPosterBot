# QuestionPosterBot

A bot which reposts top-level comments from one thread and posts them as individual comments to another thread.

The intended use of this bot is to allow posting an announcement of an AMA where users can submit questions ahead of time,
and have their questions delivered to the participant automatically when the AMA begins.

## How to run your own

1. Install PRAW. [See the PRAW website for instructions](https://praw.readthedocs.io/en/latest/getting_started/installation.html). QuestionPosterBot is written targetting PRAW 7.5 and Python 3.8.
2. Created a Reddit authorised app [here](https://www.reddit.com/prefs/apps/)
3. Give the bot a name of your choosing, set its type to "script", leave the about url blank or point to this repo. Add a description if you want, and set the redirect uri to http://localhost:8080.
4. Make a note of the `client_id`, which is the number found under the words "personal use script", under the name of your bot, once you have created the app. Also note your `secret`.
5. Create a `praw.ini` file in the same directory as this application, formatted as shown. `username` and `password` refer to the user account you wish to run the bot under.
```ini
[QuestionBot]
username=<username>
password=<password>
client_id=<client_id>
client_secret=<secret>
```
6. Run the script and provide it with arguments as shown:
```python
python question_poster_bot.py <source-thread-id> <destination-thread-id> <username>
```
where `<username>` refers to the username of the user responsible for running the script, for use with the bot's user agent.

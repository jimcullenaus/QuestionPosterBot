import praw
import argparse

class QuestionPosterBot:
	source_id: str
	destination_id: str
	reddit: praw.Reddit

	def run(self):
		self.get_arguments()
		self.log_in()

		top_comments = self.get_top_comments()

		self.post_comments(top_comments)


	def get_arguments(self):
		parser = argparse.ArgumentParser(description="Copy top-level comments from one Reddit thread to another.")
		parser.add_argument('source', type=str, help="The thread to copy top-level comments from")
		parser.add_argument('destination', type=str, help="The thread to submit top-level comments to")

		args = parser.parse_args()

		self.source_id = args.source
		self.destination_id = args.destination

	def log_in(self):
		self.reddit = praw.Reddit(
			"QuestionBot",
			user_agent="praw:QuestionPoster:1.0.0 (by /u/Zagorath)",
		)

	def get_top_comments(self):
		source_post = self.reddit.submission(self.source_id)
		source_post.comments.replace_more(limit=None)
		return (comment for comment in source_post.comments if self.is_valid_comment(comment))

	def post_comments(self, comments):
		destination_post = self.reddit.submission(self.destination_id)

		for comment in comments:
			reply = f"From /u/{comment.author}:\n\n{comment.body}"
			print(f"Repling with: {comment.body[:80]}")
			destination_post.reply(reply)

	def is_valid_comment(self, comment: str):
		return (comment.author is not None
			and not comment.distinguished)

if __name__ == '__main__':
	bot = QuestionPosterBot()
	bot.run()

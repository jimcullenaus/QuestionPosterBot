import praw
import argparse
from args import Args

def run():
    args = get_arguments()
    print(args.source)
    

def get_arguments():
    parser = argparse.ArgumentParser(description="Copy top-level comments from one Reddit thread to another.")
    parser.add_argument('source', type=str, help="The thread to copy top-level comments from")
    parser.add_argument('destination', type=str, help="The thread to submit top-level comments to")

    args = parser.parse_args()

    return Args(args.source, args.destination)



def log_in():
    reddit = praw.Reddit(
        user_agent="praw:QuestionPosterBot:0.1.0 (by /u/Zagorath)",
    )





if __name__ == '__main__':
    run()
import json
import re
from collections import defaultdict

with open('./ForumCrawler/comments.json') as f:
    comments = json.load(f)
    user_comments = defaultdict(list)
    for comment in comments:
        user_comments[comment['user']].append(comment['comment'])


command = input("""
Welcome to Comments CLI.
Use the following commands to interact with the system:
help -> shows the list of available commands.
list users -> shows all the users which has comments in our database.
get comments <user> -> shows all the comments of a single user.
get count comments -> shows list of users and count of the comments for each of them.
Exit -> terminates the program.

""")

def help():
    print("""help -> shows the list of available commands.
list users -> shows all the users which has comments in our database.
get comments <user> -> shows all the comments of a single user.
get count comments -> shows list of users and count of the comments for each of them.
Exit -> terminates the program.""")

def list_users():
    for user in user_comments.keys():
        print(user)

def get_count_comments():
    for user in user_comments.keys():
        print(user, '->', len(user_comments[user]))

def get_user_comments(user):
    for comment in user_comments[user]:
        print(comment)
        print("\n\n")

while command.lower() != "exit":
    matcher = re.search(r"^get user comments (.+)$", command)
    if command.lower() == "help":
        help()
    elif command.lower() == "list users":
        list_users()
    elif command.lower() == "get count comments":
        get_count_comments()
    elif matcher is not None:
        get_user_comments(matcher.group(1))
    else:
        print("This command is not available.")
    command = input("\nEnter next command: ")





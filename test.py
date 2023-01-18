from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!!"

users = [
    {
        "user_id": "user1",
        "username": "usesasa2",
    },
    {
        "user_id": "user2",
        "username": "usesasaasdsa2",
    }
]

@app.route("/get_user_ids")
def get_user_ids():
    ids = {"idList": []}

    for user in users:
        ids["idList"].append(user["user_id"])
    return ids

@app.route("/get_usernames")
def get_usernames():
    usernames = {"usernames": []}

    for user in users:
        usernames["usernames"].append(user["username"])
    return usernames

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)
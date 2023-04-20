import requests, json
from collections import defaultdict

r = requests.get('https://jsonplaceholder.typicode.com/todos')
website_content = r.json()
frequency_of_completed_tasks = defaultdict(int)

def making_dic(website_content, frequency_of_completed_tasks):
    for user_datas in website_content:
        if user_datas["completed"] == True:
            frequency_of_completed_tasks[user_datas["userId"]] += 1


def most_user_points(frequency_of_completed_tasks):
    most_points = max(frequency_of_completed_tasks.values())
    best_users = [
    user
    for user, max_points in frequency_of_completed_tasks.items()
    if max_points == most_points
]
    return most_points,best_users

making_dic(website_content, frequency_of_completed_tasks)
most_points, best_users = most_user_points(frequency_of_completed_tasks)

r = requests.get('https://jsonplaceholder.typicode.com/users')
users = r.json()
names_of_best_users = []
for user in users:
    if user['id'] in best_users:
        names_of_best_users.append(user['name'])
print(f'Najlepszymi pracownikami tego miesiąca byli {names_of_best_users} i mieli oni/one {most_points} punktów')





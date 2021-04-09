import json
import requests
import math
import random

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = json.loads(response.text)

response1 = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response1.text)

# Test - comment lines 14-41 to disable adding random users and posts
# If you need you can add additional names and titles to lists
names = ['Jan Kowalski', 'Marcin Nowak', 'Jane Doe', 'Darek Wąs', 'Daria Kwiatkowska', 'Anna Michalska',
         'Adam Małysz', 'Iga Ząbek', 'Natalia Bień',  'Wojtek Prysak']
titles = ['tytul1', 'tytul2', 'tytul3', 'tytul4', 'tytul5', 'tytul6', 'tytul7', 'tytul8', 'tytul9', 'tytul10',
          'tytul11', 'tytul12', 'tytul13', 'tytul14', 'tytul15', 'tytul16', 'tytul17', 'tytul18', 'tytul19', 'tytul20']

# Create new users with random names from list and random real geographic location
# You can change amount of new users by editing number 'for i in range(x)' - 'x' is amount of new users
for i in range(10):
    users.append({
        'id': len(users) + 1,
        'name': random.choice(names),
        'address': {
            'geo': {
                'lat': str(random.randint(-90, 90)),
                'lng': str(random.randint(-180, 180))
            }
        },
    })

# Create new posts for randomly chosen users and titles randomly chosen from list
# You can change amount of new posts by editing number 'for i in range(x)' - 'x' is amount of new posts
for i in range(150):
    posts.append({
        'userId': random.randint(1, len(users)),
        'id': len(posts) + 1,
        'title': random.choice(titles),
    })

# task 1
usersPosts = []

for user in users:
    usersPosts.append(0)
    for post in posts:
        if user['id'] == post['userId']:
            usersPosts[user['id'] - 1] += 1
    print(user['name'] + ' napisał(a) ' + str(usersPosts[user['id'] - 1]) + ' postów')

# task 2
postTitles = []
uniqueList = []
notUniqueList = []

for post in posts:
    postTitles.append(post['title'])

flag = len(set(postTitles)) == len(postTitles)

if flag:
    print('\nWszystkie tytuły postów są unikalne')
else:
    for title in postTitles:
        if title not in uniqueList:
            uniqueList.append(title)
        elif title not in notUniqueList:
            notUniqueList.append(title)

print('\nLista tytułów nieunikalnych:')
for title in notUniqueList:
    print(title)

# task 3
usersLocation = [[0 for x in range(2)] for y in range(len(users))]
userDistances = []
minDistancedUserId = []

for user in users:
    usersLocation[int(user['id'] - 1)][0] = float(user['address']['geo']['lat'])
    usersLocation[int(user['id'] - 1)][1] = float(user['address']['geo']['lng'])

for location in usersLocation:
    for location2 in usersLocation:
        userDistances.append(math.dist(location, location2))

    minDistance = min(i for i in userDistances if i > 0)
    for i in range(len(users)):
        if minDistance == userDistances[i]:
            minDistancedUserId.append(i)
    userDistances = []

print('\nNajbliżej mieszkający użytkownik dla:')
for i in range(len(users)):
    print(users[i]['name'] + '\t->\t' + users[minDistancedUserId[i]]['name'])

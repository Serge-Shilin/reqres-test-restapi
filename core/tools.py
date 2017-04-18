import requests


OK = 200
CREATED = 201


def post_create_user_request(host, name, job):
    return requests.post(host + '/api/users', data={"name": name,"job": job})


def get_list_users(host, page):
    return requests.get(host + '/api/users?page=' + page)


def get_user(host, id):
    return requests.get(host + '/api/user/' + str(id))
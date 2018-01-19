abc = [('北京北', 'VAP'), ('北京东', 'BOP'), ('北京', 'BJP')]
dict = dict(abc)
print(dict)

id =[1,2,3,4]
username = ['xm','xh','xq','xf']
users = []
for i in range(len(id)):
    user={}
    user['id'] = id[i]
    user['username'] = username[i]
    users.append(user)
print(users)
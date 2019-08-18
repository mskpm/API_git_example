import requests
import json
from get_repo_info import show_info
import pygal
#from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

username = 'mskpm'

# from https://github.com/user/settings/tokens
token = 'bf0642e8b1c11ab42c2489cb9c0d367d5fe3b53e'

repos_url = 'https://api.github.com/user/repos'

# create a re-usable session object with the user creds in-built

gh_session = requests.Session()
gh_session.auth = (username, token)


# get the list of repos belonging to me
repos = json.loads(gh_session.get(repos_url).text)

repo_keys, repo_all = [], []
repo_sizes = []
repo_names = []
xlink = []

for key in repos[0]:
    repo_keys.append(key)
    
for key in repos:
    repo_all.append(key)
    repo_sizes.append(key['size'])
    repo_names.append(key['name'])
    xlink.append(key['html_url'])

size_dict = dict(zip(repo_names, repo_sizes))


#rk=json.dumps(repo_keys, indent=4, sort_keys=True)
#rall=json.dumps(repo_all, indent=4, sort_keys=True)

#with open("repo_keys.json", 'w') as fp:
#    fp.write(rk)

#with open("repos_all.json", 'w') as fpa:
#    fpa.write(rall)

#for index, repo in enumerate(repos):
#    #print(index)
#    repo=repos[index]
#    show_info(repo)

# Wizaualizacja danych
#my_style = LS('#333366', base_style=LCS)
#chart = pygal.Pie(style = my_style, show_legend = True)


chart = pygal.Pie(show_legend = True)
chart.force_url_protocol = 'http'
chart.title = 'Wielkości repozytoriów użytkownika ' + username
chart.labels = repo_names


for k,v in size_dict.items():
    chart.add(k,v)

chart.render_to_file('repos_sizes.svg')


# make more requests using "gh_session" to create repos, list issues, etc.

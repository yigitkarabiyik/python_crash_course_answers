import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the rsponse.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)

print("Status code: ", r.status_code)

# Store API response in a variable.
response_dict =r.json()
print("Total repositories: ", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts= response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
#repo_dict=repo_dicts[0]

names, plot_dicts= [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	
	# Get the project description, if one is available.
	description = repo_dict['description']
	if not description:
		description = 'No description privided.'
		
	plot_dict= {
		'value': repo_dict['stargazers_count'],
		'label': description,
		'xlink': repo_dict['html_url'],
		}
	plot_dicts.append(plot_dict)
	
# Make visualization.
my_style = LS('#333366', base_style=LCS)

# Refining pygal charts
my_config =pygal.Config()
my_config.x_label_rotation = 45
my_config.shot_legend = False
my_config.title_font_size =24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)

chart.title ='Most-Starred Python Projects on GitHub'
chart.x_labels =names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')


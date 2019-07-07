try:
  import unzip_requirements
except ImportError:
  pass

import os
import json
import feedparser
import requests

from github import Github, GithubException
from github.GithubException import UnknownObjectException


class PypiProject:

    def __init__(self, project_name):
        response = requests.get("https://pypi.org/pypi/%s/json" % project_name)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        self._json = response.json()
        self._name = project_name

    def is_interesting(self):
        if "info" in self._json and "classifiers" in self._json["info"]:
            return any("Console" in s for s in self._json["info"]["classifiers"])
        return False

    def __str__(self):
        return self._name

    def pretty_print(self):
        print(json.dumps(self._json["info"], indent=4))



def pythockerize(event, context):
    gh = Github(login_or_token=os.environ["GH_TOKEN"])
    gh_org = gh.get_organization("pythockerize")

    updated_projects = get_recently_updated_projects()

    repos_created = []
    for project_name in updated_projects:
        try:
            pypi_project = PypiProject(project_name)
            if pypi_project.is_interesting():
                try:
                    gh_repo = gh_org.get_repo(project_name)
                    print("%s already exists" % gh_repo)
                except UnknownObjectException:
                    print("create repo %s" % pypi_project)
                    gh_repo = gh_org.create_repo(name=project_name)
                    repos_created.append(project_name)
                    print(gh_repo)
        except requests.HTTPError:
            pass

    return {
        "statusCode": 200,
        "body": repos_created
    }


def get_recently_updated_projects():
    feed_url = "https://pypi.org/rss/updates.xml"
    feed = feedparser.parse(feed_url)
    projects = []
    for entry in feed.entries:
        title_splitted = entry.title.split(" ")
        projects.append(title_splitted[0])
    return projects


def get_newest_projects():
    feed_url = "https://pypi.org/rss/packages.xml"
    feed = feedparser.parse(feed_url)
    projects = []
    for entry in feed.entries:
        projects.append(entry.title.split(" ")[0])
    return projects


if __name__ == "__main__":
    print(pythockerize('', ''))

#!/usr/bin/env python3

from git import Repo
from notion2md import *
import os
import shutil
import subprocess
import sys
from sys import platform

repoDir = '../informapedia.github.io'
#repoDir = sys.argv[2]

def git_push(filenameToAdd, commitMessage):
    print("Starting to push file {}", filenameToAdd)
    try:
        repo = Repo(repoDir)
        repo.git.add(filenameToAdd)
        repo.index.commit(commitMessage)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')

notionUrl = sys.argv[1]
tokenV2 = os.getenv('NOTION_TOKEN')

export_cli(token_v2=tokenV2, url=notionUrl, bmode=1)

notionTitle = None
filenameToAdd = None
for folder in os.scandir('notion2md_output'):
    notionTitle = folder.name
    for filename in os.scandir(folder):
        if filename.name.endswith('.md'):
            with open(filename, 'r') as f:
                content = f.read().replace('\n[', '[').replace('permalink: /boasPraticas/:title:output_ext', 'permalink: /boasPraticas/:year/:month/:day/:title')
            with open(filename, 'w') as f:
                f.write(content)
        filenameToAdd = os.path.join('_posts', filename.name)
        try:
            os.remove(os.path.join(repoDir, filenameToAdd))
        except:
            pass
        shutil.move(filename, os.path.join(repoDir, '_posts'))
    os.removedirs(folder)

print("start test")
oldCurrentWorkingDir = os.getcwd()

os.chdir(repoDir)
if platform == "linux" or platform == "linux2" or platform == "darwin":
    subprocess.run("./localhostTestSite.sh", stdout=subprocess.DEVNULL)
elif platform == "win32":
    subprocess.run("localhostTestSite.bat", stdout=subprocess.DEVNULL)

os.chdir(oldCurrentWorkingDir)

canPushFile = input("Can be commit? [Y/N]: ")
canPushFile = canPushFile.lower()
while canPushFile != 'y' and canPushFile != 'n':
    print("Wrong input {}, please answer with Y or N.".format(canPushFile))
    canPushFile = input("Can be commit? [Y/N]")
    canPushFile = canPushFile.lower()


if platform == "linux" or platform == "linux2" or platform == "darwin":
    os.system("ps aux | grep jekyll | awk \'{print $2}\' | xargs kill -9")

if (canPushFile == 'y'):
    git_push(filenameToAdd, "Adicionando notícia em Boas Práticas {}".format(notionTitle))
else:
    os.remove(os.path.join(repoDir, filenameToAdd))

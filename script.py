from notion2md import *
import os
import sys

notionUrl = sys.argv[1]
tokenV2 = os.getenv('NOTION_TOKEN')

export_cli(token_v2=tokenV2, url=notionUrl, bmode=1)
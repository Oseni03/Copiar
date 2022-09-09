from django.conf import settings

import os
import shutil
from pywebcopy import save_website, save_webpage

class Clone:
    def __init__(self, url, project_name):
        self.url = url 
        self.project_folder = os.path.join(settings.BASE_DIR, "projects")
        self.project_name = project_name
        self.project_path = os.path.join(self.project_folder, project_name)
    
    def website(self):
        save_website(
            url= self.url,
            project_folder= self.project_folder,
            project_name= self.project_name,
            bypass_robots=True,
            debug=True,
            open_in_browser=True,
            delay=None,
            threaded=False,
        )
        shutil.make_archive(self.project_name, "zip", self.project_path)
        resultpath = os.path.join(settings.BASE_DIR, f"{self.project_name}.zip")
        return resultpath
    
    def page(self):
        save_webpage(
            url= self.url,
            project_folder= self.project_folder,
            project_name= self.project_name,
            bypass_robots=True,
            debug=True,
            open_in_browser=True,
            delay=None,
            threaded=False,
        )
        shutil.make_archive(self.project_name, "zip", self.project_path)
        resultpath = os.path.join(settings.BASE_DIR, f"{self.project_name}.zip")
        return resultpath 
    
    def delete_files(self):
        dirs = os.listdir(self.project_folder)
        for file in dirs:
            if os.path.isdir(f"{self.project_folder}/{file}"):
                os.rmdir(f"{self.project_folder}/{file}")
            elif os.path.isfile(f"{self.project_folder}/{file}"):
                os.remove(f"{self.project_folder}/{file}")

# url = "https://www.resume.com/"
# web = Clone(url, "New_resume")
# web.website()
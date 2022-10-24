#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import re

def create_markdown(source_path, end_path, overwrite = False):
    '''This function creates for each Jupyter Notebook in source_path the respective markdown file in 
       end_path. By default, existing files in end_path are not overwritten. Whitespaces are not allowed
       in filenames.
    '''
    os.chdir(source_path)
    for f in os.listdir('.'):
        if f.endswith('ipynb'):
                f_md = re.sub('.ipynb', '.md', f)        # filename with changed file extension
                if not(os.path.exists(end_path + f_md)): # True if the respecitve fail does not exist
                    os.system("jupyter nbconvert --to markdown " + f)
                    os.rename(source_path + f_md, end_path + f_md)
                elif overwrite == True:
                    os.remove(end_path + f_md)
                    os.system("jupyter nbconvert --to markdown " + f)
                    os.rename(source_path + f_md, end_path + f_md)
    print('Finished ' + source_path + ".")
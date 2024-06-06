#!/usr/bin/python3
from fabric import task
from time import strftime
from datetime import datetime

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    local = c.local  # Adjust for Fabric 3.x
    
    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Create the archive name with the current date and time
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    # Print message indicating the start of the packing process
    print("Packing web_static to {}".format(archive_name))

    # Create the archive
    try:
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        print("An error occurred while creating the archive:", e)
        return None


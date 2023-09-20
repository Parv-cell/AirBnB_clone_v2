from fabric.api import local
from datetime import datetime
import os

def do_pack():
	# Gets the cuurent date and time
	now = datetime.now().strftime("%Y%m%d%H%M%S")

	# Creates the versions folder if it doesn't exist
	if not os.path.exists("versions"):
		os.makedirs("versions")

	# Sets the name of the archive file
	archive_name = "web_static_" + now + ".tgz"

	# Creates the archive by compressing the web_static folder
	result = local("tar -czvf versions/{} web_static".format(archive_name))

	# Checks if archive was created successfully
	if result.succeeded:
		# Returns the path of the created archive
		return "version/" + archive_name
	else:
		# Returns None if the archive creation failed
		return None

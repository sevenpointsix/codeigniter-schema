import os
from fabric.api import *
from fabric.contrib import console

# We don't need to run any server commands in this fab file
# it's just a shortcut to various Git commands:

########################################################################
# local commands
########################################################################

def commit():
	"""
	Commits changes to the local repository, prompting for a commit message if necessary
	Usage:
	fab commit
	Note that in most situations, calling fab push will suffice
	"""
	msg = prompt("Commit message:", default="No message")
	_commit(msg)

def _commit(msg=None):

	local("git add .", capture=False)
	
	with settings(hide('warnings'),warn_only=True):
		if(msg):
			local("git commit -am \"%s\"" % msg, capture=False)
		else:
			local("git commit -am \"No message\"", capture=False)

def push():
	"""
	Commits changes and then pushes them to the remote repository
	Usage:
	fab push
	"""
	with hide('running'):
		print("Pushing files to remote repository")
		commit()
		local("git push origin master", capture=False)

def pull():
	"""
	Pulls changes from the remote repository, and updates the local copy
	Usage:
	fab pull
	"""
	with hide('running'):
		print("Pulling files from remote repository")
		local("git pull origin master")

def retag():
	"""
	"Retags" the repository, meaning that the current codebase becomes 1.0.0
	Based on code from http://nathanhoad.net/how-to-delete-a-remote-git-tag
	"""
	version = prompt("Enter tag:")
	_retag(version)


def _retag(version=0):	
	with hide('running'):
		if version > '':
			print("Retagging repository as %s"  % version)
			local("git tag -d %s"  % version, capture=False)
			local("git push origin :refs/tags/%s"  % version, capture=False)
			local("git tag %s"  % version, capture=False)
			local("git push origin %s"  % version, capture=False)
		else:
			print("Pleas specify the version to retag as.");

	
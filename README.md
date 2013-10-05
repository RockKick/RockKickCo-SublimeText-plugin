##Rock Kick Co. SublimeText Plugin

Tools to streamline the workflow within SublimeText.

####Installation:
Ensure [`git`](http://git-scm.com/) is installed on your local machine.

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
	git clone git@github.com:RockKickCo/RockKickCo-SublimeText-plugin.git Rock\ Kick\ Co.
	Restart SublimeText.  All plugin features are enabled by default

####Enable/Disable Features:
Set true/false what features you need enabled/disable in the settings file.

	open ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Rock Kick Co./RockKickCo.sublime-settings

####Updates:
To receive the latest updates just `git pull origin master` from your plugin folder and restart SublimeText.

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Rock Kick Co.
	git pull origin master

####Troubleshooting:
If your plugin is still pointed at an old repository you can point it at this one:

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Rock Kick Co./
	git config remote.origin.url git@github.com:Rock Kick Co./RockKickCo-SublimeText-plugin.git
	git pull origin master

####Recommended Packages:
For js and php lint check (syntax checking) try:  [SublimeLinter](http://github.com/Kronuz/SublimeLinter)

To handle all your trailing spaces issues, try: [TrailingSpace](https://github.com/SublimeText/TrailingSpaces)
##Rock Kick Co. SublimeText Plugin

Some tools to help make dev easier in SublimeText.

####Installation:
Ensure [`git`](http://git-scm.com/) is installed on your local machine.

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
	git clone git@github.vimeows.com:Vimeo/Vimeo-SublimeText-plugin.git Rock\ Kick\ Co.
	Restart SublimeText.  All plugin features are enabled by default

####Enable/Disable Features:
Set true/false what features you need enabled/disable in the settings file.

	open ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Rock Kick Co./RockKickCo.sublime-settings

####Updates:
To receive the latest updates just `git pull origin master` from your plugin folder and restart SublimeText.

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Rock Kick Co.
	git pull origin master


####Notifications:
Notifications will appear in the status bar.

![notification](http://f.cl.ly/items/3m0Z2V3P2a1V40443o2G/Screen%20Shot%202012-01-31%20at%204.32.29%20PM.png)

####Troubleshooting:
If your plugin is still pointed at an old repository you can point it at this one:

	cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Rock Kick Co./
	git config remote.origin.url git@github.com:Rock Kick Co./RockKickCo-SublimeText-plugin.git
	git pull origin master


####Recommended Packages:
For js and php lint check (syntax checking) try:  [SublimeLinter](http://github.com/Kronuz/SublimeLinter)
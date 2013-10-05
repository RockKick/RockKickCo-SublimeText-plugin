import sublime
import sublime_plugin
import functools
import os
import subprocess

class CompileCompassOnSaveListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        path = view.file_name()
        file_name = os.path.basename(path)
        settings = sublime.load_settings('RockKickCo.sublime-settings')

        # compass compiling is turned off
        if settings.get('compile_compass_on_save') is not True:
            return

        # not a sass file
        if file_name[-5:] != '.scss' and file_name[-5:] != '.sass':
            return;

        # ignore files starting with _
        if file_name[0] == '_':
            return

        # confirm file is in sass directory
        if not '/sass/' in path:
            return

        # get the project dir based on file location
        parts = path.split('/sass/')
        project_dir = parts[0]

        cmd = 'compass compile %s --output-style compressed --force' % project_dir
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        ret = process.returncode

        if ret is not 0:
            sublime.error_message("Rock Kick Co. Compass SASS Error:\n\n%s\n\nCommand executed:\n%s\n\n" % (error, cmd))
            return

        # setting timeout so that the normal save message doesn't overwrite our status
        sublime.set_timeout(functools.partial(sublime.status_message, "Compass compiled"), 500)
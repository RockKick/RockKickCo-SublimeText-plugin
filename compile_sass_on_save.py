import sublime
import sublime_plugin
import functools
import os
import re
import subprocess as sp


class CompileSassOnSaveListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        path = view.file_name()
        file_name = os.path.basename(path)
        settings = sublime.load_settings("RockKickCo.sublime-settings")

        # sass compling is turned off
        if settings.get('compile_sass_on_save') is not True:
            return

        # not a sass file
        if file_name[-5:] != ".scss" and file_name[-5:] != ".sass":
            return

        # ignore files starting with _
        if file_name[0] == "_":
            return

        if not '/sass/' in path:
            return

        parts = path.split('/sass/')
        output_dir = parts[0] + '/css/'

        sub_dir = os.path.dirname(parts[1])

        # one off for v5
        # if '/assets/styles/sass/v5/' in path:
        #     output_dir = os.path.dirname(path.replace('/styles/sass/v5', '/css_v5')) + '/'
        #     sub_dir = os.path.dirname(path.split('/styles/sass/v5/')[1])

        # if sub directories, make them part of the file name  ie: a/b/c.css -> a_b_c.css
        if sub_dir:
            # file_name = sub_dir + "/" + file_name
            # file_name = re.sub("/", "_", file_name)
            output_dir += sub_dir

        output_file = output_dir + file_name[:-5] + ".css"

        cmd = "sass %s %s --style compressed --no-cache" % (path, output_file)
        process = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = process.communicate()
        ret = process.returncode

        if ret is not 0:
            sublime.error_message("Rock Kick Co. Sublime SASS Error:\n\n%s\n\nCommand executed:\n%s\n\n" % (error, cmd))
            return

        # setting timeout so that the normal save message doesn't overwrite our status
        sublime.set_timeout(functools.partial(sublime.status_message, "Compiled SASS file to %s" % output_file), 400)

from errbot import BotPlugin, botcmd, botmatch
import subprocess, tempfile, re, time

class Setup(BotPlugin):
    """Setup plugin for Errbot"""
    
    share_drive_paths = []

    @botcmd
    def setup_path(self, msg, args):
        """Set up shared drive path between errbot and local drive"""
        
        path = args.strip()
        
        if path == "":
            yield "No path provided. Please provide an absolute path: !setup path /path/to/shareddrive"
        elif re.match("^(?:/[^/\n]+)*?$", path):
            string = str(msg.frm) + ":" + path
            new_list = []
            found = False
            for s in self.share_drive_paths:
                if s == string:
                    found = True
                else:
                    new_list.append(s)
            new_list.append(string)
            self.share_drive_paths = new_list
            if found:
                yield "Your shared drive path has been updated."
            else:
                yield "Your shared drive path was added successfully."
        else:
            yield "Absolute path required. Must be Linux path for now."

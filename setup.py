from errbot import BotPlugin, botcmd, botmatch
import subprocess, tempfile, re, time

class Setup(BotPlugin):
    """Setup plugin for Errbot"""
    
    share_drive_paths = []

    @botcmd
    def setup_path(self, msg, args):
        """Set up shared drive path between errbot and local drive"""
        string = str(msg.frm) + ":" + args
        self.share_drive_paths.append(string)
        for s in self.share_drive_paths:
            yield s

from errbot import BotPlugin, botcmd
import subprocess, tempfile, re, time

class Setup(BotPlugin):
"""Setup plugin for Errbot"""

    share_drive_paths = []

    @botcmd
    def setup(self, msg, args):
        """Set up shared drive path between errbot and local drive"""
        self.presetup(msg, args)
        self['command'] = "setup"
        
    def presetup(self, msg, args):
        """Set up the environment for input"""
        #self['permission'] = False
        #self['args'] = args
        #self['user'] = msg.frm
        self.send(msg.frm, "What is the path for your locally shared drive?")
        
    @botmatch(r'^[a-zA-Z]$', flow_only=True)
    def shared_drive(self, msg, match):
        """Confirmation dialogue"""
        string = msg.frm + ":" + match
        self.share_drive_paths.append(string)

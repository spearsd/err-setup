from errbot import botflow, FlowRoot, BotFlow, FLOW_END

class setup_flow(BotFlow):

    @botflow
    def setup_flow(self, flow: FlowRoot):
        """ This flow sets up confirmation with the users."""
        # List of flows, confirm dialogues, and commands that need confirmation
        flows = []
        con = []
        commands = ['setup']
        for i in range(len(commands)):
            flows.append(flow.connect(commands[i], auto_trigger=True))
            con.append(flows[i].connect('shared_drive'))
            con[i].connect('shared_drive')
            con[i].connect(FLOW_END)#, predicate=lambda ctx: ctx['tries'] == 0)

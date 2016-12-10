import re

class Bot(object):

    def __init__(self):
        self.values = []
        self.buffer = []

    def addCommand(self, command):
        self.buffer.append(command)

    def getCommand(self):
        return self.buffer.pop(0)

    def canExecute(self):
        return len(self.values) == 2

    def addValue(self, v):
        self.values.append(v)

    def getLow(self):
        self.values = sorted(self.values)
        return self.values.pop(0)

    def getHigh(self):
        self.values = sorted(self.values)
        return self.values.pop()

class BotProduction(object):

    def __init__(self):
        self.bots = {}
        self.outputs = {}

    def addBotIfNotExists(self, id):
        if id not in self.bots:
            self.bots[id] = Bot()

    def addValueToBot(self, id, value):
        self.addBotIfNotExists(id)
        self.bots[id].addValue(value)

    def addCommandToBot(self, id, command):
        self.addBotIfNotExists(id)
        self.bots[id].addCommand(command)

    def botsHaveBufferData(self):
        for bot_id in self.bots:
            bot = self.bots[bot_id]
            if len(bot.buffer) > 0:
                return True
        return False

    def executeBotCommands(self):
        while self.botsHaveBufferData():
            for bot_id in self.bots:
                bot = self.bots[bot_id]
                if bot.canExecute():
                    command = bot.getCommand()
                    bot_low = bot.getLow()
                    bot_high = bot.getHigh()
                    id_1 = int(command[1])
                    id_2 = int(command[3])

                    if bot_low == 17 and bot_high == 61:
                        print bot_id

                    if command[0] == 'bot':
                        self.bots[id_1].addValue(bot_low)
                    if command[0] == 'output':
                        self.outputs[id_1] = bot_low

                    if command[2] == 'bot':
                        self.bots[id_2].addValue(bot_high)
                    if command[2] == 'output':
                        self.outputs[id_2] = bot_high

input = file('day_10.input', 'r').readlines()

bot_production = BotProduction()

for line in input:
    line = line.strip()

    if 'value' in line:
        r = re.findall(r'[0-9]+', line)
        value = int(r[0])
        bot_id = int(r[1])

        bot_production.addValueToBot(bot_id, value)
    else:
        r = re.match(r'bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)', line)
        bot_id = int(r.groups()[0])
        command = r.groups()[1:]

        bot_production.addCommandToBot(bot_id, command)

bot_production.executeBotCommands()
import yaml

config = """
replay.require: step_definitions
replay.features: features
replay.data: data
replay.out: target

replay.player: replayer.web_player.WebPlayer
replay.players: 5
replay.iterations: -1

replay.think: False
replay.think.time:

"""

print yaml.load(config)

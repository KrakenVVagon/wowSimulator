from characters.playerCharacter import playerCharacter

class baseSpell:
    def __init__(self, damageCoefficient: float, playerStats: playerCharacter):
        self.damageCoefficient = damageCoefficient
        self.playerStats = playerStats

    def damage(self, spellPower):
        return self.damageCoefficient * spellPower * (1 + self.playerStats.vers)

    def cooldown(self, duration=1500):
        pass

class baseAbility:
    def __init__(self, damageCoefficient: float):
        self.damageCoefficient =  damageCoefficient

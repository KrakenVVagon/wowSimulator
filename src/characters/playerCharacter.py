from data.characterStats_data import mainStats, conversionRates

class playerCharacter:
    def __init__(self, spec: str, stats: dict, items: dict, spellFromAbility=False):
        self.spec =  spec
        self.stats = stats
        self.items = items
        self.spellFromAbility = spellFromAbility
        self.crit = stats["crit"]
        self.haste = stats["haste"]
        self.vers = stats["vers"]
        self.mastery = stats["mastery"]
        self.stamina = stats["stamina"]
        self.int = stats["int"]
        self.agi = stats["agi"]
        self.str = stats["str"]
        self.mainStat = mainStats[spec]
        self._ratingToPercent()
        self.abilityPower = self._getAbilityPower()
        self.spellPower = self._getSpellPower()

    def _getAbilityPower(self):
        return self.items["mainhandWeaponDPS"] * 6 + self.mainStat

    def _getSpellPower(self):
        if self.spellFromAbility:
            return 0
#            return spellDamageCoefficient * self.abilityPower
        return self.mainStat

    def _ratingToPercent(self):
        # assuming only level 80
        self.statPercent = {}
        # returns a whole number percentage (eg 700 crit == 1% crit) so that mastery points can be easily calculated
        for key, value in conversionRates.items():
            self.statPercent[key] = self.stats[key]/value
        return True

    def addAbility(self, ability):
        pass

    def getAbilities(self):
        pass

if __name__ == "__main__":
    stats = {
        "crit": 700,
        "haste": 700,
        "vers": 700,
        "mastery": 700
    }

class Character:
    """Defines a character"""

    def __init__(self, name: str, attact_power: int, life: int) -> None:
        """Creates an instance of a 'Character'"""
        self.name = name
        self.attact_power = attact_power
        self.life = life

    def __repr__(self) -> str:
        return "<class 'Character'>"

    def __str__(self) -> str:
        return f"Name: {self.name}, Attack Power: {self.attact_power}, life: {self.life}"


villain1 = Character("Thanos", 400, 1500)
villain2 = Character(life=1000, name="Red Score", attact_power=350)

print(villain1)
print(villain2)

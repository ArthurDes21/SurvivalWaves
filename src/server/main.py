import j2l.pytactx.agent as pytactx
from ZombieManager import ZombieManager

arbitre = pytactx.Agent(
            playerId="21122003",
            arena="survivalwaves", 
            username="demo", 
            password="demo", 
            server="mqtt.jusdeliens.com", 
            verbosity=2
        )

# Zombies names
noms_zombies = [
    "RigoloMort",
    "CervelleJoyeuse",
    "ZombiComique",
    "Risquatouille",
    "FarceurDécomposé",
]

# Rules
arbitre.ruleArena("reset", True)
arbitre.ruleArena("profiles", ["arbitre", "zombie"])
arbitre.ruleArena("pIcons", ["👮", "🧟"])
arbitre.ruleArena("dtMove", [0, 1000])
arbitre.update()

# Create zombies
zombie_manager = ZombieManager(arbitre)
zombie_manager.create_zombies(noms_zombies)
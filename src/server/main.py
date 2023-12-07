from dotenv import load_dotenv
import os
import j2l.pytactx.agent as pytactx
from ZombieManager import ZombieManager

load_dotenv() 
playerId = os.environ['PLAYER_ID']

arbitre = pytactx.Agent(
    playerId=playerId,
	arena="survivalwaves",
	username="demo",
	password="demo",
	server="mqtt.jusdeliens.com",
	verbosity=2
)

noms_zombies = [
    "RigoloMort",
    "CervelleJoyeuse",
    "ZombiComique",
    "Risquatouille",
    "FarceurDécomposé",
]

# Create zombies
zombie_manager = ZombieManager(arbitre)
zombie_manager.create_zombies(noms_zombies)

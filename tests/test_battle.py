# test_battle.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.battle import iniciar_combate
from core.game import Person
from core.magic import Spell
from core.inventory import Item

# Hechizos de prueba
fire = Spell("Fire", 10, 150, "black")
cure = Spell("Cure", 10, 70, "white")

# Ítems de prueba
potion = Item("Potion", "potion", "Heals 50 HP", 50)

# Jugadores de prueba
player1 = Person("Zack:", 3000, 400, 800, 70, [fire, cure], [{"item": potion, "quantity": 5}], "no")
player2 = Person("Leon:", 3000, 400, 110, 70, [fire, cure], [{"item": potion, "quantity": 5}], "no")
player3 = Person("Sora:", 3000, 400, 110, 70, [fire, cure], [{"item": potion, "quantity": 5}], "no")

# Llamada al combate con los datos simulados
iniciar_combate([player1, player2, player3], [fire, cure], [{"item": potion, "quantity": 5}])

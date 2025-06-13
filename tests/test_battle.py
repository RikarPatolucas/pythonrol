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

# Hechizos con efectos de estado
veneno = Spell("Toxico", 15, 0, "black", efecto={"nombre": "veneno", "duracion": 5, "potencia": 80})
aturdir = Spell("Aturdir", 10, 0, "black", efecto={"nombre": "aturdido", "duracion": 3, "efectividad": 0.2})

# Ítems de prueba
potion = Item("Potion", "potion", "Heals 50 HP", 50)

# Ítems con efectos de estado
bomba_toxica = Item("B.Tóxica", "attack", "Aplica veneno", 0, efecto={"nombre": "veneno", "duracion": 5, "potencia": 80})
granada_sonica = Item("G.Sónica", "attack", "Aplica aturdimiento", 0, efecto={"nombre": "aturdido", "duracion": 3, "efectividad": 0.2})

# Jugadores de prueba
player1 = Person("Zack:", 3000, 400, 8000, 70, [fire, cure, veneno], [{"item": potion, "quantity": 5}, {"item": bomba_toxica, "quantity": 3}], "no")
player2 = Person("Leon:", 3000, 400, 900, 70, [fire, aturdir], [{"item": granada_sonica, "quantity": 2}], "no")
player3 = Person("Sora:", 3000, 400, 110, 70, [cure], [{"item": potion, "quantity": 5}], "no")

# Llamada al combate con los datos simulados
iniciar_combate([player1, player2, player3], [fire, cure, veneno, aturdir], [{"item": potion, "quantity": 5}])

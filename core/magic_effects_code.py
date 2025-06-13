from core.spell import Spell

# Nuevos hechizos con efectos de estado
veneno = Spell("Toxico", 15, 0, "black", efecto={"nombre": "veneno", "duracion": 5, "potencia": 80})
aturdir = Spell("Aturdir", 10, 0, "black", efecto={"nombre": "aturdido", "duracion": 3, "efectividad": 0.2})
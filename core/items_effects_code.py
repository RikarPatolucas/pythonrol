from core.item import Item
# Nuevos ítems con efectos
bomba_toxica = Item("B.Tóxica", "attack", "Aplica veneno", 0, efecto={"nombre": "veneno", "duracion": 5, "potencia": 80})
granada_sonica = Item("G.Sónica", "attack", "Aplica aturdimiento", 0, efecto={"nombre": "aturdido", "duracion": 3, "efectividad": 0.2})
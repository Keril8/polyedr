#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

tk = TkDrawer()
try:
    for name in ["cube", "ccc", "cube", "box", "king"]: # ["cube", "ccc", "cube", "box", "king"]
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        # Создаем экземпляр полиэдра и сохраняем его в переменную
        polyedr = Polyedr(f"data/{name}.geom")

        # Рисуем полиэдр
        polyedr.draw(tk)
        delta_time = time() - start_time
        print(f"Сумма длин проекций чстично видимых: "
              f"{Polyedr.calculate(polyedr)}")
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()

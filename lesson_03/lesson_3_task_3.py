from adress import Address
from mail import Mailing


to_address = Address(235437, "Murom", "Moskovskay", 76, 2)
from_address = Address(246768, "Moscow", "Pushkina", 185, 44)

pompa = Mailing(to_address, from_address, 1500, "TY12245465U")

print(f"Отправление {pompa.track} из {pompa.from_address} в "
      f"{pompa.to_address}. Стоймость {pompa.cost} рублей")

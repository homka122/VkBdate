import vk_api
from prettytable import PrettyTable

vk_session = vk_api.VkApi(login="ЛОГИН", password="ПАРОЛЬ")
vk_session.auth()
vk = vk_session.get_api()
info = vk.friends.get(order="name", fields="bdate")

table = PrettyTable(["Имя", "Фамилия", "Дата рождения"])
table2 = PrettyTable(["Имя", "Фамилия"])

for k in info["items"]:
    if ("bdate" in k):
        table.add_row([k["first_name"], k["last_name"], k["bdate"]])
    else:
        table2.add_row([k["first_name"], k["last_name"]])

print("ДРУЗЬЯ, ДР КОТОРЫХ ИЗВЕСТНО:\n")
print(table)
print("\n\nДРУЗЬЯ, ДР КОТОРЫХ НЕИЗВЕСТНО\n")
print(table2)

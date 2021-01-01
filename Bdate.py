import vk_api
from prettytable import PrettyTable

login = "Ваш Логин"
password = "Ваш Пароль"
table = PrettyTable(["Имя", "Фамилия", "Дата рождения"])
table2 = PrettyTable(["Имя", "Фамилия"])

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()
info = vk.friends.get(order="name", fields="bdate")

for k in info["items"]:
    if ("bdate" in k):
        table.add_row([k["first_name"], k["last_name"], k["bdate"]])
    else:
        table2.add_row([k["first_name"], k["last_name"]])

print("Друзья, др которых известно:\n")
print(table)
print("\n\nДрузья, др которых неизвестно\n")
print(table2)

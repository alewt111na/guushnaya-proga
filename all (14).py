a = input()

match a:
    case "старт":
        print("запуск")
    case "стоп":
          print("остановка")
    case _:
        print("неизвестная команда")
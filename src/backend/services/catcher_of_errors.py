# class Catcher_Of_Errors:
#     def pattern_of_catcher(self,url, httpcode):
#         try:
#             urlopen(f"{url}")
#         except HTTPError as err:
#             if err.code == httpcode:
#                 return f"Ошибка номер {httpcode}, попробуйте заново"
#             else:
#                 return False
from typing import Sequence


def result_not_found[
    T
](result: T | Sequence[T] | None, message: str = "not found") -> str | T | Sequence[T]:
    return message if result == None else result


audience_not_found: str = (
    "Аудитории по запрошеному Id не было найдено пожалуйста попробуйте другой или создайте новый"
)
reservation_not_found: str = (
    "Бронирования по запрошеному Id не было найдено пожалуйста попробуйте другой или создайте новый"
)
user_not_found: str = (
    "Пользователь по запрошеному Id не был найден пожалуйста попробуйте другой или создайте новый"
)

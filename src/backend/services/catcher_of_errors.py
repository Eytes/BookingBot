# class Catcher_Of_Errors:
#     def pattern_of_catcher(self,url, httpcode):
#         try:
#             urlopen(f"{url}")
#         except HTTPError as err:
#             if err.code == httpcode:
#                 return f"Ошибка номер {httpcode}, попробуйте заново"
#             else:
#                 return False
async def Not_found(res, message):
    if await res == None:
        return await message
    else:
        return await res


audience_not_found: str = (
    "Аудитории по запрошеному Id не было найдено пожалуйста попробуйте другой или создайте новый"
)
reservation_not_found: str = (
    "Бронирования по запрошеному Id не было найдено пожалуйста попробуйте другой или создайте новый"
)
user_not_found: str = (
    "Пользователь по запрошеному Id не был найден пожалуйста попробуйте другой или создайте новый"
)

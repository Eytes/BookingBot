# class Catcher_Of_Errors:
#     def pattern_of_catcher(self,url, httpcode):
#         try:
#             urlopen(f"{url}")
#         except HTTPError as err:
#             if err.code == httpcode:
#                 return f"Ошибка номер {httpcode}, попробуйте заново"
#             else:
#                 return False
def Not_found(res, string):
    if res != None:
        return res
    else:
        return string

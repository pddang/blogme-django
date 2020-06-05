from rest_framework.exceptions import APIException

class ProfileDoesNotExist(APIException):
    status_code = 400
    default_detail = "The request profile does not exist!"

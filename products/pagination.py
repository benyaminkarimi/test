from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


ADMIN_PAGE_SIZE = 1000
USER_PAGE_SIZE = 100

class AdminPagination(PageNumberPagination):
    page_size = ADMIN_PAGE_SIZE

class UserPagination(PageNumberPagination):
    page_size = USER_PAGE_SIZE

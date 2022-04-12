from rest_framework.pagination import PageNumberPagination

class BassPagination(PageNumberPagination):
    page_size = 3;
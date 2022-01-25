from rest_framework.pagination import PageNumberPagination


class ApiPagination(PageNumberPagination):
    page_size = 6


class CustomUserPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = "limit"

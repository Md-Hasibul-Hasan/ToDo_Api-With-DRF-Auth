from rest_framework.pagination import PageNumberPagination

class TodoPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'page'
    last_page_strings = ['last', 'end']

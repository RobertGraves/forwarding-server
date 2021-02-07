from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
class StandardResultsSetPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        response = super(StandardResultsSetPagination, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size=1000000

from rest_framework.pagination import PageNumberPagination


class CustomizedPagination(PageNumberPagination):
    # 默认页面大小
    page_size = 5
    # 页面大小对应的查询参数
    page_size_query_param = 'size'
    # 页面大小的最大值
    max_page_size = 50
form asyncio_http import AsyncioHttp


def main():

    url = "https://xxxx.xxx.xxx.xxx/zabbix/api_jsonrpc.php"
    header = {
        "Content-Type": "application/json"
    }

    http_method = "post"

    request_body_1 = '''{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "OOOOOOOOO", "password": "XXXXXXXXXX"}, "id":1, "auth": null}'''
    request_body_2 = '''{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "OOOOOOOOO", "password": "XXXXXXXXXX"}, "id":1, "auth": null}'''
    request_body_3 = '''{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "OOOOOOOOO", "password": "XXXXXXXXXX"}, "id":1, "auth": null}'''
    request_body_4 = '''{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "OOOOOOOOO", "password": "XXXXXXXXXX"}, "id":1, "auth": null}'''
    request_body_5 = '''{"jsonrpc": "2.0", "method": "user.login", "params": {"user": "OOOOOOOOO", "password": "XXXXXXXXXX"}, "id":1, "auth": null}'''

    requests = [request_body_1, request_body_2, request_body_3, request_body_4, request_body_5]

    chunk_number = 3

    asyncio_http_obj = AsyncioHttp(endpoint_url=url, header=header, http_method=method, requests=requests, chunk_number=chunk_number)

    print(asyncio_http_obj.get_query_result())


if __name__ == '__main__':
    main()

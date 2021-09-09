from elasticsearch import Elasticsearch

def es_search_all(es, index_name, query, scroll_range="10m", size=10000, request_timeout=300):
    # とりあえず一回検索しとかなあかんっぽい？
    response = es.search(scroll=scroll_range,
                         index=index_name, 
                         body=query,
                         size=size,
                         request_timeout=request_timeout
                        )

    # スクロールIDなるものを取得
    sid = response['_scroll_id']

    # スクロールサイズなるものを取得
    scroll_size = len( response['hits']['hits'] )

    result = []
    while True:
        # スクロールサイズ 0 だったら終了
        if scroll_size <= 0:
            break

        # 検索結果を処理
        for i in response['hits']['hits']:
            result.append(i)

        # スクロールから次の検索結果取得
        response = es.scroll(scroll_id=sid, scroll=scroll_range, request_timeout=request_timeout)
        scroll_size = len(response['hits']['hits'])
        
    return result

# 作成したインデックス一覧を見る
def show_es_indexs(es):
    return es.cat.indices(index="*", h="index").splitlines()

# indexの削除
def del_index(es, index_name):
    return es.indices.delete(index=index_name)

# indexのマッピングを表示
def show_mapping(es, index_name=None):
    return es.indices.get_mapping(index=index_name)
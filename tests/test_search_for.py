from TikTokApi import TikTokApi

def test_search_for():
    api = TikTokApi()
    assert len(api.search_for_hashtags('a')) >= 0
    assert len(api.search_for_music('a')) >= 0
    assert len(api.search_for_users('a')) >= 0
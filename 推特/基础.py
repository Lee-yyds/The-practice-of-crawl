import requests


headers = {
    "authority": "twitter.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs^%^3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "referer": "https://twitter.com/POTUS",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "x-csrf-token": "7af86473668729225a697732d85c765905896d69afe9d07aabc17c8ed18aac1209c99863a3afe0dcf7f93c519809ff8fa502b03e8fb711a416484508ee27d37313810637cad41645eb25d5dfa407132d",
    "x-twitter-active-user": "yes",
    "x-twitter-auth-type": "OAuth2Session",
    "x-twitter-client-language": "en"
}
cookies = {
    "guest_id_marketing": "v1^%^3A166314763164027752",
    "guest_id_ads": "v1^%^3A166314763164027752",
    "personalization_id": "^\\^v1_tCyTjnOhq3ZWYoPfUOKbmQ==^^",
    "guest_id": "v1^%^3A166314763164027752",
    "gt": "1569981075669061632",
    "_ga": "GA1.2.661118113.1663147638",
    "_gid": "GA1.2.1288787211.1663147638",
    "g_state": "^{^\\^i_l^^:0^}",
    "kdt": "58GzyfuCcJsbYTKLgHojD1mgCGyJaaB6VBrSNTfv",
    "auth_token": "5d48b0ad05291ef2407c68dc3051cb8bf5d7231f",
    "ct0": "7af86473668729225a697732d85c765905896d69afe9d07aabc17c8ed18aac1209c99863a3afe0dcf7f93c519809ff8fa502b03e8fb711a416484508ee27d37313810637cad41645eb25d5dfa407132d",
    "twid": "u^%^3D1569981125216604163"
}
url = "https://twitter.com/i/api/graphql/q881FFtQa69KN7jS9h_EDA/UserTweets"
params = {
    "variables": "^%^7B^%^22userId^%^22^%^3A^%^221349149096909668363^%^22^%^2C^%^22count^%^22^%^3A40^%^2C^%^22cursor^%^22^%^3A^%^22HBaEgLHJn9LrxCsAAA^%^3D^%^3D^%^22^%^2C^%^22includePromotedContent^%^22^%^3Atrue^%^2C^%^22withQuickPromoteEligibilityTweetFields^%^22^%^3Atrue^%^2C^%^22withSuperFollowsUserFields^%^22^%^3Atrue^%^2C^%^22withDownvotePerspective^%^22^%^3Afalse^%^2C^%^22withReactionsMetadata^%^22^%^3Afalse^%^2C^%^22withReactionsPerspective^%^22^%^3Afalse^%^2C^%^22withSuperFollowsTweetFields^%^22^%^3Atrue^%^2C^%^22withVoice^%^22^%^3Atrue^%^2C^%^22withV2Timeline^%^22^%^3Atrue^%^7D",
    "features": "^%^7B^%^22responsive_web_graphql_timeline_navigation_enabled^%^22^%^3Afalse^%^2C^%^22unified_cards_ad_metadata_container_dynamic_card_content_query_enabled^%^22^%^3Afalse^%^2C^%^22dont_mention_me_view_api_enabled^%^22^%^3Atrue^%^2C^%^22responsive_web_uc_gql_enabled^%^22^%^3Atrue^%^2C^%^22vibe_api_enabled^%^22^%^3Atrue^%^2C^%^22responsive_web_edit_tweet_api_enabled^%^22^%^3Atrue^%^2C^%^22graphql_is_translatable_rweb_tweet_is_translatable_enabled^%^22^%^3Afalse^%^2C^%^22standardized_nudges_misinfo^%^22^%^3Atrue^%^2C^%^22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled^%^22^%^3Afalse^%^2C^%^22interactive_text_enabled^%^22^%^3Atrue^%^2C^%^22responsive_web_text_conversations_enabled^%^22^%^3Afalse^%^2C^%^22responsive_web_enhance_cards_enabled^%^22^%^3Atrue^%^7D"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
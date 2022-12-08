import json
import requests
from dm_pb2 import DmSegMobileReply
from google.protobuf.json_format import MessageToJson, Parse

b_web_cookie = "buvid3=B27193EE-7574-C77F-17BE-E70A7D3FEE1A45689infoc; b_nut=1670244645; i-wanna-go-back=-1; b_ut=7; b_lsid=5C8B3EDF_184E256E717; _uuid=DCD8103E3-D7FB-5C46-EAED-9DE747106C331056925infoc; buvid4=0C93BD52-8C5D-063D-29FD-EF4D76AA7DEC46850-022120520-TtI3cncwnbghqKUT6Tkp9w==; fingerprint=b4f484f66a6d0218cd109d1bf710c4c6; buvid_fp_plain=undefined; SESSDATA=dd44cc2e,1685796660,cd03f*c1; bili_jct=a0703d984f09a7721dd79b163e9e034e; DedeUserID=150336411; DedeUserID__ckMd5=f5abbbb765024669; buvid_fp=676daeca879cfda6f48cb7675045cf9a; nostalgia_conf=-1; innersign=1; CURRENT_FNVAL=4048; sid=5v5ptrdf; rpdid=|(J|Y|RlRlR)0J'uY~|kRR)J|"


def get_date_list():
    url = "https://api.bilibili.com/x/v2/dm/history/index?type=1&oid=168855206&month=2022-02"
    headers = {
        'cookie': b_web_cookie
    }
    response = requests.get(url, headers=headers)
    print(json.dumps(response.json(), ensure_ascii=False, indent=4))


def dm_real_time():
    url_real_time = 'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=168855206&pid=98919207&segment_index=1'
    resp = requests.get(url_real_time)

    DM = DmSegMobileReply()
    DM.ParseFromString(resp.content)
    data_dict = json.loads(MessageToJson(DM))
    # print(data_dict)
    list(map(lambda x=None: print(x['content']), data_dict.get('elems', [])))


def dm_history():
    url_history = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=862913601&date=2022-10-17'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'cookie': b_web_cookie
    }
    resp = requests.get(url_history, headers=headers)
    DM = DmSegMobileReply()
    DM.ParseFromString(resp.content)
    data_dict = json.loads(MessageToJson(DM))
    print(data_dict)
    # list(map(lambda x=None: print(x['content']), data_dict.get('elems', [])))


if __name__ == '__main__':
    # dm_real_time()
    # get_date_list()
    dm_history()

    pass

import fontTools.ttLib.sfnt
import requests
import json

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 目标站点
url = 'http://scxk.nmpa.gov.cn:81/xk/'
data = requests.get(url=url, headers=headers).text
with open('test.html', 'w', encoding='utf-8') as fp:
    fp.write(data)
    fp.close()

# 首页的url一直在改变导致无法使用爬虫爬取所有已登记企业的ID
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5F4LvOGf6iO_ALPvbEUgfQ6o2ovIWUWd20C3X7t1pFRU1Njt9h.RYyxwfYodaEMRjeMjlIIMPw.pU9w7gjputLQo8YtUbtwKEDNMwfm1ach6cCV5QK9bMazKh.eawtM0ed438c2lvnppAOOQK1P_EIAAa2T5omVd_ggBVGyXxshgXEq4sXzLoCZbVZe3x7e.ouCBmRjXBAJc.53OiXTQYVC7REMsOBrKbDrXPa_87gyN4owX9WbIA1Jel.ezUFWlJmNWOupolMGRppShZkTobYRAP1aebOH8zMIerBw88bVG&8X7Yi61c=4ud2GKJzmDvIatuIEYVd550KtlEvEIQLPoj711Y0WERTGBn0DXbmHJbe08BucPiEmUBBK.VBN_FR5CGsR1MOLDNXnOgFUyJmvOuEsiR0.57Y2K8lu2iF1yx60BXOHOUOq
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5wq.oTxAnvfgeJabyHtQet4wZ3.LqshsZUBH01ZjytycNbRizuR6GmQ3zlsKlXd.QizoXdZyfNXvFRthytloU1dqE8.eS7KJOQwzFpJsVFJ67aqZX.v91yrA4gSP7tLZK7T7ANdtl0il3yoilDGtDk0DAQKvctGBPqq1_jCpChYI3ZzIeIur6.6tgkMgxBVFhkPtHe54G25gIHmT91DCkzMOy5bb4X22SOxsTDYN7J5NpLLwWUeIn_h9kEzcCaXeKNuljm3Xb7N.KTTZ2RuNp9uEfWLEjucLDKnnUDX4KQrE&8X7Yi61c=4DNZAyLtTh0SOjcvC553cJHEMxdAVEQ0Sk422qzCKB4QXjb2uS4EO4IUscTxPSDp0MRngzWPLEwK_4q7K2PbUJNmmt5ZEqhnPzreICTlMJM1Nz9_r533Ju4jTLhfmuqZ.

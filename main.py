import requests,datetime
response=requests.get("https://www.36jxs.com/api/Commonweal/almanac",{ "sun": datetime.date.today()})
data=response.json()['data']
def get(s):
	if data[s]=='':
		return "暂无数据"
	else:
		return data[s]
with open('almanac.txt','w',encoding='utf-8') as f:
	print("＋－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－＋",file=f)
	print("＋公历日期时间：{ymdgeoti}　节假日　农历日期时间：{ymdchnti}＋".format(ymdgeoti=get('GregorianDateTime'),ymdchnti=get('LunarDateTime')),file=f)
	print("＋农历节日：{chnday}　　{tdy}年{tdm}月{tdd}日　公历节日：{geoday}＋".format(chnday=get('LJie'),geoday=get('GJie'),tdy=get('TianGanDiZhiYear'),tdm=get('TianGanDiZhiMonth'),tdd=get('TianGanDiZhiDay')),file=f)
	print("＋宜：　　　　　　　　　　　{nlm}{nld}　　　　　　　　　　　忌：＋".format(nlm=get('LMonth'),nld=get('LDay')),file=f)
	print("＋{yi}　　　　　 {ji}＋".format(yi=get("Yi"),ji=get('Ji')),file=f)
	print("＋月相：{moon}　　　　　　生肖：{animal}　　　　　　　月名：{month}＋".format(moon=get('LunarShow'),animal=get('LYear'),month=get('MoonName')),file=f)
	print("＋　　　　　　　　　　　　　　神位：　　　　　　　　　　　　　＋",file=f)
	print("＋  {sw}   ＋".format(sw=get('ShenWei')),file=f)
	print("＋胎神：　                {ts}＋".format(ts=get('Taishen')),file=f)
	print("＋冲煞：{cs} 　　　　　　　　　　      岁煞：{ss}＋".format(cs=get('Chong'),ss=get('SuiSha')),file=f)
	print("＋五行甲子：{wx}　　　　　　　　　　　　　　　农历节气：{jq}＋".format(wx=get('WuxingJiazi'),jq=get('SolarTermName')),file=f)
	print("＋纳音五行年：{nyy}　　　　　　　　　　　　　黄历12值神建：{sj}＋".format(nyy=get('WuxingNaYear'),sj=get('JianShen')),file=f)
	print("＋纳音五行月：{nym}　　　　　        星宿吉凶：{xx}＋".format(nym=get('WuxingNaMonth'),xx=get('XingEast')),file=f)
	print("＋纳音五行日：{nyd}　　　　　　　　　　　　　　　星座：{xz}＋".format(nyd=get('WuxingNaDay'),xz=get('XingWest')),file=f)
	print("＋　　　　　　　　彭祖百忌：        {bj}　　　　＋".format(bj=get('PengZu')),file=f)
	print("＋－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－＋",end='',file=f)

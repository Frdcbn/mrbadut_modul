import requests,json,time
from os import system
import shutil,os
from time import sleep
from bs4 import BeautifulSoup as bs
from http.cookies import SimpleCookie
from tqdm import tqdm
from pyfiglet import figlet_format 
import pathlib
def animasi(menit):
  detik = menit * 60
  pattern_list = list("▁▃▅▇▅▃▁") * detik
  for i in range(detik):
      animasi = "".join(pattern_list[i:i+5])
      output = f"[{animasi}] - Please wait {detik//60:02d}:{detik%60:02d}"
      print(output, end='\r')
      time.sleep(1)
      detik -= 1
hijau1 = "\033[1;92m"#Terang
kuning1 = "\033[1;93m"#Terang
putih1 = "\033[1;97m"#Terang
merah1 = "\033[1;91m"#Terang
biru1 = "\033[1;94m"#Terang
def cache_control(name):
  main_folder = 'cache'
  sub_folder = name
  main_folder_path = pathlib.Path(main_folder)
  if not main_folder_path.exists():
      main_folder_path.mkdir()
  sub_folder_path = main_folder_path / sub_folder
  if not sub_folder_path.exists():
      sub_folder_path.mkdir()
def data_control(name):
  main_folder = 'data'
  sub_folder = name
  main_folder_path = pathlib.Path(main_folder)
  if not main_folder_path.exists():
      main_folder_path.mkdir()
  sub_folder_path = main_folder_path / sub_folder
  if not sub_folder_path.exists():
      sub_folder_path.mkdir()
def save_data(name):
      cookies=input(hijau1+'masukan cookies mu > ')
      user_agent=input(hijau1+'masukan User-Agent mu > ')
      data = {
          'cookies': cookies,
          'user_agent': user_agent
      }
      # Menyimpan data dalam format JSON
      with open(f'data/{name}/{name}.json', 'w') as file:
          json.dump(data, file)
def load_data(name):
      try:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          cookies = data['cookies']
          user_agent = data['user_agent']
          return cookies, user_agent
      except FileNotFoundError:
          return None, None
def btccanyon(modulesl,banner):
  system('clear')
  banner.banner("BTCCANYON")
  data_control('btccanyon')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/btccanyon/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('btccanyon')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://btccanyon.com/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://btccanyon.com/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/btccanyon/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://btccanyon.com/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data('btccanyon')
  if not os.path.exists("data/btccanyon/btccanyon.json"):
    save_data('btccanyon')
    btccanyon(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://btccanyon.com/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+biru1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data('btccanyon')
    btccanyon(modulesl,banner)
  print(hijau1+"> "+biru1+"Start working on ptc")
  get_ptc=curl.get('https://btccanyon.com/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://btccanyon.com/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
  del get_id[0]
  for _id in get_id:
   sesi=False
   while(sesi==False):
    _i=_id["onclick"].split("opensite('")[1].split("','")[0]
    key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
    get_reward=curl.get(f'https://btccanyon.com/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
    token1=get_reward.text.split("var token = '")[1].split("';")[0]
    secon=get_reward.text.split("var secs = ")[1].split(";")[0]
    for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
            time.sleep(1)
            pass
    answer=get_answer()
    reward=json.loads(curl.post('https://btccanyon.com/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
    if reward["status"] == 200:
      gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      sesi=True
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://btccanyon.com/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+biru1+"Start Bypassing Shortlinks")
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      providers = {
        'clks.pro': modulesl.clks_pro,
        'linksly.co': modulesl.linksly,
        'shrinkearn.com': modulesl.shrinkearn,
        'fc.lc': modulesl.fl_lc,
        'clk.sh': modulesl.clksh,
        'linksfly.me': modulesl.linksfly,
        'chainfo.xyz': modulesl.chainfo,
        'flyzu.icu': modulesl.flyzu,
        'adshorti.xyz': modulesl.adshorti_xyz,
        'usalink.io': modulesl.usalink,
        'birdurls.com': modulesl.birdurl,
        'owllink.net': modulesl.owlink,
        'clickzu.icu': modulesl.clickzu_icu,
        'zuba.link': modulesl.zuba_link,
        'mitly.us': modulesl.mitly,
        'illink.net': modulesl.illink_net,
        'exe.io': modulesl.exe_io,
        'insfly.pw': modulesl.insfly,
        'linkvor.pw': modulesl.linkvor_pw,
        'linkjust.com': modulesl.linkjust,
        'cashurl.win': modulesl.cashurl_win,
        'shorti.io': modulesl.shorti_io,
        'oii.io': modulesl.oii,
        'ex-foary.com': modulesl.ex_foary_com,
      }
      if any(provider in name for provider in providers):
        provider = next(provider for provider in providers if provider in name)
        for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
            get_sl = curl.get('https://btccanyon.com/shortlinks.html', headers=ua, cookies=cookies)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            status = True
            while(status==True):
                da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                get_lk = json.loads(curl.post('https://btccanyon.com/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                if get_lk["status"] == 200:
                    answer = providers[provider](get_lk['shortlink'])
                    if 'failed to bypass' in answer:
                        print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                    if answer:
                        try:
                            get_sl = curl.get(answer, headers=ua, cookies=cookies)
                            sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                            print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                            print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                        except:
                            print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                    break
                if get_lk['status'] == 600:
                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                else:
                  print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                  break
   except:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+biru1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://btccanyon.com/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LdzF6MlAAAAACcN9JGXW8tSs4dy1MjeKZKFJ11M',get_sl.url)
    g=json.loads(curl.post('https://btccanyon.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(600)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def claimlite(modulesl,banner):
  system('clear')
  banner.banner("CLAIMLITE")
  data_control('claimlite')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/claimlite/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('claimlite')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://claimlite.club/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://claimlite.club/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/claimlite/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://claimlite.club/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data('claimlite')
  if not os.path.exists("data/claimlite/claimlite.json"):
    save_data('claimlite')
    claimlite(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://claimlite.club/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+biru1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data('claimlite')
    claimlite(modulesl,banner)
  print(hijau1+"> "+biru1+"Start working on ptc")
  get_ptc=curl.get('https://claimlite.club/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://claimlite.club/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
 # del get_id[0]
  for _id in get_id:
   sesi=False
   while(sesi==False):
    _i=_id["onclick"].split("opensite('")[1].split("','")[0]
    key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
    get_reward=curl.get(f'https://claimlite.club/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
    token1=get_reward.text.split("var token = '")[1].split("';")[0]
    secon=get_reward.text.split("var secs = ")[1].split(";")[0]
    for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
            time.sleep(1)
            pass
    answer=get_answer()
    reward=json.loads(curl.post('https://claimlite.club/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
    if reward["status"] == 200:
      gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      sesi=True
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://claimlite.club/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+biru1+"Start Bypassing Shortlinks")
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      providers = {
        'clks': modulesl.clks_pro,
        'adshort': modulesl.adshorti_xyz,
        'ctr': modulesl.ctrsh,
        'ez4short': modulesl.ez4short,
        'usalink': modulesl.usalink,
        'bitads': modulesl.bitads,
        'shrinkme': modulesl.shrinkme,
        'chainfo': modulesl.chainfo,
        'cuty': modulesl.cuty_io,
        'exe': modulesl.exe_io,
        'oii': modulesl.oii,
        'try2link': modulesl.try2,
      }
      if any(provider in name for provider in providers):
        provider = next(provider for provider in providers if provider in name)
        for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
            get_sl = curl.get('https://claimlite.club/shortlinks.html', headers=ua, cookies=cookies)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            status = True
            while(status==True):
                da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                get_lk = json.loads(curl.post('https://claimlite.club/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                if get_lk["status"] == 200:
                    answer = providers[provider](get_lk['shortlink'])
                    if 'failed to bypass' in answer:
                        print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                    if answer:
                        try:
                            get_sl = curl.get(answer, headers=ua, cookies=cookies)
                            sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                            print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                            print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                        except:
                            print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                    break
                if get_lk['status'] == 600:
                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                else:
                  print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                  break
   except:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+biru1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://claimlite.club/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Leen-YUAAAAAFsd9t6qwRGyF8fLf6kixqicahQj',get_sl.url)
    g=json.loads(curl.post('https://claimlite.club/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(240)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def rushbitcoin(modulesl,banner):
  system('clear')
  banner.banner("RUSHBITCOIN")
  data_control('rushbitcoin')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/rushbitcoin/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('rushbitcoin')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://rushbitcoin.com/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://rushbitcoin.com/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/rushbitcoin/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://rushbitcoin.com/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data('rushbitcoin')
  if not os.path.exists("data/rushbitcoin/rushbitcoin.json"):
    save_data('rushbitcoin')
    rushbitcoin(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://rushbitcoin.com/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+biru1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data('rushbitcoin')
    rushbitcoin(modulesl,banner)
  print(hijau1+"> "+biru1+"Start working on ptc")
  get_ptc=curl.get('https://rushbitcoin.com/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://rushbitcoin.com/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
 # del get_id[0]
  for _id in get_id:
   try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://rushbitcoin.com/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://rushbitcoin.com/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data('rushbitcoin')
     rushbitcoin(modulesl,banner)
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://rushbitcoin.com/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+biru1+"Start Bypassing Shortlinks")
  websites = {
    'shrinkme.link': modulesl.shrinkme,
    'exe.io': modulesl.exe_io,
    'adshort.co': modulesl.adshorti_co,
    'Clks': modulesl.clks_pro,
    'Shrinlearn': modulesl.shrinkearn,
    'Adshorti': modulesl.adshorti_xyz,
  }
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
            if name in websites:
                for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
                    get_sl = curl.get('https://rushbitcoin.com/shortlinks.html', headers=ua, cookies=cookies)
                    token = get_sl.text.split("var token = '")[1].split("';")[0]
                    status = True
                    while status == True:
                        da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                        get_lk = json.loads(curl.post('https://rushbitcoin.com/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                        if get_lk["status"] == 200:
                            answer = websites[name](get_lk["shortlink"])
                            if "failed to bypass" == answer:
                                print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                            if "" == answer:
                                pass
                            else:
                                time.sleep(10)
                                get_sl = curl.get(answer, headers=ua, cookies=cookies)
                                try:
                                    sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                                    print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                                    print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                                except:
                                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                                status = False
                        if get_lk['status'] == 600:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                        else:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
    except:
        pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+biru1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://rushbitcoin.com/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LfokMEUAAAAAEwBx23jh3mlghwTF7VJqbN9fERK',get_sl.url)
    g=json.loads(curl.post('https://rushbitcoin.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(420)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def claimbits(modulesl,banner):
  system('clear')
  nama_host="claimbits"
  host="claimbits.net"
  banner.banner(nama_host.upper())
  data_control(''+nama_host+'')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/'+nama_host+f'/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control(nama_host)
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://'+host+f'/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/'+nama_host+'/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://'+host+'/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data(''+nama_host+'')
  if not os.path.exists('data/'+nama_host+'/'+nama_host+'.json'):
    save_data(nama_host)
    claimbits(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+biru1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(nama_host)
    claimbits(modulesl,banner)
  print(hijau1+"> "+biru1+"Start working on ptc")
  get_ptc=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
 # del get_id[0]
  for _id in get_id:
   try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://'+host+f'/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://'+host+'/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(nama_host)
     claimbits(modulesl,banner)
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+biru1+"Start Bypassing Shortlinks")
  websites = {
    'shrinkearn.com': modulesl.shrinkearn,
    'linksfly.me': modulesl.linksfly,
    'mitly.us': modulesl.mitly,
    'url.namaidani.com': modulesl.url_namaidani,
    'oii.io': modulesl.oii,
    'FC.LC': modulesl.fl_lc,
    'megaurl.in': modulesl.megaurl,
    'ExE': modulesl.exe_io,
    'ex-foary.com': modulesl.ex_foary_com,
    'clks.pro': modulesl.clks_pro,
    'adshort.co': modulesl.adshorti_co,
    'cuty.io': modulesl.cuty_io,
    'link1s.com': modulesl.links1s_com,
  }
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
            if name in websites:
                for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
                    get_sl = curl.get('https://'+host+'/shortlinks.html', headers=ua, cookies=cookies)
                    token = get_sl.text.split("var token = '")[1].split("';")[0]
                    status = True
                    while status == True:
                        da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                        get_lk = json.loads(curl.post('https://'+host+'/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                        if get_lk["status"] == 200:
                            answer = websites[name](get_lk["shortlink"])
                            if "failed to bypass" == answer:
                                print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                            if "" == answer:
                                pass
                            else:
                                time.sleep(10)
                                get_sl = curl.get(answer, headers=ua, cookies=cookies)
                                try:
                                    sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                                    print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                                    print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                                except:
                                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                                status = False
                        if get_lk['status'] == 600:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                        else:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
    except:
        pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+biru1+"Bypass faucet")
  while True:
   try:
    get_sl=curl.get('https://claimbits.net/faucet.html',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Lf6q3okAAAAAOO5I84xHj2g8cWRb-cNwsTnMHBa',get_sl.url)
    g=json.loads(curl.post('https://'+host+'/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
   except Exception as e:
     print('Cloudflare!!')
     save_data(nama_host)
     claimbits(modulesl,banner)
def ltchunt(modulesl,banner):
  system('clear')
  nama_host="ltchunt"
  host="ltchunt.com"
  banner.banner(nama_host.upper())
  data_control(''+nama_host+'')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/'+nama_host+f'/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control(nama_host)
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://'+host+f'/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/'+nama_host+'/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://'+host+'/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data(''+nama_host+'')
  if not os.path.exists('data/'+nama_host+'/'+nama_host+'.json'):
    save_data(nama_host)
    ltchunt(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+biru1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(nama_host)
    ltchunt(modulesl,banner)
  print(hijau1+"> "+biru1+"Start working on ptc")
  get_ptc=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
  del get_id[0]
  for _id in get_id:
   try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://'+host+f'/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://'+host+'/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(nama_host)
     ltchunt(modulesl,banner)
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+biru1+"Start Bypassing Shortlinks")
  websites = {
    'shortsfly.me': modulesl.shortfly,
    'flyzu.icu': modulesl.flyzu,
    'linksfly.me': modulesl.linksfly,
    'usalink.io': modulesl.usalink,
    'shortzu.icu': modulesl.shortzu_icu,
    'zuba.link': modulesl.zuba_link,
    'shorti.io': modulesl.shorti_io,
    'clk.sh': modulesl.clksh,
    'clickzu.icu': modulesl.clickzu_icu,
    'kiw.app': modulesl.kiw_app,
    'shrinkearn.com': modulesl.shrinkearn,
    'clks.pro': modulesl.clks_pro,
    'fc.lc': modulesl.fl_lc,
    'exe.io': modulesl.exe_io,
    'illink.net': modulesl.illink_net,
    'birdurls.com': modulesl.birdurl,
    'adshorti.xyz': modulesl.adshorti_xyz,
    'owllink.net': modulesl.owlink,
    'linksly.co': modulesl.linksly,
    'chainfo.xyz': modulesl.chainfo,
    'linkjust.com': modulesl.linkjust,
    'link1s.com': modulesl.links1s_com,
    'megaurl.io': modulesl.megaurl,
    'mitly.us': modulesl.mitly,
    'cashurl.win': modulesl.cashurl_win,
    'megafly.in': modulesl.megafly,
    'oii.io': modulesl.oii,
    'ex-foary.com': modulesl.ex_foary_com,
    'linkvor.pw': modulesl.linkvor_pw,
    'insfly.pw': modulesl.insfly,
  }
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
            if name in websites:
                for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
                    get_sl = curl.get('https://'+host+'/shortlinks.html', headers=ua, cookies=cookies)
                    token = get_sl.text.split("var token = '")[1].split("';")[0]
                    status = True
                    while status == True:
                        da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                        get_lk = json.loads(curl.post('https://'+host+'/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                        if get_lk["status"] == 200:
                            answer = websites[name](get_lk["shortlink"])
                            if "failed to bypass" == answer:
                                print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                            if "" == answer:
                                pass
                            else:
                                time.sleep(10)
                                get_sl = curl.get(answer, headers=ua, cookies=cookies)
                                try:
                                    sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                                    print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                                    print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                                except:
                                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                                status = False
                        if get_lk['status'] == 600:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                        else:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
    except:
        pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+biru1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://'+host+'/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Ld28FEkAAAAAHU7Z8ddeMVLzt4CAIzITn9g7ENZ',get_sl.url)
    g=json.loads(curl.post('https://'+host+'/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def coingax(modulesl,banner):
  system('clear')
  data_control('coingax')
  banner.banner('COINGAX')
  cookies, ugentmu = load_data('coingax')
  if not os.path.exists("data/coingax/coingax.json"):
    save_data('coingax')
    coingax(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"coingax.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dahs=curl.get('https://coingax.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dahs.text:
    save_data('coingax')
    coingax(modulesl,banner)
  fd=bs(dahs.text,'html.parser').find_all('div',{'class':'col-xl-3 col-lg-6 col-md-6 col-sm-6 col-xs-12'})
  print(hijau1+"> "+biru1+"Account information")
  for i in fd:
    print(hijau1+'> '+i.text.strip().splitlines()[0]+' : '+i.text.strip().splitlines()[1])
  link=curl.get('https://coingax.com/links',headers=ua,cookies=cookies)
  fd=bs(link.text,'html.parser').find_all('div',{'class':'col-md-6 col-lg-4 mb-3 mb-lg-0'})
  for li in fd:
   try:
    name=li.text.strip().splitlines()[0]
    jumlah=li.text.strip().splitlines()[6].split('Available ')[1].split('/')[0]
    if 'Cuty - Easy' in name:
      for i in range(int(jumlah)):
        link=li.find('a',{'class':'btn btn-success w-100'})['href']
        get_links=curl.get(link,headers=ua,cookies=cookies,allow_redirects=False).headers['Location']
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : '+get_links,end='\r')
        answer=modulesl.cuty_io(get_links)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass',end='\r')
        else:
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
          
    if 'Shortsfly - Mid' in name:
      for i in range(int(jumlah)):
        link=li.find('a',{'class':'btn btn-success w-100'})['href']
        get_links=curl.get(link,headers=ua,cookies=cookies,allow_redirects=False).headers['Location']
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : '+get_links,end='\r')
        answer=modulesl.shortfly(get_links)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass',end='\r')
        else:
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
    if 'Linksfly - Mid' in name:
      for i in range(int(jumlah)):
        link=li.find('a',{'class':'btn btn-success w-100'})['href']
        get_links=curl.get(link,headers=ua,cookies=cookies,allow_redirects=False).headers['Location']
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : '+get_links,end='\r')
        answer=modulesl.linksfly(get_links)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass',end='\r')
        else:
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
   except:
     pass
def claimsatoshi(modulesl,banner):
  system('clear')
  data_control('claimsatoshi')
  banner.banner('CLAIMSATOSHI')
  cookies, ugentmu = load_data('claimsatoshi')
  if not os.path.exists("data/claimsatoshi/claimsatoshi.json"):
    save_data('claimsatoshi')
    claimsatoshi(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"claimsatoshi.xyz",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://claimsatoshi.xyz/dashboard',headers=ua,cookies=cookies)
  if 'Current Balance' not in dash.text:
    save_data('claimsatoshi')
    claimsatoshi(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-xl-3 col-sm-6'})
  print(hijau1+"> "+biru1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[1]+' : '+info.text.strip().splitlines()[0])
  print(hijau1+"> "+biru1+"Start ptc")
  ptc=curl.get('https://claimsatoshi.xyz/ptc',headers=ua,cookies=cookies)
  surf=bs(ptc.text,'html.parser').find_all('div',{'class':'col-12 col-lg-4 mb-3 mb-lg-0'})
  for surf in surf:
    url=surf.find('button',{'class':'btn btn-one bg-dark btn-block'})['onclick'].split("window.location = '")[1].split("'")[0]
    name=surf.find('h2',{'class':'card-title'}).text.strip()
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    surf1=curl.get(url,headers=ua,cookies=cookies)
    sleep(int(surf1.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(surf1.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LduER0gAAAAAN1zeqcxdU3FxDAwgOI7PhMGUzR0',url)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(url.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
  print(hijau1+"> "+biru1+"Start shortlinks")
  gt_link = curl.get('https://claimsatoshi.xyz/links', headers=ua, cookies=cookies)
  gtf = bs(gt_link.text, 'html.parser')
  gt_info = gtf.find_all('div', {'class': 'col-12 col-lg-4 mb-3 mb-lg-0'})
  def process_link(link, bypass_function):
    try:
      lik = link.find('a')["href"]
      get_info = [i for i in link.text.strip().splitlines() if i]
      for i in range(int(get_info[4].split('/')[0].split('Claim ')[1])):
        get_lik = curl.get(lik, headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_lik,end='\r')
        answer = bypass_function(get_lik)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
        else:
          reward = curl.get(answer, headers=ua, cookies=cookies).text
          if 'Good job!' in reward:
            print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
          else:
            print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:
      pass
  for link in gt_info:
    if 'cbshort[Easy]' in link.text:
      process_link(link, modulesl.cbshort)
    elif 'Ez4short' in link.text:
      process_link(link, modulesl.ez4short)
    elif 'linksfly' in link.text:
      process_link(link, modulesl.linksfly)
    elif 'shortfly' in link.text:
      process_link(link, modulesl.shortfly)
    elif 'usalink' in link.text:
      process_link(link, modulesl.usalink)
    elif 'link1s' in link.text:
      process_link(link, modulesl.links1s_com)
    elif 'Shareus' in link.text:
      process_link(link, modulesl.cuty_io)
    elif 'Cuttyio' in link.text:
      process_link(link, modulesl.cuty_io)
    elif 'flyzu' in link.text:
      process_link(link, modulesl.flyzu)
    elif 'Shrinkearn' in link.text:
      process_link(link, modulesl.shrinkearn)
    elif 'droplink' in link.text:
      process_link(link, modulesl.droplink)
    elif 'Clksh' in link.text:
      process_link(link, modulesl.clksh)
    elif 'Hrshort' in link.text:
      process_link(link, modulesl.hrshort)
    elif 'Birdurls' in link.text:
      process_link(link, modulesl.birdurl)
    elif 'Owlink' in link.text:
      process_link(link, modulesl.owlink)
    elif 'Megaurl' in link.text:
      process_link(link, modulesl.megaurl)
    elif 'Mitly' in link.text:
      process_link(link, modulesl.mitly)
    elif 'link1snet' in link.text:
      process_link(link, modulesl.link1s_net)
  print(hijau1+"> "+biru1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://claimsatoshi.xyz/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(15)
    reward=curl.post('https://claimsatoshi.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except:
     break
     pass
  print(hijau1+"> "+biru1+"Start faucet")
  #<h2 class="card-title text-white">49/50</h2>
  ulang=bs(curl.get('https://claimsatoshi.xyz/faucet',headers=ua,cookies=cookies).text,'html.parser').find_all('h2',{'class':'card-title text-white'})
  ulang=ulang[len(ulang)-1].text.split('/')[0]
  for ulang in range(int(ulang)):
    faucet=curl.get('https://claimsatoshi.xyz/faucet',headers=ua,cookies=cookies)
    bs4 = bs(faucet.text, "html.parser")
    inputs = bs4.find_all("input")
    data = {input.get("name"): input.get("value") for input in inputs}
    data["captcha"]="recaptchav2"
    answer=modulesl.RecaptchaV2('6LduER0gAAAAAN1zeqcxdU3FxDAwgOI7PhMGUzR0',faucet.url)
    data["g-recaptcha-response"]=answer
    verify=curl.post('https://claimsatoshi.xyz/faucet/verify',data=data,headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"})
    if 'firewall' in verify.url:
      bs4 = bs(verify.text, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      data["captcha"]="recaptchav2"
      answer=modulesl.RecaptchaV2('6LduER0gAAAAAN1zeqcxdU3FxDAwgOI7PhMGUzR0',faucet.url)
      data["g-recaptcha-response"]=answer
      gas=curl.post('https://claimsatoshi.xyz/firewall/verify',data=data,headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"})
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
    animasi(5)
def coinfola(modulesl,banner):
  system('clear')
  data_control('coinfola')
  banner.banner('COINFOLA')
  cookies, ugentmu = load_data('coinfola')
  if not os.path.exists("data/coinfola/coinfola.json"):
    save_data('coinfola')
    coinfola(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"coinfola.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dahs=curl.get('https://coinfola.com/account',headers=ua,cookies=cookies)
  if 'Balance' not in dahs.text:
    save_data('coinfola')
    coinfola(modulesl,banner)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  print(hijau1+"> "+biru1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get('https://coinfola.com/shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+biru1+"Start bypass shortlinks")
  providers = {
    "Clks":modulesl.clks_pro,
    "Try2Link":modulesl.try2,
    "Clk":modulesl.clksh,
    "ShortsFly":modulesl.shortfly,
    "ShrinkEarn":modulesl.shrinkearn,
    "LinksFly":modulesl.linksfly,
    "Usalink":modulesl.usalink,
    "Chainfo":modulesl.chainfo,
    "Fclc":modulesl.fl_lc,
    "Shrinkme":modulesl.shrinkme,
    "Shorti":modulesl.shorti_io,
    "eXeio":modulesl.exe_io,
    "Cuty":modulesl.cuty_io,
    "AdBitFly":modulesl.adbitfly,
  }
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      for provider in providers:
          if provider in name:
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':'card shadow text-decoration-none text-dark'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://coinfola.com' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                      _1 = reward.text.split("message: 'You")[1].split("tickets.'")[0]
                      _2 = reward.text.split("message: 'Congratulations.")[1].split("credited.'")[0]
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+'Congratulations. ' + _2 + ' credited. & You ' + _1 + ' tickets.')
    except Exception as e:
      pass
def simpleads(modulesl,banner):
  system('clear')
  data_control('simpleads')
  banner.banner('SIMPLEADS')
  cookies, ugentmu = load_data('simpleads')
  if not os.path.exists("data/simpleads/simpleads.json"):
    save_data('simpleads')
    simpleads(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"simpleads.io",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  curl=requests.Session()
  dahs=curl.get('https://simpleads.io/account',headers=ua,cookies=cookies)
  if 'Balance' not in dahs.text:
    save_data('coinfola')
    simpleads(modulesl,banner)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  print(hijau1+"> "+biru1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get('https://simpleads.io/shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+biru1+"Start bypass shortlinks")
  providers = {
    "linksfly":modulesl.linksfly,
  }
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      for provider in providers:
          if provider in name:
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':'card shadow text-decoration-none text-dark'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://simpleads.io' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
    except Exception as e:
      pass
  print(hijau1+"> "+biru1+"Start bypass faucet")
  while True:
   try:
    faucet=curl.get('https://simpleads.io/faucet',headers=ua,cookies=cookies)
    csrf=bs(faucet.text,'html.parser').find('input',{'name':'csrfToken'})['value']
    answer=modulesl.RecaptchaV2('6Lee4w0kAAAAAEjQzK7OARMkmpiCf_9eOo9WFsHJ',faucet.url)
    data=f"csrfToken={csrf}&g-recaptcha-response={answer}"
    reward=curl.post(faucet.url,data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'success' in reward.text:
            print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
            animasi(3)
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1} Cloudflare!!')
     save_data('simpleads')
     simpleads(modulesl,banner)
def adhives(modulesl,banner):
  system('clear')
  data_control('adhives')
  banner.banner('ADHIVES')
  cookies, ugentmu = load_data('adhives')
  if not os.path.exists("data/adhives/adhives.json"):
    save_data('adhives')
    adhives(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"adhives.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dahs=curl.get('https://adhives.com/account',headers=ua,cookies=cookies)
  if 'Balance' not in dahs.text:
    save_data('adhives')
    adhives(modulesl,banner)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  print(hijau1+"> "+biru1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get('https://adhives.com/shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+biru1+"Start bypass shortlinks")
  providers = {
    "Linksfly":modulesl.linksfly,
    "Shortsfly":modulesl.shortfly,
    "Shrinkearn":modulesl.shrinkearn,
    "Clks":modulesl.clks_pro,
    "Fc":modulesl.fl_lc,
    "Cuty":modulesl.cuty_io,
    "Oii":modulesl.oii,
  }
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      for provider in providers:
          if provider in name:
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':'card shadow text-decoration-none text-dark'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://adhives.com' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
    except Exception as e:
      pass
def earnsolana(modulesl,banner):
  system('clear')
  data_control('earnsolana')
  banner.banner('EARNSOLANA')
  cookies, ugentmu = load_data('earnsolana')
  if not os.path.exists("data/earnsolana/earnsolana.json"):
    save_data('earnsolana')
    earnsolana(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"earnsolana.xyz",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://earnsolana.xyz/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data('earnsolana')
    earnsolana(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+biru1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+biru1+"Start ptc")
  ptc=curl.get('https://earnsolana.xyz/ptc',headers=ua,cookies=cookies)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6Lem2pIjAAAAAESScDYn7ChChD9JS7pqa0d7TUUL',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except:
        pass
  print(hijau1+"> "+biru1+"Start bypass shortlinks")
  get_links=curl.get('https://earnsolana.xyz/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
            'ShrinkEarn': modulesl.shrinkearn,
            'ShrinkMe': modulesl.shrinkme,
            'Ez4Short': modulesl.ez4short,
            'LinksFly': modulesl.linksfly,
            'ShortsFly.me': modulesl.shortfly,
            'Usalink': modulesl.usalink,
            'LinksLy': modulesl.linksly,
            'Clks.pro': modulesl.clks_pro,
        }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except:
        pass
  print(hijau1+"> "+biru1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://earnsolana.xyz/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(30)
    reward=curl.post('https://earnsolana.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     exit()
def claim_ro(modulesl,banner):
  system('clear')
  data_control('claim_ro')
  banner.banner('CLAIM_RO')
  cookies, ugentmu = load_data('claim_ro')
  if not os.path.exists("data/claim_ro/claim_ro.json"):
    save_data('claim_ro')
    claim_ro(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"claimro.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://claimro.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data('claim_ro')
    claim_ro(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+biru1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+biru1+"Start ptc")
  ptc=curl.get('https://claimro.com/ptc',headers=ua,cookies=cookies)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LdAqlAgAAAAAGqPveMFEw3mhkHDVh-rOdyclZAQ',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except:
        pass
  print(hijau1+"> "+biru1+"Start bypass shortlinks")
  get_links=curl.get('https://claimro.com/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
            'ctr.sh': modulesl.ctrsh,
            'fc.lc': modulesl.fl_lc,
            'birdsurl': modulesl.birdurl,
            'linksfly': modulesl.linksfly,
            'shortsfly': modulesl.shortfly,
            'clk.sh': modulesl.clksh,
            'owllink': modulesl.owlink,
            'shrinkearn': modulesl.shrinkearn,
            'insfly': modulesl.insfly,
            'clks.pro': modulesl.clks_pro,
        }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except:
        pass
def btcadspace(modulesl,banner):
  system('clear')
  data_control('btcadspace')
  banner.banner('BTCADSPACE')
  cookies, ugentmu = load_data('btcadspace')
  if not os.path.exists("data/btcadspace/btcadspace.json"):
    save_data('btcadspace')
    btcadspace(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"btcadspace.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://btcadspace.com/account',headers=ua,cookies=cookies)
  if 'Main Balance' not in dash.text:
    save_data('btcadspace')
    btcadspace(modulesl,banner)
  fd=bs(dash.text,'html.parser').find_all('div',{'class':'col-md-4 stretch-card grid-margin mt-3'})
  print(hijau1+"> "+biru1+"Account information")
  for i in fd:
    print(hijau1+'> '+i.text.strip().replace('    ','').splitlines()[0]+' : '+i.text.strip().replace('    ','').splitlines()[1])
  print(hijau1+"> "+biru1+"Bypass shortlinks")
  get_links=curl.get('https://btcadspace.com/shortlinks',headers=ua, cookies=cookies)
  gas=bs(get_links.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  methods = {
    'Linksfly': modulesl.linksfly,
    'Shortsfly': modulesl.shortfly,
    'Ctr': modulesl.ctrsh,
    'Usalink': modulesl.usalink,
    'Cuty': modulesl.cuty_io,
    'Clks': modulesl.clks_pro,
    'Shrinkearn': modulesl.shrinkearn,
    'Bitads': modulesl.bitads,
  }
  for i in gas:
      info = [i for i in i.text.strip().replace('            ', '').splitlines() if i]
      jumlah = info[2].split(' clicks remaining')[0]
      for method, bypass_func in methods.items():
        try:
          if method in info[0]:
              for jun in range(int(jumlah)):
                  url = curl.get('https://btcadspace.com' + i.find('a', {'class': 'card shadow text-decoration-none text-dark'})['href'], headers=ua, cookies=cookies, allow_redirects=False).headers['location']
                  answer = bypass_func(url)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  else:
                      get_reward = curl.get(answer, headers=ua, cookies=cookies)
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("message: '")[1].split("'")[0])
        except Exception as e:
          pass
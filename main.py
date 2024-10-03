import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6,et;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 'HSID=ArLXA6SuenrClC1a0; SSID=A5ezAa_voFZnP2ywO; APISID=je04JBQpqEqM-2HJ/A7SJ-lK0ePGgWLZz3; SAPISID=nUbB68VqoKWCjBc2/AAIWIIQVUhAU7e4Zv; __Secure-1PAPISID=nUbB68VqoKWCjBc2/AAIWIIQVUhAU7e4Zv; __Secure-3PAPISID=nUbB68VqoKWCjBc2/AAIWIIQVUhAU7e4Zv; receive-cookie-deprecation=1; __Secure-BUCKET=CM0B; SID=g.a000nwiZOmlRjCZ1WfbkKGQR1UZhrSkSKSLvHYa_kQU1UAhIHIZ5sBRcHC-kc_O0gWtIZtqNeAACgYKAVMSARISFQHGX2MiwbJjlL65MdpPAo1wgSjpThoVAUF8yKpic-KODII11Mg1xwFeuOl80076; __Secure-1PSID=g.a000nwiZOmlRjCZ1WfbkKGQR1UZhrSkSKSLvHYa_kQU1UAhIHIZ5g52ugYgn7LnqLYcpSrFZkgACgYKAZQSARISFQHGX2MiH07vT9g1HChyPQzQe_EzHRoVAUF8yKpjFPHhb5g-4qFGBwyOgroN0076; __Secure-3PSID=g.a000nwiZOmlRjCZ1WfbkKGQR1UZhrSkSKSLvHYa_kQU1UAhIHIZ5IncT3bBsZ9Jkv0-Ff5ZpeQACgYKAcsSARISFQHGX2Miy8aKizhewrTmcEvdq_1xgRoVAUF8yKryRzkNRKkeUHdeeMY2C_4p0076; SEARCH_SAMESITE=CgQInZwB; AEC=AVYB7cq3PHCis1wE--SfophDyjXpfR9GA9jy0QEklxg9bpadILuzBavu5A; NID=518=Qaq_-9mAkeNNQ7YdIUjAZsXj_lriMJPah---s_huKoEJFsgm62RmQqIYxtQLNcg4s0d-Tr6kzKnPz4buHK2AfNFpZSworpzVsyHCCTVtZacuin3DoFU0CXJ3G7PcsPXAFrkTKACa_Y_0WRwF1B9qGMSwQlJlTzeIxMTxvFIPPzAUt8J9pdt4wh9oc22KDuZkUkMDuaMB_P9sUSL8dcueJ0y_9i4I_QiWRpQJC8WsXUd7ipmLOhNWe8rozoo365nVjJlDeJCCbNDISJUtuVD5UOLzDLwgDNi7YOcxdS04_1ROz02o7d3vYWv2iyv6kLN_ci2QFN8KCBgVdD4R6ggqyyYFpMbvIx515fE-qr8XU4k5vT3r2jOrDriZSUcmMwwT8Q; __Secure-1PSIDTS=sidts-CjEBQlrA-Pz9GkkvPH6FU2vMOqnSzyPYjGFo7RztxkNvHWzOQ4TbdGDqRjPWD758A7Y-EAA; __Secure-3PSIDTS=sidts-CjEBQlrA-Pz9GkkvPH6FU2vMOqnSzyPYjGFo7RztxkNvHWzOQ4TbdGDqRjPWD758A7Y-EAA; SIDCC=AKEyXzXM3sbHClJ-2mx-1Q-9LR2W8DV9XPgTth9MI1e2LVooqv9685qIIb1KhjtCieAK6vbTFvc; __Secure-1PSIDCC=AKEyXzWuIx7beo5yQoM1tR3fwB0e8RfioibDp0sba9VmGrNIfX3oK0J6iXLWpdp759UzUpk1wA; __Secure-3PSIDCC=AKEyXzWHXQjHeGUuESej40bk4nXMsYUS570PfuC1ykeWWyY31a0PQk0rzf10DbL9hW7D9rQR_g',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-form-factors': '"Desktop"',
    'sec-ch-ua-full-version': '"127.0.6533.100"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.100", "Chromium";v="127.0.6533.100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.3.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    # 'x-client-data': 'CIy2yQEIo7bJAQipncoBCK3cygEIk6HLAQj/mM0BCIagzQEIi6jOAQjlr84BCLaxzgEIpbLOAQjAts4BCNq3zgEYoJ3OARidsc4B',
}

params = {
    'q': 'python',
}

response = requests.get('https://www.google.com/search', params=params, headers=headers)
a = 1
/Users/wyx/Documents/GIthub/google_search
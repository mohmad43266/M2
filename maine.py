import requests
import os

Almunharif_arab_countries_1A = {
    1: ("YE", "اليمن"),
    2: ("AE", "الإمارات العربية المتحدة"),
    3: ("BH", "البحرين"),
    4: ("DZ", "الجزائر"),
    5: ("EG", "مصر"),
    6: ("IQ", "العراق"),
    7: ("JO", "الأردن"),
    8: ("KW", "الكويت"),
    9: ("LB", "لبنان"),
    10: ("LY", "ليبيا"),
    11: ("MA", "المغرب"),
    12: ("OM", "عمان"),
    13: ("PS", "فلسطين"),
    14: ("QA", "قطر"),
    15: ("SA", "السعودية"),
    16: ("SD", "السودان"),
    17: ("SY", "سوريا"),
    18: ("TN", "تونس")
    19: ("TN", "ليبيا")
}

print("اختر الدولة:")
os.system('clear')
for Almunharif_num_X9, (Almunharif_code_Z6, Almunharif_country_Q2) in Almunharif_arab_countries_1A.items():
    print(f"{Almunharif_num_X9}: {Almunharif_country_Q2}")

Almunharif_country_num_Y4 = int(input("أدخل رقم الدولة من القائمة أعلاه: "))
os.system('clear')

if Almunharif_country_num_Y4 not in Almunharif_arab_countries_1A:
    print("رقم الدولة غير صحيح!")
else:
    Almunharif_country_code_V3, Almunharif_country_name_4D = Almunharif_arab_countries_1A[Almunharif_country_num_Y4]
    print(f"تم اختيار الدولة: {Almunharif_country_name_4D}")

    Almunharif_email_H9 = input("أدخل البريد الإلكتروني: ")
    os.system('clear')

    Almunharif_phone_number_L7 = input("أدخل رقم الهاتف: ")
    os.system('clear')

    Almunharif_url_T8 = 'https://www.whatsapp.com/contact/noclient/async/new/'
    Almunharif_headers_F1 = {
        'authority': 'www.whatsapp.com',
        'accept': '*/*',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'wa_lang_pref=ar; wa_ul=0ff4787b-96a8-4862-9185-6c96fcc58c63; wa_cb=1_2024_10_01_; wa_csrf=E0ARLIosEExWvpNVK-o8ju',
        'origin': 'https://www.whatsapp.com',
        'referer': 'https://www.whatsapp.com/contact/noclient?lang=ar_AR',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-asbd-id': '129477',
        'x-fb-lsd': 'AVq55ZW7b6U'
    }

    Almunharif_data_K5 = {
        'country_selector': Almunharif_country_code_V3,
        'email': Almunharif_email_H9,
        'email_confirm': Almunharif_email_H9,
        'phone_number': Almunharif_phone_number_L7,
        'platform': 'ANDROID',
        'your_message': 'Мой номер телефона был заблокирован, и я прошу вас рассмотреть возможность его разблокировки. Я всегда соблюдал правила использования приложения и надеюсь на ваше понимание.Заранее благодарю за помощь',
        'step': 'submit',
        '__user': '0',
        '__a': '1',
        '__req': '6',
        '__hs': '20001.BP:whatsapp_www_pkg.2.0..0.0',
        'dpr': '1',
        '__ccg': 'UNKNOWN',
        '__rev': '1017091165',
        '__s': 'a2ahpr:3ih36z:temqn5',
        '__hsi': '7422189115179150330',
        '__dyn': '7xeUmwkHg7ebwKBAg5S1Dxu13wqovzEdEc8uxa1twYwJw4BwUx60Vo1upE4W0OE2WxO0FE2aw7Bx61vw4iwBgao1aU2swaO4U2zxe0RE88co5G0zE5W0HUvw5rwSyES0gq0Lo6-1Fw4mwr81UU7u1rw',
        '__csr': '',
        'lsd': 'AVq55ZW7b6U',
        'jazoest': '2839'
    }

    Almunharif_response_R3 = requests.post(Almunharif_url_T8, headers=Almunharif_headers_F1, data=Almunharif_data_K5)
    print("تم إرسال الطلب:")

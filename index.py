from instagrapi import Client

# اطلاعات ورود
username = "fax.vpn"
password = "mstrman4"

cl = Client()
# cl.session.verify = False  # نادیده گرفتن SSL
# cl.request_timeout = 30  # افزایش تایم‌اوت
# try:
#     cl.login(username, password)
#     print("✅ با موفقیت لاگین شدی!")
# except Exception as e:
#     print(f"❌ خطا در لاگین: {e}")

cl.login(username, password)
post_url = "https://www.instagram.com/p/DDuOhypMv8z/?img_index=1"

def get_post_id(cl, url):
    shortcode = url.split("/")[-2]  # استخراج shortcode از URL
    media_id = cl.media_id(cl.media_pk_from_code(shortcode))
    return media_id

media_id = get_post_id(cl, post_url)

cl.media_like(media_id) 

# print(f"Media ID: {media_id}")



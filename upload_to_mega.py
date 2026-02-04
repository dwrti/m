import os
import sys
import requests
from mega import Mega

def transfer_to_mega():
    # التحقق من أنك وضعت رابط عند التشغيل
    if len(sys.argv) < 2:
        print("خطأ: لم يتم تزويد رابط للملف!")
        return

    url = sys.argv[1]
    filename = "video_file.mp4"

    # سحب الإيميل والباسورد من الخزنة (Secrets)
    email = os.environ.get('MEGA_EMAIL')
    password = os.environ.get('MEGA_PASSWORD')

    print(f"جاري تحميل الملف...")
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print("جاري الرفع إلى Mega...")
    mega = Mega()
    m = mega.login(email, password)
    file = m.upload(filename)
    link = m.get_upload_link(file)
    
    print(f"✅ تم الرفع! الرابط: {link}")
    
    if os.path.exists(filename):
        os.remove(filename)

if __name__ == "__main__":
    transfer_to_mega()

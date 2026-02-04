import os
import sys
import requests
from mega import Mega

def transfer_to_mega():
    # التحقق مما إذا كان المستخدم أدخل رابطاً
    if len(sys.argv) < 2:
        print("خطأ: لم يتم تزويد رابط للملف!")
        return

    url = sys.argv[1]
    filename = "downloaded_file.mp4" # يمكنك تحسين هذا لاستخراج الاسم من الرابط

    print(f"جاري تحميل: {url}")
    
    # عملية التحميل
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # تسجيل الدخول (يفضل استخدام الأسرار Secrets)
    mega = Mega()
    # استبدل بمفاتيحك أو استخدم os.environ
    m = mega.login("EMAIL", "PASSWORD") 

    print("جاري الرفع إلى Mega...")
    file = m.upload(filename)
    link = m.get_upload_link(file)
    
    print(f"تم الرفع بنجاح! الرابط الجديد: {link}")
    
    os.remove(filename)

if __name__ == "__main__":
    transfer_to_mega()

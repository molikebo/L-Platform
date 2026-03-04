from google import genai

import os



# إعداد الـ AI - ضع مفتاحك هنا

client = genai.Client(api_key="AIzaSyB6qRH_ytyq1_DYldHFFWQvrrn-DtOq_tM")



def create_article(topic):

    prompt = f"""

    اكتب مقالاً خبرياً قصيراً ومثيراً عن: {topic}.

    استخدم أسلوب الصحافة الفنية والتريند.

    أريد المخرجات بصيغة HTML بسيطة (فقط المحتوى الداخلي):

    - عنوان جذاب داخل <h1>

    - محتوى مشوق داخل <p>

    - وسوم مثل #تريند داخل <span>

    """

    

    # استخدام الموديل الجديد لعام 2026

    response = client.models.generate_content(

model="gemini-1.5-flash",

        contents=prompt

    )

    

    content = response.text

    

    # تنظيف اسم الملف من المسافات

    safe_topic = topic.replace(" ", "_")

    file_name = f"posts/{safe_topic}.html"

    

    # قالب الصفحة الرسمي باللون الأزرق السماوي

    template = f"""

    <!DOCTYPE html>

    <html lang="ar" dir="rtl">

    <head>

        <meta charset="UTF-8">

        <title>{topic} | L Platform</title>

        <style>

            body {{ 

                background: #0f1014; color: #f1f1f1; 

                font-family: 'Segoe UI', Tahoma; padding: 50px; 

                line-height: 1.8; max-width: 800px; margin: auto;

            }}

            h1 {{ color: #00b4d8; border-right: 5px solid #00b4d8; padding-right: 15px; }}

            p {{ font-size: 19px; color: #ccc; }}

            span {{ 

                color: #00b4d8; font-weight: bold; border: 1px solid #00b4d8; 

                padding: 4px 10px; border-radius: 4px; font-size: 14px;

            }}

            .back-btn {{ 

                display: inline-block; margin-top: 40px; color: #00b4d8; 

                text-decoration: none; font-weight: bold; border: 1px solid #00b4d8;

                padding: 10px 20px; border-radius: 5px;

            }}

            .back-btn:hover {{ background: #00b4d8; color: black; }}

        </style>

    </head>

    <body>

        {content}

        <a href="../index.html" class="back-btn">← العودة للمنصة الرئيسية</a>

    </body>

    </html>

    """

    

    # التأكد من وجود مجلد posts

    if not os.path.exists('posts'):

        os.makedirs('posts')

        

    with open(file_name, "w", encoding="utf-8") as f:

        f.write(template)

    

    print(f"\n✅ نجاح! تم إنشاء المقال في: {file_name}")



# تشغيل السكربت

print("--- L Platform AI Content Creator ---")

topic = input("أدخل موضوع الخبر اليوم: ")

create_article(topic)

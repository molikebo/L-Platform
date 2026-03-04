import os
from google import genai

# المفتاح الخاص بك
api_key = "AIzaSyB6qRH_ytyq1_DYldHFFWQvrrn-DtOq_tM" 

# التعديل: شلنا الـ v1 عشان المكتبة تختار النسخة المتوافقة لوحدها
client = genai.Client(api_key=api_key)

def create_article(topic):
    print(f"📝 جاري محاولة كتابة الخبر عن: {topic}...")
    
    # الطلب من الـ AI
    prompt = f"اكتب خبر فني قصير ومثير باللغة العربية عن {topic} بتنسيق HTML (عنوان h1 وفقرة p ووسم span للتريند)"
    
    try:
        # التعديل: جربنا نكتب اسم الموديل بدون أي مقدمات
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        # التأكد من وجود مجلد posts
        if not os.path.exists('posts'):
            os.makedirs('posts')
            
        # اسم الملف
        file_name = f"posts/{topic.replace(' ', '_')}.html"
        
        # القالب بتاعنا باللون الأزرق السماوي
        template = f"""
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ background: #0f1014; color: #f1f1f1; font-family: sans-serif; padding: 50px; text-align: center; }}
                h1 {{ color: #00b4d8; }}
                .content {{ background: #1a1c23; padding: 30px; border-radius: 15px; border: 1px solid #333; display: inline-block; text-align: right; max-width: 800px; }}
                a {{ color: #00b4d8; text-decoration: none; display: block; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="content">
                {response.text}
                <a href="../index.html">← العودة للمنصة الرئيسية</a>
            </div>
        </body>
        </html>
        """
        
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(template)
            
        print(f"✅ مبروووك! المقال اتعمل بنجاح في: {file_name}")

    except Exception as e:
        print(f"❌ لسه في مشكلة تقنية: {e}")

# التشغيل
if __name__ == "__main__":
    topic = input("أدخل موضوع الخبر: ")
    create_article(topic)

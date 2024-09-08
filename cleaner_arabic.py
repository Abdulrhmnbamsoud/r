import re
from nltk.corpus import stopwords
from pyarabic.araby import strip_tashkeel
from nltk.stem.isri import ISRIStemmer
import nltk

# تحميل كلمات التوقف للغة العربية
nltk.download('stopwords')
arabic_stopwords = set(stopwords.words('arabic'))

# دالة تنظيف النصوص العربية
def clean_text_arabic(text):
    # إزالة الروابط
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    
    # إزالة الأحرف الخاصة وعلامات الترقيم
    text = re.sub(r'\W+', ' ', text)
    
    # إزالة الأرقام
    text = re.sub(r'\d+', '', text)
    
    # تحويل الأحرف إلى أحرف صغيرة
    text = text.lower()
    
    # إزالة التشكيل
    text = strip_tashkeel(text)
    
    # إزالة كلمات التوقف للغة العربية
    text = ' '.join([word for word in text.split() if word not in arabic_stopwords])
    
    # تطبيق الترجمة (Stemming) باستخدام ISRIStemmer للعربية
    stemmer = ISRIStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    
    # إزالة المسافات الزائدة
    text = re.sub(r'\s+', ' ', text).strip()

    return text

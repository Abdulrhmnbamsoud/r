import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# تحميل كلمات التوقف للغة الإنجليزية
nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))

# دالة تنظيف النصوص الإنجليزية
def clean_text_english(text):
    # إزالة الروابط
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    
    # إزالة الأحرف الخاصة وعلامات الترقيم
    text = re.sub(r'[^\w\s]', '', text)  # الاحتفاظ بالأحرف والكلمات فقط
    
    # إزالة الأرقام
    text = re.sub(r'\d+', '', text)
    
    # تحويل الأحرف إلى أحرف صغيرة
    text = text.lower()

    # إزالة الأحرف غير الإنجليزية (الأحرف الغريبة مثل "å" و "ì_")
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    # إزالة كلمات التوقف للغة الإنجليزية
    text = ' '.join([word for word in text.split() if word not in english_stopwords])
    
    # إزالة الكلمات القصيرة جدًا (مثل "u", "nd")
    text = ' '.join([word for word in text.split() if len(word) > 2])
    
    # تطبيق الترجمة (Stemming) باستخدام PorterStemmer
    stemmer = PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    
    # إزالة المسافات الزائدة
    text = re.sub(r'\s+', ' ', text).strip()

    return text

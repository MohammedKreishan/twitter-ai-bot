
import tweepy
import schedule
import time
import os
from datetime import datetime
from dotenv import load_dotenv

# ==========================================
# تحميل المتغيرات من .env
# ==========================================

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# ==========================================
# التحقق من تحميل المفاتيح
# ==========================================

print("API_KEY loaded:", API_KEY is not None)
print("API_SECRET loaded:", API_SECRET is not None)
print("ACCESS_TOKEN loaded:", ACCESS_TOKEN is not None)
print("ACCESS_SECRET loaded:", ACCESS_SECRET is not None)

# ==========================================
# الاتصال بمنصة X
# ==========================================

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# ==========================================
# ملف تتبع التغريدات
# ==========================================

INDEX_FILE = "tweet_index.txt"

# ==========================================
# قائمة التغريدات
# ==========================================

tweets = [
    "Electric vehicles are not just transportation; they are a key part of the future energy ecosystem. #EV #ElectricalEngineering",
    "Battery management systems are essential for improving safety, efficiency, and battery lifespan in electric vehicles. #EV #BatteryTechnology",
    "Artificial Intelligence is transforming power systems through predictive maintenance and smart energy management. #AI #PowerSystems",
    "Renewable energy integration requires smarter electrical grids capable of handling dynamic power flows. #SmartGrid #RenewableEnergy",
    "Electrical engineers are helping drive the global transition toward sustainable transportation and clean energy. #Engineering #Energy",
    "Machine learning can significantly improve fault detection and diagnostics in electrical systems. #MachineLearning #Engineering",
    "Energy storage technologies will play a major role in the future of electrical power systems. #EnergyStorage #PowerSystems",
    "Hybrid vehicle research continues to bridge the gap between conventional and fully electric transportation. #HybridVehicles",
    "The future of power systems depends on digitalization, automation, and intelligent control strategies. #PowerSystems #AI",
    "Charging infrastructure remains one of the key challenges for accelerating EV adoption worldwide. #EV #Infrastructure",
    "Artificial intelligence can optimize charging schedules and reduce stress on power grids. #AI #SmartGrid",
    "Power electronics are the backbone of modern electric vehicles and renewable energy systems. #PowerElectronics",
    "Developing efficient battery technologies is critical for the next generation of electric vehicles. #BatteryTechnology #EV",
    "Smart grids enable better communication between utilities and consumers, improving reliability and efficiency. #SmartGrid",
    "Electrical engineering is evolving rapidly through AI, IoT, and advanced control systems. #Engineering #Technology",
    "Data-driven decision making is becoming increasingly important in modern power system operation. #DataScience #PowerSystems",
    "Combining AI with renewable energy can significantly improve energy forecasting accuracy. #AI #RenewableEnergy",
    "Electric vehicles are transforming both transportation and energy sectors simultaneously. #EV #CleanEnergy",
    "Predictive maintenance powered by AI can reduce downtime and operating costs in electrical systems. #AI #Engineering",
    "Modern engineers need strong knowledge of both hardware and software technologies. #ElectricalEngineering",
    "Vehicle-to-grid technology could become a major component of future energy management strategies. #V2G #EV",
    "Battery health estimation remains one of the most important research areas in EV development. #BatteryManagement",
    "Electrical engineering research increasingly combines power systems, AI, and data analytics. #Research",
    "The transition to sustainable energy requires innovation in generation, storage, and distribution technologies. #EnergyTransition",
    "Fast-charging technologies are improving the practicality of electric vehicles for everyday use. #EV",
    "Power quality and grid stability remain essential as renewable energy penetration continues to grow. #PowerSystems",
    "Future engineers must combine technical expertise with creativity and lifelong learning. #Engineering",
    "Research and development in electrical engineering continues to shape technologies that power modern society. #Research #Engineering",
    "Artificial intelligence is becoming a powerful tool for optimizing energy consumption and grid performance. #AI #Energy",
    "Electric mobility and smart energy systems will define the next generation of sustainable infrastructure. #EV #SmartGrid"
]

# ==========================================
# اختيار التغريدة التالية
# ==========================================

def generate_tweet():

    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "w") as f:
            f.write("0")

    with open(INDEX_FILE, "r") as f:
        index = int(f.read())

    tweet = tweets[index % len(tweets)]

    with open(INDEX_FILE, "w") as f:
        f.write(str(index + 1))

    return tweet

# ==========================================
# نشر التغريدة
# ==========================================

def post_tweet():

    try:

        tweet = generate_tweet()

        response = client.create_tweet(
            text=tweet
        )

        print("\n==============================")
        print("✅ Tweet Published Successfully")
        print("Time:", datetime.now())
        print("Tweet:")
        print(tweet)
        print("Response:")
        print(response)
        print("==============================\n")

    except Exception as e:

        print("\n❌ Publishing Failed")
        print(type(e))
        print(e)

        if hasattr(e, "response"):
            print(e.response.text)

# ==========================================
# تشغيل البوت
# ==========================================

if __name__ == "__main__":

    print("🚀 Twitter Bot Started")

    # نشر اختبار عند التشغيل
    post_tweet()

    # النشر اليومي الساعة 9 صباحاً
    schedule.every().day.at("09:00").do(post_tweet)

    print("📅 Daily posting scheduled at 09:00 AM")

    while True:
        schedule.run_pending()
        time.sleep(60)
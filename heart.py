# neon_love_heart.py (รวมโค้ดทั้งหมดในไฟล์เดียว)
import math
import random
import time
import turtle

# ==========================================
# 1. ข้อมูลคำบอกรักและฟังก์ชันคำนวณ (เดิมมาจาก love.py)
# ==========================================

PHRASES = [
    "I love you", "Seni seviyorum", "Te amo", "Ti amo", "Je t'aime",
    "Я тебя люблю", "Ich liebe dich", "Aku cinta kamu", "Kocham cię",
    "Jag älskar dig", "ฉันรักคุณ", "사랑해", "我爱你", "Anh yêu em"
]

def heart(t):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x, y

def fonts():
    size = random.randint(10, 18)
    return ("Arial", size, "bold")


# ==========================================
# 2. โค้ดหลักสำหรับวาดรูปหัวใจ (Neon Animation)
# ==========================================

# ตั้งค่าหน้าจอ
s = turtle.Screen()
s.setup(800, 800)
s.bgcolor("black")
s.title("Neon Love Heart - Sweep Animation")

# สร้างปากกาวาด
t_pen = turtle.Turtle()
t_pen.hideturtle()
t_pen.penup()
t_pen.speed(0)

# สร้างจุดตามมุม t ของสมการหัวใจ
points = []
num_points = 250

for i in range(num_points):
    t = (i / num_points) * (2 * math.pi)
    scale = random.uniform(10, 18)

    x, y = heart(t)
    x *= scale
    y *= scale

    text = random.choice(PHRASES)
    color = random.choice(["#ff0055", "#ff3300", "#ff66aa", "#ff0000", "#ffffff"])

    points.append({"x": x, "y": y, "text": text, "color": color, "font": fonts()})

# สั่งวาดทีละจุดตามลำดับการวนรอบรูปหัวใจ
for p in points:
    t_pen.goto(p["x"], p["y"])
    t_pen.color(p["color"])
    t_pen.write(p["text"], align="center", font=p["font"])

    time.sleep(0.000001)

s.mainloop()
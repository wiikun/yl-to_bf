import sys
with open(sys.argv[1],encoding="utf-8") as x:
    xstar=x.read()
tl = [("ヤッフー！","+"),("イェーイ！","-"),("ヤフー！",">"),("ウィッヒュー！","<"),("オー！","["),("マンマミーア！","]"),("レッツゴー！","."),("セーブする？",",")]
for i in tl:
    a,b = i
    xstar = xstar.replace(a,b)
with open(sys.argv[1].replace(".yl",".bf"), mode="w", encoding="utf-8") as f:
    f.write(xstar)
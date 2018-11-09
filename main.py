from PIL import Image, ImageDraw, ImageFont
import os, glob
import tkinter.messagebox
print("This program was created by Kim Woo Young (Xeros)",end="\n\n")
print("https://hackerxeros.tistory.com")
print("Version : 1.0.0")
print("몇퍼센트, 혹은 할인할 금액을 입력해주세요(Ex. 3% 또는 5000)")
saleprice = input("입력:")
target_image = Image.open('./data/src.png')
fontsFolder = './data'
selectedFont = ImageFont.truetype(os.path.join(fontsFolder,'font.ttf'),50)
draw = ImageDraw.Draw(target_image)
draw.text((16,30), saleprice, fill='green', font=selectedFont)
tkinter.messagebox.showinfo("완료", "프로그램이 위치한 경로에 result.png로 쿠폰 이미지를 저장했습니다")
target_image.save('./result.png')
os.system("result.png")
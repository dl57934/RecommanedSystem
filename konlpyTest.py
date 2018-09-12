from konlpy.tag import Twitter

testText = "콧대가 낮아서 콧대 섀딩용으로 섀도우를 사서 씁니다저번엔 더페이스샵껄 세일하길래 샀다" \
           "이번엔 홀리카가 세일해서 이걸 샀네요더페이스샵보다 가루가 더 고운거 같아요 살짝 찍어서 콧대 옆에 " \
           "쓸어주면 콧대가 생겨요땀만 안나면 지속력이 괜찮아서 여름 지나면 쓰려고 생각 중입니다 "

twitter = Twitter()
classificationText = twitter.pos(testText, norm=True, stem=True)

for i in classificationText:
    if i[1] not in ["Punctuation", "Eomi", "Josa"]:
        print(i[0])


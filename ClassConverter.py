def Label2Class(label) :
    # 0: person 1: 이동수단 2: 도로 3: 주방도구 4: 가방 5: 도구 6: 식품 7: 운동기구 8: 가구 9: 전자기기 10: 동물 11: 강아지 12: 고양이 13: 자동차 14: 새  15: 기타
    labelList = [[0],#사람
    [1,3,4,5,6,7,8],#이동수단
    [9,10,11,12,13],#도로
    [39,40,41,42,43,44,45],#주방도구
    [24,26,28],#가방
    [25,27,33,73,74,75,76,77,78,79],#도구
    [46,47,48,49,50,51,52,53,54,55],#식품
    [29,30,31,32,34,35,36,37,38],#운동기구
    [56,57,58,59,60,61,62,68,69,70,71,72],#가구
    [63,64,65,66,67],#전자기기
    [17,18,19,20,22,23],#동물
    [16,21],#강아지
    [15],#고양이
    [2],#자동차
    [14],#새
    [99]]#기타
    labelList_str = ["people","vehicle","road","kitchen","bag","tools","food","gym","furniture","electronic","animal","dog","cat","car","bird","none"]
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    check = 99
    for i in range(len(classes)) :
        if(label == classes[i]) :
            check = i
            break
    index = 16
    for i in range(len(labelList)) :
        if(check in labelList[i]) :
            index = i
            break
    return labelList_str[index]
    
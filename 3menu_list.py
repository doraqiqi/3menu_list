# Author：zhaoyanqi

info = {
    "北京":{
        "朝阳":[
            "国贸",
            "鸟巢",
            "水立方"
        ],
        "东城":[
            "火车站",
            "东便门",
            "广渠门"
        ],
        "海淀":[
            "西二旗",
            "月坛",
            "牡丹园"
        ]
    },
    "上海":{
        "静安":[
            "静安寺",
            "彭浦新村",
            "美琪大戏院"
        ],
        "黄埔":[
            "人民广场",
            "外滩",
            "淮海路"
        ],
        "杨浦":[
            "五角场",
            "复旦大学",
            "东外滩"
        ]
    },
    "香港":{
        "旺角":[
            "花园街",
            "信和中心",
            "庙街"
        ],
        "中环":[
            "置地广场",
            "中银大厦",
            "中环中心"
        ],
        "尖沙咀":[
            "海港城",
            "星光大道",
            "重庆大厦"
        ]
    }
}
while True:
    for i in info:
        print(i)
    choice = input("选择进入第一层，输入q退出：")
    if choice in info:

        while True:
            for i2 in info[choice]:
                print(i2)
            choice2 = input("选择进入第二层，输入q退出，输入b返回上一级：")
            if choice2 in info[choice]:
                while True:
                    for i3 in info[choice][choice2]:
                        print(i3)
                    choice3 = input("选择进入第三层，输入q退出，输入b返回上一级：")
                    if choice3 in info[choice][choice2]:
                        print("选择结束")
                        exit()
                    elif choice3 == "q":
                        exit()
                    elif choice3 == "b":
                        break
                    else:
                        print("选项不存在，请重新输入：")
            elif choice2 == "q":
                exit()
            elif choice2 == "b":
                break
            else:
                print("选项不存在，请重新输入：")
    elif choice == "q":
        exit()
    else:
        print("选项不存在，请重新输入：")

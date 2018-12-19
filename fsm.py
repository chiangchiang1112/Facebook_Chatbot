from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '開始'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你好！歡迎體驗兩分鐘歷史\n接下來你將扮演一名民國時期的有為青年，在國家動盪不安時做出你的決定，請小心的活下去")
        responese = send_text_message(sender_id, "接下來將說明規則，每次都會有幾個選項供你挑選，選擇一個喜歡的路線並繼續下去\n例如：你會選擇哪個？\n1.準時起床\n2.賴床一下\n3.睡過頭啦")
        responese = send_text_message(sender_id, "如果你選擇準時起床，請在對話框輸入 1 就可以了，這樣清楚了吧！")
        responese = send_text_message(sender_id, "另外旅程意外難免，你可以在得到結果後重新開始")
        responese = send_text_message(sender_id, "現在旅程即將展開，請輕鬆的選擇吧")
        responese = send_text_message(sender_id, "陽光灑下來，你從床上睡醒了，簡單的盥洗一下後，你...\n1.上課要來不及啦趕快出門\n2.坐在餐桌前悠閒的吃早餐\n3.帶著家人準備的便當盒出門")

    def on_exit_state1(self, event):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "上課真的好想睡覺啊，終於到了社團時間了，座位旁的同學問我要不要去社團...\n1.聽說讀書會可以遇到有趣的學長姐\n2.聽說烹飪社可以遇到厲害的學長姐")

    def on_exit_state2(self, event):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是李章瑞\n因為你參與的讀書會中有人被舉報為匪諜，無辜的你被牽連入獄，你得到的結果是...")
        send_text_message(sender_id, "有期徒刑15年，而後被改判為死刑")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/8/89/%E6%9D%8E%E5%BC%B5%E7%91%9E.jpg")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "噹噹噹，放學了，難得提早放學，去哪裡好呢\n1.圖書館看書\n2.老師的課後輔導")

    def on_exit_state4(self, event):
        print('Leaving state4')

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "在圖書館找書時看到自己的好朋友被一個怪人尾隨欸，我該上前嗎\n1.要阿，告訴朋友有怪人要小心\n2.別吧，假裝沒看到好了")

    def on_exit_state5(self, event):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是傅如芝\n沒有想到老師的課後輔導竟然是在講解民族自決的想法，不知情的你被認為有反叛思想，你得到的結果是...")
        send_text_message(sender_id, "有期徒刑10年，而後被改判為死刑")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/zh/b/b1/Fu_Ru_Zhi.jpg")
        self.go_back()

    def on_exit_state6(self):
        print('Leaving state6')

    def on_enter_state7(self, event):
        print("I'm entering state7")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是丁窈窕\n你因為建議朋友與怪人保持距離，生氣的他跑去檢舉你為匪諜，你得到的結果是...")
        send_text_message(sender_id, "死刑槍決")
        send_image_url(sender_id , "https://upload.wikimedia.org/wikipedia/commons/2/20/%E9%AB%98%E4%BA%8C%E6%99%82%E7%9A%84%E4%B8%81%E7%AA%88%E7%AA%95.jpg")
        self.go_back()

    def on_exit_state7(self):
        print('Leaving state7')

    def on_enter_state8(self, event):
        print("I'm entering state8")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "眼前的朋友發現我後突然走過來，並告知身邊有人不懷好意的在看我，我該怎麼辦\n1.朋友說說的而已應該沒關心吧\n2.聽朋友的跟怪人保持距離")

    def on_exit_state8(self, event):
        print('Leaving state8')

    def on_enter_state9(self, event):
        print("I'm entering state9")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "平安的一天又過去了，你感謝你自己做出明確的決定，你選擇明哲保身了自己，而其他人呢")
        send_text_message(sender_id, "想知道其他人怎麼了嗎，你可以選擇重新開始")
        self.go_back()

    def on_exit_state9(self):
        print('Leaving state9')

    def on_enter_state10(self, event):
        print("I'm entering state10")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是施水環\n聽從朋友的你選擇與追求者保持距離，而卻為你帶來一個無辜的匪諜做罪名，你得到的結果是...")
        send_text_message(sender_id, "死刑槍決")
        send_image_url(sender_id , "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Shih_Shui-Huan_1.jpg/220px-Shih_Shui-Huan_1.jpg")
        self.go_back()

    def on_exit_state10(self):
        print('Leaving state10')

    def is_going_to_state11(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state12(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state13(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state14(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state15(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state16(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '3'
        return False

    def is_going_to_state17(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state18(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state19(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state20(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def on_enter_state11(self, event):
        print("I'm entering state11")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "早餐旁放著一本雜誌和一份報紙，這時你突然有個念頭\n1.這本雜誌我很喜歡呢，贊助一點支持他們\n2.這份報紙我很喜歡呢，和家人討論其內容")

    def on_exit_state11(self, event):
        print('Leaving state11')

    def on_enter_state12(self, event):
        print("I'm entering state12")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是陳文成\n你關心的這本雜誌為美麗島雜誌，其內容被政府認為有顛覆國家的問題，有天軍隊在半夜闖進你家把你帶走，你得到的結果是...")
        send_text_message(sender_id , "刑求致死")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/zh/thumb/3/31/20120702.jpg/220px-20120702.jpg")
        self.go_back()

    def on_exit_state12(self):
        print('Leaving state12')

    def on_enter_state13(self, event):
        print("I'm entering state13")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "吃完早餐後，你回到自己的書房準備開始自己的一天\n1.撰寫一篇世界文學的評論文章\n2.撰寫一段詩詞去紀錄自己生活\n3.撰寫一封信件與朋友討論國家")

    def on_exit_state13(self, event):
        print('Leaving state3')

    def on_enter_state14(self, event):
        print("I'm entering state14")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是葉石濤\n你的文章太過於出色而被他人忌妒，因此被有心人士冠上知匪不報的罪名，你得到的結果是...")
        send_text_message(sender_id, "有期徒刑5年")
        send_image_url(sender_id , "https://nckulitterateur.files.wordpress.com/2012/04/feb2.jpg?")
        self.go_back()

    def on_exit_state14(self):
        print('Leaving state14')

    def on_enter_state15(self, event):
        print("I'm entering state15")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "做完這件事情後，你選擇出門走走，散步途中突然有兩個朋友叫住你，並希望請你幫一個忙\n1.幫忙朋友進行買賣\n2.幫忙朋友競選鎮長")

    def on_exit_state15(self, event):
        print('Leaving state15')

    def on_enter_state16(self, event):
        print("I'm entering state16")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是林樹枝\n你的信件被軍警人員抽查，他們對於你提及政府的內容很不滿意，於是請你來警局一趟，你得到的結果是...")
        send_text_message(sender_id, "有期徒刑15年")
        send_image_url(sender_id, "https://s.yimg.com/uu/api/res/1.2/xvuJLH0WbWcbAVp0hVB7RQ--~B/aD04MDA7dz01MzE7c209MTthcHBpZD15dGFjaHlvbg--/http://media.zenfs.com/zh_hant_tw/News/Reuters/20171210000019M.jpg")
        self.go_back()

    def on_exit_state16(self):
        print('Leaving state16')

    def on_enter_state17(self, event):
        print("I'm entering state17")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "面對這個被管控的社會，你有些心灰意冷，家人有些擔心你的狀況\n1.好好打起精神繼續生活\n2.好好振作一下繼續生活")

    def on_exit_state17(self,event):
        print('Leaving state17')

    def on_enter_state18(self, event):
        print("I'm entering state18")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是鄭再添\n朋友當選鎮長後你得到了鎮公所的總務課長位置，但是三個半月後警察在半夜將你帶走，並要你供出辦公室的匪諜，而你拒絕回答，你得到的結果是...")
        send_text_message(sender_id, "死刑")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/8/82/%E9%84%AD%E5%86%8D%E6%B7%BB_01.jpg")
        self.go_back()

    def on_exit_state18(self):
        print('Leaving state18')

    def on_enter_state19(self, event):
        print("I'm entering state19")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "平安的一天又過去了，你感謝你自己做出明確的決定，你選擇明哲保身了自己，而其他人呢")
        send_text_message(sender_id, "想知道其他人怎麼了嗎，你可以選擇重新開始")
        self.go_back()

    def on_exit_state19(self):
        print('Leaving state19')

    def on_enter_state20(self, event):
        print("I'm entering state20")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是崔小萍\n你遭人向警備總司令部舉發為匪諜，不知情的你含冤入罪，而舉發人可得到部份你家產，你得到的結果是...")
        send_text_message(sender_id, "有期徒刑9年")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/0/0a/Cui_Xiao-ping_in_high-heeled_shoes_and_Qipao.jpg")
        self.go_back()

    def on_exit_state20(self):
        print('Leaving state20')

    def is_going_to_state21(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '3'
        return False

    def is_going_to_state22(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state23(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state24(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state25(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state26(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state27(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state28(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state29(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state30(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state31(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def on_enter_state21(self, event):
        print("I'm entering state21")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "拿著便當盒的你出門了，今天陽光有點刺眼，你準備去工作地點，於是走向\n1.往軍營的公車站\n2.往學校的公車站")

    def on_exit_state21(self, event):
        print('Leaving state11')

    def on_enter_state22(self, event):
        print("I'm entering state22")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "今天政府又派督察過來盯人了，罵人的聲音感覺從未停過，壓力有些大的你選擇\n1.偷偷的跟屬下抱怨\n2.偷偷的在廁所塗鴉")

    def on_exit_state22(self,event):
        print('Leaving state22')

    def on_enter_state23(self, event):
        print("I'm entering state23")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "今天政府突然派人過來要求徵收民兵，要求中學生強制入伍，身為導師的你，你該怎麼辦\n1.面對軍方，勇敢保護學生\n2.面對軍方，選擇默不作聲")

    def on_exit_state23(self, event):
        print('Leaving state23')

    def on_enter_state24(self, event):
        print("I'm entering state24")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是歐陽劍華\n你隨口對屬下的抱怨，被傳出去給長官聽到了，而被檢舉你的思想不純正，你得到的結果是...")
        send_text_message(sender_id, "有期徒刑10年")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/zh/8/80/Ou_Yang_Jian_Hua.jpg")
        self.go_back()

    def on_exit_state24(self):
        print('Leaving state24')

    def on_enter_state25(self, event):
        print("I'm entering state25")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是謝東榮\n你在廁所寫下「軍隊是人民公社，大家要忍耐」，被檢舉書寫反動文字，這個突如其來的指控，你得到的結果是...")
        send_text_message(sender_id, "有期徒刑7年")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/%E8%AC%9D%E6%9D%B1%E6%A6%AE%E7%94%9F%E5%89%8D.jpg/800px-%E8%AC%9D%E6%9D%B1%E6%A6%AE%E7%94%9F%E5%89%8D.jpg")
        self.go_back()

    def on_exit_state25(self):
        print('Leaving state25')

    def on_enter_state26(self, event):
        print("I'm entering state26")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是張敏之\n你為了維護學生權益而勇敢向軍方交涉，如此英勇的下場，你得到的結果是...")
        send_text_message(sender_id, "槍決，學生集體死刑")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/1/1e/Zhang_Minzhi.jpg")
        self.go_back()

    def on_exit_state26(self):
        print('Leaving state26')

    def on_enter_state27(self, event):
        print("I'm entering state27")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "面對軍方束手無策的你，今天提早離開了學校，回家路上有人在發傳單，你希望可以幫助這個社會\n1.你拿著傳單，加入商業公會\n2.你拿著傳單，加入農業公會")

    def on_exit_state27(self,event):
        print('Leaving state27')

    def on_enter_state28(self, event):
        print("I'm entering state28")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "回到家，你的家人很緊張的告訴你一件事，你過去曾經參加過得讀書會被其他人知道了，於是你\n1.我選擇坦蕩作人，心中無鬼不必怕\n2.我選擇花錢封嘴，世風日下求安穩")

    def on_exit_state28(self,event):
        print('Leaving state28')

    def on_enter_state29(self, event):
        print("I'm entering state29")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是邱桶\n你參加的農民協會幫助農民擺脫貧窮，但是農會的幹部被舉發為共諜，縱使你並不知情這件事，你得到的結果是...")
        send_text_message(sender_id, "槍決")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/commons/3/3d/%E9%82%B1%E6%A1%B6.jpg")
        self.go_back()

    def on_exit_state29(self):
        print('Leaving state29')

    def on_enter_state30(self, event):
        print("I'm entering state30")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "恭喜！你是沈嫄璋\n你過往的經歷被檢舉，軍警假借約談的名義將你帶走，手無寸鐵的你只能乖乖配合，你得到的結果是...")
        send_text_message(sender_id, "刑求致死")
        send_image_url(sender_id, "https://upload.wikimedia.org/wikipedia/zh/7/77/Chen_Yuan_Zhang.jpg")
        self.go_back()

    def on_exit_state30(self):
        print('Leaving state30')

    def on_enter_state31(self, event):
        print("I'm entering state31")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "平安的一天又過去了，你感謝你自己做出明確的決定，你選擇明哲保身了自己，而其他人呢")
        send_text_message(sender_id, "想知道其他人怎麼了嗎，你可以選擇重新開始")
        self.go_back()

    def on_exit_state31(self):
        print('Leaving state31')
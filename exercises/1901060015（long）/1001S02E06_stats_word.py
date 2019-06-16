text="""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

def stats_text_en(text):
    # 文章字符串前期处理
    strl_ist = text.replace('\n', '').replace('.', '').replace('!', '').replace('--', '').lower().split(' ')
    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for text in strl_ist:
        if text in count_dict.keys():
            count_dict[text] = count_dict[text] + 1
        else:
            count_dict[text] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    return count_list
print (stats_text_en(text))

text="""村上春树，日本后现代主义作家，1949年1月12日生于京都伏见区。毕业于早稻田大学第一文学部演剧科。
村上春树29岁开始写作，第一部作品《且听风吟》即获得日本群像新人奖，1987年第五部长篇小说《挪威的森林》上市至2010年在日本畅销一千万册，国内简体版到2004年销售总量786万，引起“村上现象”。
其作品在世界范围内具有广泛知名度，作品风格深受欧美作家的影响，基调轻盈，少有日本战后阴郁沉重的文字气息，被称作第一个纯正的“二战后时期作家”，并被誉为日本80年代的文学旗手。 [1]  
2017年2月24日，村上春树出版两卷本长篇小说《刺杀骑士团长》，小说上卷命名为“念头显露篇”，下卷命名为“隐喻改变篇”。 [2]  该作品的中译本首印达70万册，由于预售反响不俗又进行了加印"""

def stats_text_cn(text):
    # 文章字符串前期处理
    strl_ist=[]
    for i in text:
        strl_ist.append(i)
    
    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for text in strl_ist:
        if text in count_dict.keys():
            count_dict[text] = count_dict[text] + 1
        else:
            count_dict[text] = 1
    #按照词频从高到低排列
    count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
    return count_list
print (stats_text_cn(text))


text = '''
愚公移⼭
太⾏，王屋⼆⼭的北⾯，住了⼀個九⼗歲的⽼翁，名叫愚公。⼆⼭佔地廣闊，擋住去路，使他
和家⼈往來極為不便。
⼀天，愚公召集家⼈說：「讓我們各盡其⼒，剷平⼆⼭，開條道路，直通豫州，你們認為怎
樣？」
⼤家都異⼝同聲贊成，只有他的妻⼦表示懷疑，並說：「你連開鑿⼀個⼩丘的⼒量都沒有，怎
可能剷平太⾏、王屋⼆⼭呢？況且，鑿出的⼟⽯⼜丟到哪裏去呢？」
⼤家都熱烈地說：「把⼟⽯丟進渤海裏。」
於是愚公就和兒孫，⼀起開挖⼟，把⼟⽯搬運到渤海去。
愚公的鄰居是個寡婦，有個兒⼦⼋歲也興致勃勃地⾛來幫忙。
寒來暑往，他們要⼀年才能往返渤海⼀次。
住在⿈河河畔的智叟，看⾒他們這樣⾟苦，取笑愚公說：「你不是很愚蠢嗎？你已⼀把年紀
了，就是⽤盡你的氣⼒，也不能挖去⼭的⼀⻆呢？」
愚公歎息道：「你有這樣的成⾒，是不會明⽩的。你⽐那寡婦的⼩兒⼦還不如呢！就算我死
了，還有我的兒⼦，我的孫⼦，我的曾孫⼦，他們⼀直傳下去。⽽這⼆⼭是不會加⼤的，總有
⼀天，我們會把它們剷平。」
智叟聽了，無話可說：
⼆⼭的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位⼤
⼒神揹⾛⼆⼭。

How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do our
best to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered
his wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and
remove the earth. They transported the earth and rubble to the Sea
of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years
old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full
year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected
for his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,
and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will never
understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my
grandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will not
grow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong
and his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered
two mighty gods to carry the mountains away.
'''
def stats_text(text):
    text1=text[1:495]
    text2=text[495:2800]
    return stats_text_cn(text1)+stats_text_en(text2)

print(stats_text(text))










       




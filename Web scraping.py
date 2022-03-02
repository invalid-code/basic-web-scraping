from bs4 import BeautifulSoup
import requests as rq
import re
finished_manga = {'Kenshi o Mezashite' : ['Ch. 46', 'Ch. 47', 'Ch. 48'], 'Tonikaku Kawaii' : ['Ch. 179', 'Ch. 180', 'Ch. 181'], 'Party kara Tsuihou Sareta' : ['Ch. 20.2', 'Ch. 20.3', 'Ch. 21.1'], 'Isekai Meikyuu no Saishinbu' : ['Ch. 14', 'Ch. 15', 'Ch. 16'], 'Hazure Akamadoushi wa Kenja' : ['Ch. 12', 'Ch. 13', 'Ch. 14'], 'Konjiki no Moji Tsukai' : ['Ch. 80', 'Ch. 81', 'Ch. 82'], 'Trinity Seven' : ['Ch. 128', 'Ch. 129', 'Ch. 130'], 'Relentlessly Approaching The Poison-Tongued And Indifferent Beauty To Tickle The Cutesy Reactions Out Of Her' : ['Ch. 2', 'Ch. 3', 'Ch. 4'], 'Shin no Jitsuryoku wa Girigiri' : ['Ch. 12', 'Ch. 13', 'Ch. 14'], 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e' : ['Ch. 49', 'Ch. 50', 'Ch. 51'], 'Tensei Kenja no Isekai' : ['Ch. 31', 'Ch. 32', 'Ch. 33'], 'The White Mage Who Was Banished From the Hero’s Party Is Picked up by an S Rank Adventurer' : ['Ch. 8', 'Ch. 9', 'Ch. 10'], 'Nido Tensei Shita Shounen' : ['Ch. 22.2', 'Ch. 23', 'Ch. 24'], 'The World’s Fastest Level up!' : ['Ch. 5', 'Ch. 6', 'Ch. 7'], 'Battle Frenzy' : ['Ch. 341', 'Ch. 342', 'Ch. 343'], 'Ranker Who Lives A Second Time' : ['Ch. 111', 'Ch. 112', 'Ch. 113'], 'The Max Level Hero Has Returned!' : ['Ch. 73', 'Ch. 74', 'Ch. 75'],
              'Ranker’s Return (Remake)' : ['Ch. 45', 'Ch. 46', 'Ch. 47'], 'Reincarnation of the Battle God' : ['Ch. 35', 'Ch. 36', 'Ch. 37'], 'Leveling With The Gods' : ['Ch. 41', 'Ch. 42', 'Ch. 43'], 'Shijou Saikyou no Mahou' : ['Ch. 54', 'Ch. 55', 'Ch. 56'], 'The Reincarnated Inferior Magic Swordsman' : ['Ch. 53', 'Ch. 54', 'Ch. 55'], 'Otome Game Sekai wa Mob' : ['Ch. 37', 'Ch. 38', 'Ch. 39'], 'Hellmode ~Gamer Who Likes to Speedrun Becomes Peerless in a Parallel World with Obsolete Setting' : ['Ch. 17', 'Ch. 18', 'Ch. 19'], 'Genkai Level 1 kara no Nariagari' : ['Ch. 14.1', 'Ch. 14.2', 'Ch. 15'], 'Magia Record' : ['Ch. 9', 'Ch. 10', 'Ch. 11'], 'The Irregular of the Royal Academy of Magic' : ['Ch. 45', 'Ch. 46', 'Ch. 47'], 'Kami no Techigai de Shindara' : ['Ch. 12', 'Ch. 13', 'Ch. 14'], 'A Returner’s Magic Should Be Special' : ['Ch. 177', 'Ch. 178', 'Ch. 179'], 'Omniscient Reader’s Point of View ' : ['Ch. 94', 'Ch. 95', 'Ch. 96'], 'The tutorial tower of the advanced player' : ['Ch. 98', 'Ch. 99', 'Ch. 100'], 'Solo Max-Level Newbie' : ['Ch. 34', 'Ch. 35', 'Ch. 36'], 'Return of the Frozen Player' : ['Ch. 47', 'Ch. 48', 'Ch. 49'], 'Berserk of Gluttony' : ['Ch. 39', 'Ch. 40', 'Ch. 41'], 'Assassin de aru ore no Sutetasu' : ['Ch. 16', 'Ch. 17', 'Ch. 18']}
url = 'https://kumascans.com/'
html = rq.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
latest_update = soup.find(text='Latest Update').parent.parent.next_siblings
for manga in latest_update:
    if manga != '\n':
        manga_name_chapter = manga.find_all(class_='luf')
latest_manga = {chapter_name.h4.text:chapter_name.ul.find_all(text=re.findall('Ch\. \d*\.?\d*', str(chapter_name.ul))) for chapter_name in manga_name_chapter if chapter_name.ul}
for read_manga in finished_manga.items():
    if read_manga[0] in latest_manga:
        for read_manga_index,latest_chapter in enumerate(latest_manga[read_manga[0]], 1):
            if eval(latest_chapter[4:] + "-" + finished_manga[read_manga[0]][read_manga_index*-1][4:]) > 3:
                print("you are behind more than 3 chapter's")
            else:
                print(f'you are behind {eval(latest_chapter[4:] + "-" + finished_manga[read_manga[0]][read_manga_index*-1][4:])} chapter')
    else:
        print('no new chapter')
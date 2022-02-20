from bs4 import BeautifulSoup 
import requests as rq 
read_manga = ["Kenshi o Mezashite", "Tonikaku Kawaii", "Party kara Tsuihou Sareta", "Isekai Meikyuu no Saishinbu", "Hazure Akamadoushi wa Kenja", "Konjiki no Moji Tsukai", "Trinity Seven", "Relentlessly Approaching The Poison-Tongued And Indifferent Beauty To Tickle The Cutesy Reactions Out Of Her", "Shin no Jitsuryoku wa Girigiri", "Youkoso Jitsuryoku Shijou", "Tensei Kenja no Isekai", "The White Mage Who Was Banished From the Hero’s Party Is Picked up by an S Rank Adventurer", "Nido Tensei Shita Shounen", "The World’s Fastest Level up!", "Battle Frenzy", "Ranker Who Lives A Second Time", "The Max Level Hero has Returned!", "Ranker’s Return (Remake)", "Reincarnation of the Battle God", "Leveling With The Gods", "Shijou Saikyou no Mahou", "The Reincarnated Inferior Magic Swordsman", "Otome Game Sekai wa Mob", "Hellmode ~Gamer Who Likes to Speedrun Becomes Peerless in a Parallel World with Obsolete Setting", "Genkai Level 1 kara no Nariagari", "Magia★Record", "The Irregular of the Royal Academy of Magic", "Kami no Techigai de Shindara", "A Returner’s Magic Should Be Special", "Omniscient Reader’s Point of View", "The tutorial tower of the advanced player", "Solo Max-Level Newbie", "Return of the Frozen Player", "Berserk of Gluttony", "Assassin de aru ore no Sutetasu"]
url = "https://kumascans.com/"
html = rq.get(url)
soup = BeautifulSoup(html.text, "html.parser")
main_page = soup.find("body")
latest = main_page.find(class_="releases")
print(latest)
# for manga in read_manga:
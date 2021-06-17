#game
#/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span		gundum	
#/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span		mario
#/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span		ringfit
#price
#/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]		gundum
#/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]		mario
#/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]		ringfit
#link
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[27]/div/div/div/div/a[1]			gundum
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[27]/div/div/div/div/a[2]			mario
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[27]/div/div/div/div/a[3]			ringfit

from selenium import webdriver
import pandas as pd

#set directory from folder we download ChromeWebdriver
driver = webdriver.Chrome(r"D:\Programs\Python\chromedriver.exe")
driver.get("https://shopee.co.th/m/super-games-zone-sale#top2")

#Find links
links = []
for i in range(1,10):
	link = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[2]/div/div[2]/div/div[27]/div/div/div/div/a[{i}]")
	link_g = link.get_attribute('href')
	links.append(link_g)


top10_games = []

#Open links	
for i in range(1,10):
	try:
		driver.get(links[i])
		game = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span").text
		price = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]").text
		top10_games.append([game, price, links[i]])
	except:
		pass

#DataFrame
df_top10games = pd.DataFrame(top10_games, columns=["Games", "Prices","Link"])

#Print
print(df_top10games)


driver.quit()


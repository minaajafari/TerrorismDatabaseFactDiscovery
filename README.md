introduction :
Genocide is an internationally recognized crime where acts are committed with the intent to destroy, in whole or in part, a national, ethnic, racial, or religious group. These acts fall into five categories: 
1-	killing members of the group 
2-	causing serous bodily or mental harm to members of the group
3-	Deliberately inflicting on the group conditions of life calculated to bring about its physical destruction in whole or in part
4-	Imposing measures intended to prevent births within the group
5-	Forcibly transferring children of the group to another group

If we have a review to the terrorist attacks news in Afghanistan we will get this point which most of these events occur in Hazara ethnicity living area.Hazara is one of Afghanistan ethnicity with different race and religious which is Shia. as this ethnicity has been victim of genocide by political leaders and kings during 18 century   , there is a hypothesis which says all of these systematic terrorist attacks and victims selection process by terrorist groups manage by aim of Hazara Genocide. in this research,we are looking for some facts to prove or reject this hypothesis.

The Global Terrorism Database(GTD) is an integrated data set about all of Terrorist events that have occured in the world with more than 120 attributes for each event from 1970 till mid 2021.we used this reliable data set as an scale for our data gathering process .so as we need all of events which target was Afghan civilans ,after preprocessing GTD dataset and extract desire datasets, we start data gathering process and our scale was the attacks which listed in GTD .there are tree citation for each event and we use these citation for find the news about that event .for find more relevant news we use keywords in the summery field of each event for search more news . we scrapped the content of these news which was contain :header ,date ,reference and the content of news by Python .At the end for 51 events which occurred in Kabul ,we scrapped about 280 news which is about 6 news for each event on average.


![gtd2](https://github.com/minaajafari/TerrorismDatabaseFactDiscovery/assets/117638768/2a3b53b2-7bd7-4d83-bfc5-24222c983174)

for access to GTD
https://www.start.umd.edu/gtd/contact/download





Material & Method:


Data preparation:process of data gathering devided in two steps.
First step : 
As GTD was include whole terrorist attacks in all over the world we should customized GTD for our research. We started preprocessing data with insert some filtered which listed bellow:
1-	country=Afghanistan
2-	city=Kabul
3-	all attack should be in last decade (between 2011 until 2021)
4-	attacks target should not be Military ,Police , Airport & Aircraft ,Government ,Tourist, Journalists & Media .
5-	attacks type should not be Hostage taking(kidnapping) and Assassination.
6-	Attacks target nationality should not be Afghan .
7-	Number of people who killed in this attacks should be more than two people .
 At the end we extracted 60 event which was belong to Afghanistan ,Kabul ,2011-2021 and target was just Afghan civilian.

Second step:
In this step we should find relevant and reference news which shared this event with details .for this mean we had some important attributes .summary and  three citation column was very helpful to linked us to relevant news website. the key words of event mentioned in summary of event in GTD, so we used this key words such as date of event, place of event and etc for access more news.
After access to this news we scraped its contents as a CSV dataset and at the end we could scraped about 280 relevant news to 60 extracted GTD events.
Our final scrapped news was include title of news, publication date ,news reference ,content of news and news link.












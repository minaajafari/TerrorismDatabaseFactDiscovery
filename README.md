# TerrorismDatabaseFactDiscovery
This Project is going to discover some facts behind of Terrorist attacks based on NLP approaches
Genocide is an internationally recognized crime where acts are committed with the intent to destroy, in whole or in part, a national, ethnic, racial, or religious group. These acts fall into five categories: 
1-	killing members of the group 
2-	causing serous bodily or mental harm to members of the group
3-	Deliberately inflicting on the group conditions of life calculated to bring about its physical destruction in whole or in part
4-	Imposing measures intended to prevent births within the group
5-	Forcibly transferring children of the group to another group

If we have a review to the terrorist attacks news in Afghanistan we will get this point which most of these events occur in Hazara ethnicity living area.Hazara is one of Afghanistan ethnicity with different race and religious which is Shia. as this ethnicity has been victim of genocide by political leaders and kings during 18 century and after , there is a hypothesis which says all of these systematic terrorist attacks and victims selection process by terrorist groups manage by aim of Hazara Genocide.
The Global Terrorism Database(GTD) is an integrated data set about all of Terrorist events that have occured in the world with more than 120 attributes for each event from 1970 till mid 2021.we used this reliable data set as an scale for our data gathering process .so as we need all of events which target was civilans ,after preprocessing GTD dataset and extract desire datasets, we start data gathering process and our scale was the attacks which listed in GTD .there are tree citation for each event and we use these citation for find the news about that event .for find more relevant news we use keywords in the summery field of each event for search more news . we scrapped the content of these news which was contain :header ,date ,reference and the content of news by Python .At the end for 54 events which occurred in Kabul ,we scrapped about 300 news which is about 6 news for each event on average.

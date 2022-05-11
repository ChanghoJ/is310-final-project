# IS 310 Final Project Post!
==

The prolonged semester project is finally done! I was glad to present my final work on History by Frequency because this was my first project that is involve coding other than a statistic. Although I am currently heading for Information Sciences with a Data Science major, my experience before undergraduate was far less likely a STEM. I enjoyed reading an easy historical text that is related to Korea, mostly focusing on modern history, and enjoyed United States History as I learned from international high school in Seoul. Even after I became a freshman at the University of Oregon, I attend several history classes as an elective. Yes, my interest was and is about history, international relationships, and government. (But this does not mean I have professional knowledge, rather I just enjoyed it.) Then, after prolonged armed service and the COVID-19 pandemic, I transferred to here, the UIUC as an IS student. At first, my pathway (IS +DS) seemed not related to the history that I enjoyed, but in IS 310 and through the final project, I realized “data science does have a connection with humanities.”

At the first time of thinking about my final project, I had no idea what to do, but the meeting with Professor LeBlanc gave me an impression of the task of my final project. During the meeting with the professor, I shared my interest as the professor requested, and the interests were video games, history, and international relationships. With my interests reported, the professor shared with me some significant blog posts about history and text analysis. The blog posts are from _The Pudding_, one post, [_The world through the eyes of the US_](https://pudding.cool/2018/12/countries/), about visualized country mentioned in NYT newspapers, and the other post, [_A brief history of the past 100 YEARS as told through the New York Times archives_](https://pudding.cool/2018/12/brief-history/), about most mentioned words by years in history. Both articles inspired me to give a try measuring words within the text and showing them as a graph. After the meeting, I keep inspired by other readings from a class activity like _Gendered Language in Teacher Reviews_ and _Film Dialogue_. [_Gendered Language in Teacher Reviews_](http://benschmidt.org/profGender/#%7B%22database%22%3A%22RMP%22%2C%22plotType%22%3A%22pointchart%22%2C%22method%22%3A%22return_json%22%2C%22search_limits%22%3A%7B%22word%22%3A%5B%22gay%22%5D%2C%22department__id%22%3A%7B%22%24lte%22%3A25%7D%7D%2C%22aesthetic%22%3A%7B%22x%22%3A%22WordsPerMillion%22%2C%22y%22%3A%22department%22%2C%22color%22%3A%22gender%22%7D%2C%22counttype%22%3A%5B%22WordsPerMillion%22%5D%2C%22groups%22%3A%5B%22department%22%2C%22gender%22%5D%2C%22testGroup%22%3A%22C%22%7D) visualized how certain words are frequently mentioned by gender in both positive and negative ways, and [_Film Dialogue_](https://pudding.cool/2017/03/film-dialogue/) visualized and claimed that character dialog lengths are mostly male-dominated, only about 22% of films have female leading dialog (Anderson & Daniels, 2016; Schmidt, 2015). These articles have two shared features that influence my final project, which are the visualized frequency of words in different frames and analyzed raw data. The blog posts gave me enough impression about how to proceed with my final project.
<p>&nbsp;</p>

![NISI20220102_0018301619_web](https://user-images.githubusercontent.com/25918993/167963503-3ed2d3f8-3cfe-459d-aa17-b4de1aa564ad.jpeg)

- From [Newsis](https://mobile.newsis.com/view.html?ar_id=NISX20220103_0001711209)

Then, how did I reach the theme of my final project, “How was Korea mentioned in the Cold War?” As mentioned at the beginning, I enjoyed some historical content before, but in addition to my interest, I just felt wonder about “would the frequent words mentioned are differed by years for Korea during the Cold War” because I also heard the old stories from my grandparents and parents in back in days of the Cold War Korea. Not only the old folk tales but the Cold War era indeed still impacting me and other relatives today. My grandfather served in the air force for 30 years, my father served in the air force military police for short time, and I served in the army for about 1 and a half years. I had a chance to visit one of the watchtowers at the frontline as a tourist, and vast excluded areas are separating the north and the south by river, forest, landmines, and concrete bunkers. During the armed service, my unit often practiced [Defense ready Condition (DEFCON)](https://militarybase.net/defense-ready-condition-defcon-levels/) drill in the preparation for war with North Korea, from level 4 (caution) to level 1 (total war). Of course, the armed tension between the North and the South is far less likely to become a war today, but my curiosity about the mood of the Cold War becomes larger than before the armed service.


![Ippdae](https://user-images.githubusercontent.com/25918993/167964025-92faaf98-009a-4796-adc6-68f589077c93.jpg)

- The day I get into basic combat training (BCT). I couldn't even feel a taste, probably the worst day of my life.ㅠ
<p>&nbsp;</p>

![graduation](https://user-images.githubusercontent.com/25918993/167962242-62d38c19-7b5e-4a5b-b17b-7a11f05efa74.jpg)

- Graduated from BCT, my beret seems really odd
<p>&nbsp;</p>

![meeting](https://user-images.githubusercontent.com/25918993/167962245-0c8ae0be-d30c-4528-ae20-559118274f93.jpg)

- Meeting with parent in duty station
<p>&nbsp;</p>

![discharge](https://user-images.githubusercontent.com/25918993/167962239-e905b7c2-cfe5-4912-b638-a7bf7cea9db1.jpg)
- Discharge! One of best day of my life.ㅎ
<p>&nbsp;</p>
<p>&nbsp;</p>

### Datasets and Method
==

<p>&nbsp;</p>
<img width="1440" alt="NYT API home" src="https://user-images.githubusercontent.com/25918993/167952959-9680bd68-69b4-40ff-a3c8-549a88f5079e.png">
<img width="1050" alt="NYT API search" src="https://user-images.githubusercontent.com/25918993/167952960-62335c88-6db9-4388-b5eb-aec5cc0f50b9.png">

Ok, this is how I eventually decided to analyze text frequency on the journal articles during Cold War Korea. To accomplish my text analysis project, I needed to find news article datasets that are far back to the 1950s. Thankfully, Professor LeBlanc introduced the NYT API that contains news articles that I need for the time frame between the 1950s to 1991. 
<p>&nbsp;</p>
<p>&nbsp;</p>

<img width="1409" alt="NYT API key" src="https://user-images.githubusercontent.com/25918993/167954119-fa38aee3-2b4d-4f3d-9204-17ae760fedd3.png">

- First, as we learned during the “Introduction to APIs” class, to call the old articles from NYT API, I needed to receive the API key for calling from the website. 
<p>&nbsp;</p>
<p>&nbsp;</p>


<img width="1437" alt="python pandas nltk" src="https://user-images.githubusercontent.com/25918993/167952963-4104fc6c-be73-4ba2-baa7-b70085fddc69.png">

- Second, open the Python and import all the add-ons like pandas for using CSV files, requests for requesting data from a link, and NLTK for analyzing data as we learned from Introduction to Unstructured Data. 
<p>&nbsp;</p>
<p>&nbsp;</p>


<img width="1372" alt="Text mine" src="https://user-images.githubusercontent.com/25918993/167952967-f401b4a5-0134-4980-a034-381e45528b9e.png">

- Third, because I need as much data as possible, I used for loop to repeat the data calling code for a given amount of time. 
- I set up hits for 201, for the API returns an error only after the 200th result. 
- Then, I created an empty list for gathering all the called data from API. 
- Within the for loop, I used the if statement that causes a 50-second delay on calling for every 10th iteration of code because according to NYT article search API, the code returns an error right after running 10 hits (pages). 
- Then the URL page is assigned as an nth loop, requested data by request.get (URL assigned with API key from website), received data as JSON format, printed number of hits I can receive and how many results I received, combined results, and at last, appended data to the empty list.
<p>&nbsp;</p>
<p>&nbsp;</p>


<img width="718" alt="save as csv" src="https://user-images.githubusercontent.com/25918993/167959044-2da61c06-64cb-4e90-9331-f8b4ff48ee2f.png">

<img width="255" alt="CSVs" src="https://user-images.githubusercontent.com/25918993/167954780-a74279a8-dad7-4b83-b5a3-42d96fa4388e.png">

- Fourth, after finishing data gathering in 4-time frames (the 50s, 60s, 70s, and 80s to end), I created data frames from the gathered data and saved them as CSV files because receiving data takes a long time. 

<img width="1346" alt="dataframe" src="https://user-images.githubusercontent.com/25918993/167952956-215cd063-23a3-42b3-b4c8-f4e24b29dd53.png">

- I was faced with a problem here, some parts of the dataset or columns are empty. I did not know why, but as one of our readings [_The Library of Missing Datasets_](https://mimionuoha.com/the-library-of-missing-datasets) (2016) mentioned, there are missing data that data might exist before but were missed for some reason or just did not exist at the beginning.
<p>&nbsp;</p>
<p>&nbsp;</p>


<img width="1364" alt="text analysis 1" src="https://user-images.githubusercontent.com/25918993/167952966-c24b94e7-2b6a-4c21-bed6-2011c8101afb.png">

- Anyway, I need to use many texts to analyze the frequency of words by year, so I decided to combine columns that contain texts, such as abstracts, snippets, lead paragraphs, and headlines. 
<p>&nbsp;</p>
<p>&nbsp;</p>


<img width="987" alt="lower case stop word" src="https://user-images.githubusercontent.com/25918993/167952957-7c1f480c-3866-4ffa-b4a4-6b9a26198663.png">

<img width="594" alt="stemming" src="https://user-images.githubusercontent.com/25918993/167952965-58bfc66c-8acc-44c0-9038-a65d9a9ccfc8.png">

<img width="726" alt="visualization" src="https://user-images.githubusercontent.com/25918993/167952968-352b05d8-b920-4c59-9235-48a0f77d6c67.png">

- Fifth, I lowered cases and removed any stop words to filter possible disturbance of analysis. Then I stemmed words and removed further texts that are not word and nan. Sixth, finally, I plotted word frequency by 4-time frames by 50 results.
<p>&nbsp;</p>
<p>&nbsp;</p>

### Results
===

<img width="738" alt="50s" src="https://user-images.githubusercontent.com/25918993/167953017-72f3b6ce-1783-484d-8eb0-a0a6412067b5.png">

- [First Republic](https://www.britannica.com/place/South-Korea/History#ref34987) (1950s) (Hahn & Lew, 2022)

<img width="982" alt="United Nation Force" src="https://user-images.githubusercontent.com/25918993/167959815-b24fe36f-c3c8-4604-9d53-6a92afc0ed6a.png">
<img width="990" alt="Eisenhower" src="https://user-images.githubusercontent.com/25918993/167959814-a59f34fe-5e65-4a1d-b396-f6b568938f64.png">

According to the graph, you can see UN, nation, force, war, Seoul, troop, Rhee, Eisenhower. “war,” “force,” “Seoul,” and “troop” probably mention [Korean War between June 25, 1950. ~ July 27, 1953.](https://www.britannica.com/event/Korean-War) “UN” and “nation” probably referring the support of the United Nations, and the “Rhee” refers President of Korea at that time, Rhee Syng-man.
<p>&nbsp;</p>
<p>&nbsp;</p>

<img width="661" alt="60s" src="https://user-images.githubusercontent.com/25918993/167953018-f5d48dbf-f448-4c0c-a6b1-07550d42619e.png">

- Second to Third Republic (1960s)

<img width="972" alt="516 revolt" src="https://user-images.githubusercontent.com/25918993/167959945-11f8919c-04f0-4424-9cfa-29c90713e038.png">
<img width="990" alt="DMZ conflict" src="https://user-images.githubusercontent.com/25918993/167959947-6e9332e4-558d-494b-81b9-78abcf934a76.png">
<img width="932" alt="Vietnam dispatch" src="https://user-images.githubusercontent.com/25918993/167959948-61fde74a-fe2e-46de-a87f-e1e7ef7e72d7.png">

According to the graph, you can see Park, junta, Vietnam, demilitarized zone. The words “Park” and “junta” might reveal a military junta that was formed by the coup of military dictator Park Chung-hee, who later reign as president. “Vietnam” and “demilitarized zone” might show the military dispatch to the Vietnam War and conflicts in DMZ in Korea.
<p>&nbsp;</p>
<p>&nbsp;</p>

<img width="796" alt="70s" src="https://user-images.githubusercontent.com/25918993/167953019-179699f4-f64f-41f4-a37b-ec265b753d19.png">

- Third to Fourth Republic (1970s)

<img width="809" alt="President Carter conflict" src="https://user-images.githubusercontent.com/25918993/167960115-8f867a86-f9c0-49d4-b88d-2428394a8cbb.png">
<img width="975" alt="withdraw of USFK" src="https://user-images.githubusercontent.com/25918993/167960117-734cbbda-69a7-48ee-810b-f4e07407809e.png">

According to the plot, we have the words Park, Chung, hee, Carter, withdraw. The words “Park,” “Chung,” and “hee” indirectly mention that President Park still reigns as dictator. “Carter” and “withdraw” were possibly mentioned by the President of the United States Jimmy Carter and some policies went over for the withdrawal of US forces in Korea.
<p>&nbsp;</p>
<p>&nbsp;</p>

<img width="792" alt="80s to end" src="https://user-images.githubusercontent.com/25918993/167953020-5443d095-f44d-4386-8084-daf840ba1747.png">

- Fifth to Sixth Republic (1980s to 1991)

<img width="985" alt="TangTang" src="https://user-images.githubusercontent.com/25918993/167960195-553c59eb-40c2-4f59-beb3-64d19d4448c7.png">
<img width="958" alt="The other revolt 2" src="https://user-images.githubusercontent.com/25918993/167960199-8c439cc7-12d3-4ac3-9180-d4cfe3198515.png">
<img width="983" alt="Gwangju" src="https://user-images.githubusercontent.com/25918993/167960193-91038f09-6891-4501-9ce0-9ca17b75bf1b.png">
<img width="978" alt="Democratization" src="https://user-images.githubusercontent.com/25918993/167960192-17b55d76-5605-428d-ae40-d4bf890a78ef.png">
<img width="985" alt="88 Olympic" src="https://user-images.githubusercontent.com/25918993/167960190-36c8fa8c-d497-4841-8c6a-976c03ccf98d.png">

According to the plot, the words Chun, doo, hwan, Olympic, Soviet, and protest are revealed. The words “Chun,” “doo,” and “hwan” reveal the dictator President Chun Doo-hwan, who reigns in power with the military coup. “Protest” might refer to one the Gwangju democratic protest and the June Democratic Protest, in which the first protest was suppressed brutally and the second protest eventually lead to full democratization. “Olympic” and “Soviet” probably refer 1988 Olympics in Seoul and the end of the Cold War in 1991.
<p>&nbsp;</p>
<p>&nbsp;</p>

- Results

As the results show, I could receive some historical insights within the selected words, but not as specific as expected. For example, around the 60s and 70s, there were multiple conflicts occurred around the DMZ area, and Panmunjom was one of the places. In 1976, 2 US officers were killed by the North Korean forces in Panmunjom during cutting a tree [(Friedman, 2018)](https://www.theatlantic.com/international/archive/2018/06/axe-murder-north-korea-1976/562028/). The country was almost at war, but I cannot find any words that are related to the incident.

I did not form a data biography as Heather Krause (2017) did in one of our reading [_Data Biographies: Getting to Know Your Data_](https://gijn.org/2017/03/27/data-biographies-getting-to-know-your-data/) because at least I know where, who, how, and why about data, since NYT API is formed by journalism for news purpose. It seems that my text analysis method or the data gathering method had a problem. I feel the frequency result would different if combines with name entities recognition to find the frequency for specific nouns. Also, I know it is difficult or almost impossible, but I wonder what if I could collect every hit from the API. Would the result be different as I have more data now?

To sum up, although the final result was not as specific as I wanted, at least I feel now more familiar with one portion of digital humanities. Rather than just analyzing old articles, using computation and text analysis makes it possible to see overall aspects of old texts as a series or as one theme, just like the frequency of words presented in each timeframe of Korea from the 1950s to 1991.
<p>&nbsp;</p>
<p>&nbsp;</p>

### References
===

- Anderson, H., &; Daniels, M. (2016, April). _Film Dialogue  from 2,000 screenplays, Broken Down by Gender and Age_. The Pudding. Retrieved May 10, 2022, from https://pudding.cool/2017/03/film-dialogue/
- Friedman, U. (2018, June 10). _The 'god damn' tree that nearly brought America and North Korea to War_. The Atlantic. Retrieved May 11, 2022, from https://www.theatlantic.com/international/archive/2018/06/axe-murder-north-korea-1976/562028/
- Hahn, B.-ho, & Lew, Y. I. (2022, May 5). _History of South Korea_. Encyclopædia Britannica. Retrieved May 9, 2022, from https://www.britannica.com/place/South-Korea/History#ref34987!
- Krause, H. (2017, March 27). _Data Biographies: Getting to know your data_. Global Investigative Journalism Network. Retrieved May 11, 2022, from https://gijn.org/2017/03/27/data-biographies-getting-to-know-your-data/ 
- Schmidt, B. (2015, February). _Gendered Language in Teacher Reviews. Gendered Language in Teaching Evaluations_. Retrieved May 10, 2022, from http://benschmidt.org/profGender/#%7B%22database%22%3A%22RMP%22%2C%22plotType%22%3A%22pointchart%22%2C%22method%22%3A%22return_json%22%2C%22search_limits%22%3A%7B%22word%22%3A%5B%22gay%22%5D%2C%22department__id%22%3A%7B%22%24lte%22%3A25%7D%7D%2C%22aesthetic%22%3A%7B%22x%22%3A%22WordsPerMillion%22%2C%22y%22%3A%22department%22%2C%22color%22%3A%22gender%22%7D%2C%22counttype%22%3A%5B%22WordsPerMillion%22%5D%2C%22groups%22%3A%5B%22department%22%2C%22gender%22%5D%2C%22testGroup%22%3A%22D%22%7D
- _The library of missing datasets_. MIMI ỌNỤỌHA. (n.d.). Retrieved May 10, 2022, from https://mimionuoha.com/the-library-of-missing-datasets

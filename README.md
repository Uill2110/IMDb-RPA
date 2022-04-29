> Status: ready to homolog ⚠️

# IMDb-RPA
### This RPA Solution must open the IMDb Page, get all favorite movies informations enable and genarate an Excel File.


## STEP-1 OPEN_PAGE
+ When we open the page the robot need click to login and send the credentials.
+ After this, it need only WAIT for the elements appear.


## STEP-2 GET_FAVORITE_FILMS
+ Using Python models path app\models\pandas we are able to get the movies pages
+ this package makes the web scraping in the movies pages using requests and bs4 libs and get the necessary information



## STEP-3 EXPORT_TO_EXCEL
+ Using pandas library we export all the informations from the csv and from the webscraping tool to a Data Frame.
+ After this we generate a '.xlsx' file from the data frame using Pandas lib.

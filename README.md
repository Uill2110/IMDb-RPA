
# IMDb-RPA

> Status: ready to homolog ⚠️

### This RPA Solution must open the IMDb Page, get all favorite movies informations enable and genarate an Excel File.

## STEP-0 RUN_THE_PROGRAM
+ To run the program, we just need install the required libs and after this run the 'run.py' file.

## STEP-1 OPEN_PAGE
+ When we run the program the robot need to open the chrome browser in the page
+ click to login and select 'login with IMDb', send the credentials.
+ After this, it need only WAIT for the elements appear.


## STEP-2 GET_FAVORITE_FILMS
+ After the login steps, the programs find the 'Export this list' button.
+ This link download a '.CSV' file listing all the movies in the favorites list


## STEP-3 GET_FAVORITE_FILMS
+ Using Python models path app\models\pandas we are able to get the movies pages in the .CSV file.
+ this package makes the web scraping in the movies pages using requests and bs4 libs and place the necessary information into a dataframe.


## STEP-4 EXPORT_TO_EXCEL
+ Using pandas library we export all the informations from the csv and from the webscraping tool to a Data Frame.
+ After this we generate a '.xlsx' file on the 'Output' folder from the data frame using Pandas lib


### Technologies Used:
<table>
  <tr>
  <td>Python</td>
  <td> ChromeDriver</td>
  </tr>
  <td>3.10.0</td>
  <td>100.0.4896.60</td>
  <tr>
  </tr> 
</table>

## How to run the application:
#### Run the 'run.bat' file.

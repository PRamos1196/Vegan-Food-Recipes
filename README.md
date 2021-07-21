# project1-par25

# Recipe Page:
This is web applicaition I made using the Spoonacular API, Heroku, Flask Framework, Bootstrap. The purpose of this app is to display random vegan recipes I found were delicious and show recipes recent tweets and a link that will send you to the instruction ofthe recipe and the tweet its related to.

## How it works
* Look up different recipes, sees random recipes, create your own and save your favorite ones to chef up
 
## Instalation and Setting up (Assumption you know how to use Github and the functions of .gitignore)
* step 1. sign up for twitter developer portal at https://developer.twitter.com
* step 2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
* step 3. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
    If needed, you can regenerate your access token and secret.
* step 4. Run the following in your terminal:
```
      sudo pip install tweepy
(or)  sudo pip3 install tweepy
(or)  pip install tweepy
(or)  pip3 install tweepy
```
* step 5. Install Bootstrap, tuturial and installation can be done on this site if needed: https://getbootstrap.com/docs/4.3/getting-started/download/
* step 6. Install flask using the same process as above ([sudo] pip[3] install flask)
* step 7. Install python-dotenv using the same process as above ([sudo] pip[3] install python-dotenv)
* step 8. sign up for spoonacular developer portal at https://spoonacular.com/food-api
* step 9. click on profile and generate and copy your api key
* step 10. Add your secret keys (from step 2 and step 9) by making a new root-level file called tweepy.env and populating it as follows:

```
(KEY)     oauth_consumer_key=''
(KEY_SECRET)    oauth_consumer_secre=''
(TOKEN)      oauth_token=''
(TOKEN_SECRET)  oauth_token_secret=''
(SPOON_API)    SPOON_API=''

```
* step 11. Navigate to https://signup.heroku.com/t/platform?c=70130000001xDpdAAE&gclid=EAIaIQobChMI5fbNr_iO7AIVUMDICh1HyQOcEAAYASAAEgJRsvD_BwE and make a new heroku account
* step 12. Click on "New" and then create a new app and give it a unique name
* step 13. Install the following: npm install -g heroku
* step 14. Create the following files: Procfile, and requirements.txt
* step 15. At the end of the Procfile add the new line: 
``` web: python app.py ```
* step 16. At the end of the requirements.txt add to the new line:
```
    tweepy
    Flask
    python-gotenv
    requests
```
(note: this is case sensitive)
* step 17. Add the secrets keys to your heroku settings: 
``` settings -> config vars ```
* step 18. run the following commands in the same directory as the project location:
``` 
    heroku login -i
    heroku create
    git gush heroku master
```
* congradulations your app should be working through heroku!

## Technical Problems (solved and unsolved)
* If you try to run app.py more than the send limit, you will encounter an error, the app.py fixes this by adding a wait time until it is ready to send again
* Depending on the Browser, this wont work specifically the Browser: Brave, to fix this any alternative browser will work
* My python variable is a tuple, this may bring up problems later on if a tweet might contain more than what is given such as the author name, date, and the tweet itself.
* Python's Flask has issues regarding Cache, the solution is to clear your cache within your web browser settings.
* sometime the page wouldnt loud because of an empty index. spoonacular api recipes sometimes do not have a page and have an error in them, the best fix is to find a working recipe page
* reminder that you only have 150 usable calls a day for spoonacular api, this program calls it 4 times in 1 use, be very resourceful, fixes coming soon.
* At times when the page resets the page will come to en error within the selected food choices, a fix that can be to get a better selected sample of food choices in spoonaculars library of recipes, as mentioned in technical issues sometimes those recipes are removed or not availabe if i had more time maybe have a checker to make sure the webpage is complete or has the recipe
* Another issue was within heroku, sometimes when installing heroku an error will occur within the webpage to fix this I had to correct the port

## Improvements in the future
* I would like to add better styling in the HTML and CSS as well as including javascript within to make cool functions within the webapp, adding a search bar to see recipes you want would greatly improve this site
* I would also like to improve the functionality of random, where instead of keeping it as a list maybe extract recipes that fit the vegan criteria which is found in the JSON

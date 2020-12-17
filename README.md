# what's-it-called

This app predicts the car name from a logo. Currently only predicts a logo of 5 companies: Toyota, Honda, Volkswagen, Hyundai and Lexus.

## Give it a try

The vehicle-logo.png is a test file for testing the app and getting an idea of what kind of file to upload for it to work.

Deployed on: https://carname-api.herokuapp.com/  
Colab notebook for model: https://colab.research.google.com/drive/1MD1Wp67pltaBPp10ndfjwBNjtYR-iawQ?usp=sharing

### Test on local machine

If the above link does not work, follow these steps for setup on loacl machine. Don't worry its not much

```
1. clone repo to local machine
2. setup and run flask app:

	(For windows use, 'set' instead of 'export')
	export FLASK_APP=setup.py
  	export FLASK_ENV=development
  
3. flask run
```

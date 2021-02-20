# blockchain
This should be a good place to start :)
I built a basic framework for email/login functionalities, connection to algod-client, checking on account balance and stuff....

__replicate this Repo to your local machine:__
* git clone https://github.com/zifanwangsteven/blockchain.git
* start up a python virtual environment

__start up a python virtual environment__
* python -m venv venv
* source venv/bin/activate (for mac/linux users)

__install all packages in requirements.txt by:__
* pip install -r requirements.txt


__set up a few environment variables by adding the following to your .bashrc / .zshrc files:__
* export FLASK_APP=flasky.py
* export MAIL_USERNAME=youremailadress@gmail.com
* export MAIL_PASSWORD=your email password
* export ALGOD_ADDRESS=https://testnet-algorand.api.purestake.io/ps2
* export API_KEY= your api key obtained from purestake

__set up database:__
* flask db migrate
* flask db upgrade


__deploy on local server:__
* flask run
* open go to localhost:5000 in browser
**for email functionalities to work, you have to approve for insecure apps in your gmail setting**


## TO-DO
* project financing related
* bond features -> smart contract
* non-transparent management -> price fluctuation -> supply chain management?
* browser -> website 
* marketplace -> secondary trading -> online trading -> YTM
* query recent trading history

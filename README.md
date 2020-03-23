# CoronaVirus Bot for India (Covid19)
!(https://i.ibb.co/8BmwQDs/corona-slack-bot.png)
## Features
- Sit back and relax - the coronavirus updates will come to you.
- Get Slack notifications (picture below)
  -  New Corona Virus cases happening in India
  -  How many Indian nationals have Corona Virus per State?
  -  How many deaths happened per State?
  -  The new States entering the corona zone like Chattisgarh
- Too many updates? Subscribe only to the states that you want.

## Installation
- You need Python
- You need a Slack account + Slack Webhook to send slack notifications to your account
- Install dependencies by running
```bash
pip install tabulate
pip install requests
pip install beautifulsoup4
```
- Clone this repo and create auth.py
```bash
git clone https://github.com/rachitiitr/coronovirus-bot-tracker.git
cd coronovirus-bot-tracker
touch auth.py
```
- Write your Slack Webhook into auth.py
```python
DEFAULT_SLACK_WEBHOOK = 'https://hooks.slack.com/services/<your custome webhook url>'
```
- Setup the cron job to receive updates whenever something changes
```bash
crontab -e # opens an editor like vim or nano
# now write the following to run the bot every 5 mins
*/5 * * * * cd $PATH_TO_CLONE_DIR; python3 covid-19_bot.py --states 'haryana,maharashtra'
# to receive updates for all states, ignore the --states flag
```



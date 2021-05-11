# QueueUp Discord Bot
Basically QueueUp Live But on Discord

## Running it Locally
You would need to create environment variables in order for the program to work. 
You need to create a .env file inside your project directory, and assign these variable names. 
```
TOKEN=[Token from Discord API]
DATABASE=[Location of the Database]
DATABASE_DIRECTORY=[Location of Databases to other servers]
GOOGLE_ACCOUNT_KEY_FILE=[Location of Google File to Sync with Google Drive]
```
For rooms, each voice channel will be assigned a text channel. As a result, if there is a video failure, the TA and student can still connect via text channel.

You can store the environment variables inside a .env file. In production, it doesn't use load_dotenv, so do not create .env for production. 

To run it, you can run bin/gueueup-bot directly. 
```bash
python3 bin/queueup-bot
```
Please note that your working directory must be the root of the file, so it can access the .env file. I would recommend using Pycharm for this project. 

## Permissions to Set for the bot
1. Move Members
2. Read Message History
3. Manage Messages
4. Add Reactions
5. Embed Links
6. Send Messages
7. Manage Emojis
8. Manage Channels
9. View Channels

Also enable Privileged Gateway Intents.
- This gives the bot more control over getting members inside a server.

## Installation [Production]
You can install it using the following command
```bash
python3 setup.py install
```

You run it using the following
```bash
queueup-bot
```

## Basic setup [Production]
```.
Home Directory
│
├─── databases
│    └── queueup.db [database for Server]
│    └── queueup-servers [directory of other sqlite3 databases]
│        └── example-server-id.db [server's attributes (rooms, queues, history, etc)]
│
├─── environments 
│    └── queueup.environment [Location to store enivronment variables]
│
├─── scripts 
│    └── queueup.sh [Used only for CI/CD. It is optional]
```

## Running on AWS EC2 Instance
There is a script called ec2.sh, which can run on an EC2 instance if you decide to run the bot on an EC2 Instance. 
The Bot is currently being run by the cheapest EC2 Instance on AWS. 
For scalability, I am planning to use AWS Elastic Beanstalk.
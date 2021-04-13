# 3100 Project: DevTour


DevTour is a simple web application, aiming to build a platform for students, especially programming beginners, to play mini games to experience as a developer and to communicate with each other. Users can log in their accounts and play the game, and also leave their own comments and walkthroughs in the chat board. Our vision is to let users, especially novices in programming, understand the experience of being a software developer and engineer through the story of the game, and to create a platform for beginners and masters to communicate and discuss.

### demo video link: https://youtu.be/kemoeCB2jWU

## Done

We have used front-end interaction and storage of user data. The user can successfully register, log in and log out through the login system, and the administrator can log in and modify the user account information and add new administrator account through the administrator login interface. After logging in, the user enters the main interface. The main interface includes the game interface and the comment interface.

In the game interface, we have realized the operation logic of the game, mainly completed the front-end part of the user interaction, the back-end part of the game data saving function needs to be added. In the user chat interface, users can post their own comments and comment on others' comments.

### Language & Tools
* Front-end: HTML5 CSS3 Bootstrap JavaScript jquery Ajax 
* Back-end: NodeJS Express MySQL


## Getting Started

Make sure that you have Google Chrome, MySQL, and NodeJS installed in your environment. In the test phase, we will use the MacOS Big Sur 11.1, Google Chrome V89.0.4389.90, NodeJS V13.9.0 and MySQL V8.0.21 as the testing environment. Please refer to the following steps to configure your environment.

* NodeJS Download: https://nodejs.org/zh-cn/download/
* MySQL Download: https://www.mysql.com/cn/downloads/
* MySQL Configuration (for testing, please change to your preferance):
  * host: localhost
  * user: root
  * password: yy990525
  * database: CSCI3100
* Database Table Schema:
  * user(username varchar(20) not null, password varchar(20) not null, primary key(username));
  * admin(username varchar(20) not null, password varchar(20) not null, primary key(username));
  * chat(id int auto_increment, pid int not null, username varchar(20) not null, comment varchar(300) not null, subject varchar(20) not null, time varchar(50) not null, primary key(id)); 
* you may need to install some modules:
```sh
npm install express
```
```sh
npm install body-parser
```
```sh
npm install marked
```
```sh
npm install mysql
```
```sh
npm install fsevents
```
```sh
npm install events
```

## System Intro & Demo
1. Please first clone the repo
```sh
git clone https://github.com/1155124617/CSCI3100.git
```
```
filetree CSCI3100 
├── GroupA5 Project Initial Design Report.docx
├── demo_images
├── 3100_proj.zip
├── main_page.zip
└── README.md
```
2. Please unzip the file 3100_proj.zip:
```sh
unzip 3100_proj.zip
```

The file tree is as follows:

<img width="50%" height="50%" src="demo_images/configuration/1.png"/>

```
filetree 3100_proj
├── sign_in
├── sign_up
├── admin
├── main_page
├── server.js
├── node_modules
├── package-lock.json
└── package.json

```
<div align="center"><img width="50%" height="50%" src="demo_images/configuration/2.png"/></div>

3. Please configure the database as shown below：

<img width="50%" height="50%" src="demo_images/configuration/3.png"/>

4. After that, you can set up the NodeJS server as follows, make sure you have downloaded NodeJS in your computer:

<img width="50%" height="50%" src="demo_images/configuration/4.png"/>

5. Finally, you can open Chrome and enter:
```sh
localhost:8081/sign_in/index.html
```

Please have fun with our web application! :)

## Subsystem Demo

### User Reg & Login System

First the user should sign up to login. The URL of the sign-up form is localhost:8081/sign_in/index.html. You shall input one distinct username and your password for this account to complete the sign-up procedure. After you successfully sign up, the page will be redirected to the sign-in page. Then you can input your account information to sign in. If success, you will go into the main page of the DevTour.

1. At localhost:8081/sign_in/index.html, you can enter your username and password to log in. The username and the password you entered must be 5-16 symbols (letter or number). If you enter invalid username or password, there will be error messages to let you enter again:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/1.png"/></div>

2. If the username or password you enter is empty, there will also be error message:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/2.png"/></div>

3. If the username you enter doesn't exist or the password is wrong, there will be an alert message:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/3.png"/></div>

4. You can click "Create your account" and enter the sign up page. If your username entered is not valid, there will also be error message like above:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/4.png"/></div>

5. After entering a valid username and password, sign up successfully:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/5.png"/></div>

6. Then you can log in successfully:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/6.png"/></div>

7. You will enter to our main page. You can click the logout button on the top left corner:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/7.png"/></div>

8. After loging out, if you click return button of the web browser, the system will ask you to log in first. It's very safe:

<div align="center"><img width="80%" height="80%" src="demo_images/reg_log/8.png"/></div>

### Administrator System

In our administrator system, there will be an initial administrator account. The administrator can create new administrator account, create, update and delete user account. In the future, there will be more functions for administrator.

1. There is a button named "Administrator login" in the main page localhost:8081/sign_in/index.html. You can click it to enter the login page for administrator

<div align="center"><img width="80%" height="80%" src="demo_images/admin/1.png"/></div>

2. The rules for admin account is the same as user aaccount. if you enter the admin account incorrectly, there will be an alert:

<div align="center"><img width="80%" height="80%" src="demo_images/admin/2.png"/></div>

3. After login successfully, there will also be an alert:

<div align="center"><img width="80%" height="80%" src="demo_images/admin/3.png"/></div>

4. After login successfully, you can enter the main page for administrator to manage accounts:

<div align="center"><img width="80%" height="80%" src="demo_images/admin/4.png"/></div>

5. You can choose different functions:

<div align="center"><img width="80%" height="80%" src="demo_images/admin/5.png"/></div>

6. For example, if you want to update user account, you can enter the informations according to the form. If it's a valid operation, there will be an alert:

<div align="center"><img width="80%" height="80%" src="demo_images/admin/6.png"/></div>

7. As the following shows, the account has been updated:

<div align="center"><img width="80%" height="80%" src="demo_images/admin/7.png"/></div>
<div align="center"><img width="80%" height="80%" src="demo_images/admin/8.png"/></div>

### Game System
In the latest version 1.0.1, we have finished the Game logic and the user interface optimization. For Game Logic, we have used a few events to demonstrate the process. To be more specific, we change the status of the user according to their choices and when the status of the user reach a threshold value, game is over (just for initial demo). We will make the structure of the game more complicated and reach the goal of saving and loading in the next phase. For the user interface, we designed it based on the booklet plugins and we tried to put the game question in the right side page of the book and the status is displayed in the left hand side page. 

1. Users can click "DevTour" button on the left to enter the game page:

<div align="center"><img width="80%" height="80%" src="demo_images/game/1.png"/></div>

2. There will be a series of questions and you can choose your answer. For example, let's say, we choose "agree" and the value of physical health will increase:

<div align="center"><img width="80%" height="80%" src="demo_images/game/2.png"/></div>

3. Then the next question will show and you can choose your answer:

<div align="center"><img width="80%" height="80%" src="demo_images/game/3.png"/></div>

4. Some choise will decreasing some health values, now your money is not enough:

<div align="center"><img width="80%" height="80%" src="demo_images/game/4.png"/></div>

5. If some values are lower than the threshold, the game will over and it will restart again:

<div align="center"><img width="80%" height="80%" src="demo_images/game/5.png"/></div>

### Chat Board System

Chat Board can be reached from the main page. It requires the user to first login. You could add a new comment to the chat board. You also are able to reply others' comments by jusst clicking the "Reply" button. Once you add or reply some comments, the page would be re-rendered. Your comment would be sent the back-end server which stores your comment information to the database. The comment needs to input your name, subject and comment content. In addition, you could also select a color for the comment header. 

1. You can click "Chat Board" button on the left to enter the chat board system, the system will show the comments before:

<div align="center"><img width="80%" height="80%" src="demo_images/chatboard/1.png"/></div>

2. You can post your idea through the form in the button:

<div align="center"><img width="80%" height="80%" src="demo_images/chatboard/2.png"/></div>

3. For example, we post another comments and it will shown immediately:

<div align="center"><img width="80%" height="80%" src="demo_images/chatboard/3.png"/></div>

4. We can also reply others' comments:

<div align="center"><img width="80%" height="80%" src="demo_images/chatboard/4.png"/></div>

## Future Plan

* game backend
* update chat board system
* add more admin operations
* UI decoration
 ...


## Release History

* 0.1.0
    * CHANGE: Login and Reg System
* 0.2.0
    * CHANGE: Administrator System: CUD user account, C admin account
* 0.3.0
    * CHANGE: Basic Comment System
* 1.0.0
    * CHANGE: Basic Game System
* 1.0.1
    * CHANGE: Fix the server bug, optimize the interface of Game System and update the documentation

## Authors

* **YU Yue** 1155124490
* **DING Baizeng** 1155124617
* **CHANG Chirui** 1155124553
* **LYU An** 1155124488

## Reference
* https://www.bootstrapdash.com/product/skydash-admin-template/
* https://colorlib.com/wp/template/login-form-v1/
* https://colorlib.com/wp/template/login-form-v8/
* https://www.jq22.com/jquery-info2490
* http://builtbywill.com/
* https://www.jq22.com/demo/jquery-fanshu-150325215701/
* Assignment 2, CSCI 2720 T2, 19-20, YU Yue.


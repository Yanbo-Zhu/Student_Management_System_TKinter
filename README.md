# Student Grade Management System

## System Dependency
Python3
Third Party Dependency ( written in requirements.txt) 

| Depedency | Version |
|-----------|---------|
| Pillow    | 10.3.0  |

## Depolyment process

1. Install the thrid-party Library according to requirements.txt: `pip install -R requirement.txt`
2. run ManagerSystem through execute `python ./main.py`

## Projekt Description
The student grade management system 
User needs to login this system at first. Then the welcome view in main page will be opened. 

After that user can switch to other views through the menu bar to insert, modify, delete, display the student grade information

## Project Structure
- Student_Management_System
  - data: contains source data
    - \_\_init\_\_.py
    - database.py: script for data processing
    - student_grade.json: contains student grade
    - user.json: contains username and password for login
    - welcome.jpg: image for welcome page
  - ui
    - \_\_init\_\_.py
    - LoginPage.py // create Login page
    - MainPage.py // create Main Page. It slaves several View Frames
    - ViewFrame.py
- \_\_init\_\_.py
- README.md
- requirements.txt: Dependency List
- main.py // main function to start this student grade management system

## Chart Flow 
```mermaid
graph TD
A[Login] --> B{Login Page}
	B --> C[Main Page: Welcome View]
	C --> D(Main Page: Insert View)
	C --> E(Main Page: Modify View)
	C --> F(Main Page: Display View)
	C --> G(Main Page: Delete View)
	C --> H(Main Page: About View)
```


## Login: username and password
| username | password |
|----------|----------|
| admin    | admin    |
| Yanbo    | 123456   |


## Snapchat

### Login Page

![Login Page](./screenshot/01_LoginPage.png)

### Main Page

Welcome View 

![Welcome View](./screenshot/02_WelcomeView.png)

Insert View

![Insert View](./screenshot/03_InsertView.png)

Modify View

![Modify View](./screenshot/04_ModifyView.png)

Display View

![Display View](./screenshot/05_DisplayView.png)

Delete View

![Delete View](./screenshot/06_DeleteView.png)

About View

![About View](./screenshot/07_AboutView.png)


## Other
@Coding=UTF-8  
@Auther:Yanbo Zhu
@Time:2024-05  
@ProjectName:Student Grade Management System
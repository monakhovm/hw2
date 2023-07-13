# Task: [Password change for Linux User](https://github.com/devops01ua/python01-hw/blob/main/homeworks/HW2.md)

## Requirements:

- The program should prompt the user to enter a username.
- The program should check if user exist in system.
- The program should ask the user to input a password or generate a new one if not provided.
- The program should check the password against specified requirements
minimum length
presence of different character types (uppercase, lowercase, digits, special characters)
any other criteria you specify.
- Change password for user
- The program should print the results, including the username, the original or generated password, and whether the password meets the requirements.
Useful Links https://www.maketecheasier.com/how-linux-stores-manages-user-passwords/ https://www.section.io/engineering-education/how-to-execute-linux-commands-in-python/ https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python

---

## How to run the script:
```bash
./set_password.py
```
---

## Git flow
1. clone the repository
```bash
git clone git@github.com:monakhovm/hw2.git

```
2. create and switch to new branch
```bash
git checkout -b <name_branch>
```
3. to code

4. add changes to index
```bash
git add set_password.py
```
5. commit changes
```bash
git commit -m "coments"
```
6. push changes to github
```bash
git push # --set-upstream origin name_branch
```
or
```
git push origin branch
```
7. create pull request

8. coordinate the PR with colleagues

---

## code style:
## [black](https://pypi.org/project/black/)
```
pip install black
```

```
black {source_file_or_directory}
```
---




<div align="center">
  <img alt="logo"  src="https://raw.githubusercontent.com/kelwys/devcast/fec4e8e5d59f1f1ebaafc68c3a3a7e0ab4f2bcac/public/logo-dark.svg">
</div>


<h3 align="center">
    🎧  Devcast is a technology podcast for the developer community. 🎧 
</h3>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/kelwys/devcast-api?color=%2304D361">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/kelwys/devcast-api">

  <a href="https://github.com/kelwys/devcast-api/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/kelwys/devcast-api">
  </a>

   <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
   <a href="https://github.com/kelwys/devcast-api/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/kelwys/devcast-api?style=social">
  </a>
</p>

<p align="center">
  <a href="#about-the-project">About The Project</a> |
  <a href="#technologies">Technologies</a> |
  <a href="#contribution">Contribution</a> |
  <a href="#author">Author</a> |
  <a href="#license">License</a>
</p>

<h4 align="center">
	🚧 Status: Building 🚀  🚧
</h4>
</br>


<h2 id="about-the-project" > ⏰📈 About The Project </h2>

Listen to the best technology podcast

Python Backend API of [DEVCAST](https://github.com/kelwys/devcast)!

---

## 🚀 Getting Started

This project contains 2 parts:
Backend and Frontend. Visit the frontend [HERE](https://github.com/kelwys/devcast).

Later, run the development server:

```bash
# Clone Repository
$ git clone https://github.com/kelwys/devcast-api.git

# Go to server folder
$ cd devcast-api

# Create a Virtualenv with Python 3.6
$ python -m venv .venv
$ source .venv/bin/activate

# Install the dependencies.
$ pip install -r requirements\local.txt

# Configure the instance with .env
$ cp env_sample .env

# Apply migrations
$ Python manage.py migrate

# Lift the postgres on the docker
$ docker-compose -f local.yml up -d

# Create a super user
$ Python manage.py createsuperuser

# Run Aplication
$ Python manage.py runserver

# Access localhost
http://localhost:8000
```
---


<h2 id="technologies"> 🛠 Technologies </h2>

The following tools were used in the construction of the project:

- **[Python](https://www.python.org/)**
- **[Django](https://www.djangoproject.com/)**
- **[Django Rest Framework](https://www.django-rest-framework.org/)**

---

<h2 id="contribution"> 💪 Contribution </h2>

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<h2 id="author"> 💻 Author </h2>

<img style="border-radius: 50% !important;" src="https://kelwys.github.io/assets/images/avatar.png" width="100px;" alt="photo author"/>

 <sub><b>Kelwy Oliveira</b></sub></a> <a href="https://www.linkedin.com/in/kelwyoliveira/" title="kelwy`s linkedin">🚀</a>
 <br />

If you want to do a project with me or chat, don't hesitate to send me a message: ⤵️
<p align="left">
  <a href="https://www.linkedin.com/in/kelwyoliveira/"><img src="https://img.shields.io/badge/-kelwyoliveira-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>
  <a href="mailto:kelwyduarte@gmail.com"><img src="https://img.shields.io/badge/-kelwyduarte@gmail.com-D14836?style=flat&logo=Gmail&logoColor=white"/>
</p>

---

<h2 id="license"> 📝 License </h2>

This project is under the [MIT](./LICENSE) license.

---

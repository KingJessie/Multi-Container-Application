# Flask Apps with Docker Compose

## Intro
This repo contains two Flask apps, both containerised with Docker:
- Hello World App – a minimal Flask service that returns "Hello, world!".
- Visitor Counter App – A Flask application deployed with Docker Compose across multiple containers, using Redis for persistent storage and Nginx as a reverse proxy. The app records total visits and displays a bar chart of visits over the past 7 days.


## Project Structure
```shell
.Multi-Container-Application
├── assets
│   ├── img1.png
│   └── img2.png
├── challenge
│   ├── app.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── requirements.txt
│   ├── static
│   │   ├── images
│   │   └── style.css
│   └── templates
│       ├── count.html
│       └── index.html
├── hello_flask
│   ├── app.py
│   ├── docker-compose.yml
│   └── Docker
```
## What I Learned

While building these apps I learned:
- How to run a simple Flask app inside a Docker container.
- How to use multi-stage builds to make images lighter by separating build and runtime stages.
- How to define services with Docker Compose so multiple containers (Flask, Redis, Nginx) can be started together with a single command.
- How persistent storage in Docker works by mounting volumes, so Redis data is not lost when containers stop.
- How Nginx can act as a reverse proxy and, when configured properly, as a load balancer for multiple Flask replicas.
- The benefit of Compose guaranteeing the same environment across development, CI, and production, avoiding the “works on my machine” problem.

## Setup

### Clone the Repo
```shell
git clone https://github.com/KingJessie/Multi-Container-Application.git
cd Multi-Container-Application
```

### Running the Visitor Counter App
1. Go into the `challenge/` folder:
   ```shell
    cd challenge
   ```
2. Build and start the app
    ```shell
    docker compose up --scale web=3 --build
    ```
3. Open [http://localhost:5004](http://localhost:5004) in your browser to use the Visitor Counter App.

- Flask app is served through Nginx on port 5004
- Redis is available on port 6379 with persistent volume storage

## Visitor Counter App

Here’s what the Visitor Counter App looks like when running:

https://github.com/user-attachments/assets/a4a2d290-f1dc-42eb-b364-a30b93905bd5


## License

This project is licensed under the MIT License.

## Acknowledgments

- Learning resources and guidance from @CoderCo
- [Panda icons](https://www.flaticon.com/free-icons/panda) *created by Anastassiya Motokhova - Flaticon*
- [Panda background](https://pixabay.com/illustrations/pandas-panda-pattern-panda-bears-7400748/) *created by nipunmadusanka32 – Pixabay*  
# My Web Server

## 프로젝트 소개
Python Flask로 만든 간단한 웹 서버를 Docker로 실행하는 프로젝트입니다.

## 기술 스택
- Python 3.9
- Flask
- Docker

## 실행 방법
# 이미지 빌드
docker build -t my-web-server .

# 컨테이너 실행
docker run -p 5000:5000 my-web-server

# 브라우저에서 확인
http://localhost:5000

## 바인드 마운트 실습
# 파일 수정이 즉시 컨테이너에 반영됨
docker run -p 5000:5000 -v $(pwd):/app my-web-server

## Docker 볼륨 실습
# 볼륨 생성
docker volume create my-volume

# 볼륨 마운트 후 실행
docker run -p 5000:5000 -v my-volume:/app/data my-web-server

# 컨테이너 삭제 후에도 데이터 유지 확인
docker rm [컨테이너ID]
docker volume inspect my-volume

## 미션 완료 체크리스트
- [x] Flask 웹서버 작성 (app.py)
- [x] Dockerfile 작성
- [x] Docker 이미지 빌드
- [x] 컨테이너 실행 & 브라우저 접속 확인
- [x] 바인드 마운트 실습 완료
- [x] Docker 볼륨 영속성 검증 완료
- [x] GitHub Push 완료


## 실행 결과

Docker 컨테이너 안에서 Flask 웹 서버를 실행했다.

브라우저에서 http://127.0.0.1:5000 주소로 접속했을 때
웹페이지가 정상적으로 보이는 것을 확인했다.

또한 바인드 마운트를 사용해서
내 컴퓨터의 파일을 수정하면 Docker 컨테이너 안의 웹페이지에도
바로 반영되는 것을 확인했다.
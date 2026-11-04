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

---

## 터미널 기본 조작 실습 로그

PowerShell에서 기본 터미널 명령어를 실습했다.

```powershell
PS C:\Users\사용자명\Desktop\my-web-server> pwd

Path
----
C:\Users\사용자명\Desktop\my-web-server
```

```powershell
PS C:\Users\사용자명\Desktop\my-web-server> ls

Mode   LastWriteTime        Length Name
----   -------------        ------ ----
-a---- 2026-11-04 오후 1:47    234 app.py
-a---- 2026-11-04 오후 1:47    121 Dockerfile
-a---- 2026-11-04 오후 2:20   1508 README.md
```

### 오류 1: `ls -a`

PowerShell에서는 Linux의 `ls -a` 옵션이 그대로 동작하지 않았다.

```powershell
PS C:\Users\사용자명\Desktop\my-web-server> ls -a
Get-ChildItem : 매개 변수 이름 'a'이(가) 모호하므로 매개 변수를 처리할 수 없습니다.
```

해결 방법:

```powershell
PS C:\Users\사용자명\Desktop\my-web-server> ls -Force
```

### 디렉토리 생성 및 이동

```powershell
PS C:\Users\사용자명\Desktop\my-web-server> mkdir terminal-practice
PS C:\Users\사용자명\Desktop\my-web-server> cd terminal-practice
```

### 오류 2: `touch`

PowerShell에서는 Linux의 `touch` 명령어가 기본적으로 인식되지 않았다.

```powershell
PS C:\Users\사용자명\Desktop\my-web-server\terminal-practice> touch empty.txt
touch : 'touch' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다.
```

해결 방법:

```powershell
PS C:\Users\사용자명\Desktop\my-web-server\terminal-practice> New-Item empty.txt -ItemType File
```

### 파일 생성, 내용 확인, 복사, 이름 변경, 삭제

```powershell
PS C:\Users\사용자명\Desktop\my-web-server\terminal-practice> echo "hello terminal" > hello.txt

PS C:\Users\사용자명\Desktop\my-web-server\terminal-practice> cat hello.txt
hello terminal

PS C:\Users\사용자명\Desktop\my-web-server\terminal-practice> cp hello.txt copy-hello.txt

PS C:\Users\사용자명\Desktop\my-web-server\terminal-practice> mv copy-hello.txt renamed-hello.txt

PS C:\Users\사용자명\Desktop\my-web-server\terminal-practice> rm renamed-hello.txt
```

### PowerShell과 Linux 명령어 차이 정리

| 작업 | Linux/Git Bash | PowerShell |
|---|---|---|
| 현재 위치 확인 | `pwd` | `pwd` |
| 목록 확인 | `ls` | `ls` |
| 숨김 파일 포함 목록 | `ls -a` | `ls -Force` |
| 디렉토리 생성 | `mkdir` | `mkdir` |
| 빈 파일 생성 | `touch empty.txt` | `New-Item empty.txt -ItemType File` |
| 파일 내용 출력 | `cat` | `cat` |
| 파일 복사 | `cp` | `cp` |
| 파일 이름 변경 | `mv` | `mv` |
| 파일 삭제 | `rm` | `rm` |

또한 바인드 마운트를 사용해서
내 컴퓨터의 파일을 수정하면 Docker 컨테이너 안의 웹페이지에도
바로 반영되는 것을 확인했다.

---

## 터미널 기본 조작 실습 로그
...

---

## 파일/디렉토리 권한 확인 및 chmod 실습

Git Bash에서 `ls -l` 명령어를 사용하여 파일과 디렉토리의 권한을 확인했다.

```bash
pwd
ls -l
-rw-r--r-- app.py
drwxr-xr-x terminal-practice/
chmod +x app.py
ls -l app.py
-rw-r--r-- app.py
chmod -x app.py
ls -l app.py
-rw-r--r-- app.py

## Docker 설치 및 기본 점검

### Docker 버전 확인

Docker가 설치되어 있는지 확인하기 위해 아래 명령어를 실행했다.

```powershell
docker --version
```

실행 결과:

```text
Docker version 29.9.2, build a82e528
```

확인 결과 Docker 버전이 출력되었으므로 Docker 설치가 완료된 것을 확인했다.

### Docker 동작 상태 확인

Docker가 실제로 정상 작동하는지 확인하기 위해 아래 명령어를 실행했다.

```powershell
docker info
```

주요 실행 결과:

```text
Client:
 Version: 29.9.2
 Context: desktop-linux

Server:
 Server Version: 29.9.2
 Containers: 2
 Running: 0
 Stopped: 2
 Images: 1
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
```

확인 결과 Docker Client와 Server 정보가 정상적으로 출력되었으므로 Docker가 정상 작동 중임을 확인했다.

### Docker 이미지 목록 확인

현재 로컬에 저장된 Docker 이미지 목록을 확인하기 위해 아래 명령어를 실행했다.

```powershell
docker images
```

실행 결과:

```text
IMAGE                  ID            DISK USAGE   CONTENT SIZE
my-web-server:latest   fab89a85a8e8  203MB        49.7MB
```

이를 통해 로컬 환경에 `my-web-server:latest` Docker 이미지가 저장되어 있음을 확인했다.

---

### hello-world 컨테이너 실행

Docker가 컨테이너를 정상적으로 실행할 수 있는지 확인하기 위해 아래 명령어를 실행했다.

```powershell
docker run hello-world
```

처음에는 로컬에 `hello-world:latest` 이미지가 없어 Docker Hub에서 이미지를 내려받았다.

```text
Unable to find image 'hello-world:latest' locally
Status: Downloaded newer image for hello-world:latest
```

이후 다음 메시지가 출력되었다.

```text
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

이를 통해 Docker가 이미지를 다운로드하고 컨테이너를 정상 실행할 수 있음을 확인했다.

### Docker 컨테이너 목록 확인

현재 실행 중인 컨테이너를 확인하기 위해 아래 명령어를 실행했다.

```powershell
docker ps
```

실행 결과 현재 실행 중인 컨테이너는 없었다.

전체 컨테이너 목록을 확인하기 위해 아래 명령어를 실행했다.

```powershell
docker ps -a
```

실행 결과:

```text
CONTAINER ID   IMAGE          COMMAND           STATUS
9e79e2e44203   hello-world    "/hello"          Exited (0)
257de8514f10   my-web-server  "python app.py"   Exited (0)
b811beb86a2    my-web-server  "python app.py"   Exited (0)
```

`hello-world` 컨테이너는 실행 후 바로 종료되기 때문에 `docker ps`에는 보이지 않고, `docker ps -a`에서 확인할 수 있었다.

`Exited (0)` 상태를 통해 컨테이너가 오류 없이 정상 종료되었음을 확인했다.


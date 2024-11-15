# Kafka_study
Docker에 Kafka설치하고 Python에서 Kafka사용하기

## Docker에 Kafka설치
+ YAML파일이 필요하다
  + docker-compose.yaml
  + YAML파일은 블럭구조를 가지므로 들여쓰기를 주의해서 작성해야한다
+ 2개의 이미지가 필요하다
  + kafka
  + zookeeper : 카프카 코디네이터

### 설치 명령
YAML파일이 있는 디렉토리 위치에서 명령을 실행해야한다
**docker-compose up -d**
+ 설치 확인1 : docker ps
+ 설치 확인2 : docker desktop에서 확인
![image](https://github.com/user-attachments/assets/102670f3-8d7a-464f-8ba8-663d7a27542a)

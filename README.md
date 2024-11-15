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

### Kafka Test
#### Topic 생성
1. kafka컨테이너로 접속 : docker exec -it kafka /bin/bash
2. 실행 관련 명령들이 저장되어 있는 bin디렉토리로 이동 : cd /opt/kafka/bin
3. Topic 생성 : kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic exam-topic
4. Topic 조회 : kafka-topics.sh --bootstrap-server localhost:9092 --list
5. Topic 삭제 : kafka-console-producer.sh --topic exam-topic --broker-list localhost:9092
#### 메세지 전송
+ kafka-console-producer.sh --topic exam-topic --broker-list localhost:9092
  + 메세지 입력
#### 전송한 메세지 확인
새로운 터미널을 새로 열어서 실행한다
+ kafka-console-consumer.sh --topic exam-topic --bootstrap-server localhost:9092 --from-beginning
입력한 메세지가 전송되어서 보인다 

# Kafka_study
vsCode로 Docker에 Kafka설치하고 Python에서 Kafka사용하기

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


![image](https://github.com/user-attachments/assets/197620c2-1cbf-453a-b689-737380c7c245)

#### 전송한 메세지 확인
새로운 터미널을 새로 열어서 실행한다
+ kafka-console-consumer.sh --topic exam-topic --bootstrap-server localhost:9092 --from-beginning
입력한 메세지가 전송되어서 보인다 


![image](https://github.com/user-attachments/assets/6a40e3dc-5505-4ae6-a965-bbd29fb432ae)
---
## Python에서 Kafka사용
**Python에서 Kafka를 사용하기 위해서는 패키지를 설치해야하는데 패키지 설치를 위해 가상환경이 필요하다**
+ python디렉토리를 만들고 해당 디렉토리에서 가상환경을 생성하여 CMD창으로 변경하여 가상환경을 활성화하여 패키지 설치
+ **pip install kafka-python**

### Topic을 생성하여 메세지 전송 : pythonproducer.py
+ send, write, print 수행 : 버퍼에 기록하는 것
+ 메세지 전송 수행 : 버퍼가 가득 찬 것을 의미
+ flush 수행 : 버퍼를 비우는 것


![image](https://github.com/user-attachments/assets/66183019-2439-495f-8179-e57c36a2fcba)

### 메세지를 받았는지 확인 : pythonconsumer.py
+ 새로운 CMD창에서 실행


![image](https://github.com/user-attachments/assets/aa163a27-1e20-47ce-847a-40c9dcef9f2f)

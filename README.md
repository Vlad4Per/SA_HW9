# SA_course_HW9
Message Brokers
# Team 22
Pershko Vladislav v.pershko@innopolis.university

Sergey Dzyuba s.dzyuba@innopolis.university

Mikhail Voronin m.voronin@innopolis.university

Vladislav Vechkanov v.vechkanov@innopolis.university

## Project Overview
Our goal is to compare two architectures: **Pipes and Filters** and **Event-Based**.
### Event-Based Architecture
For the Event-Based architecture, we use RabbitMQ for interaction between services.
**Structure:**
- `filter_service`
    - `filter_service.py`
- `publish_service`
    - `publish_service.py`
- `rest_api_service`
    - `rest_api_service.py`
- `screaming_service`
    - `screaming_service.py`
### Pipes and Filters Architecture
For the Pipes and Filters architecture, we use Python's queue for interaction between processes (services).
**Structure:**
- `main.py`
- `Pipes-and-filters`
  - `filter_service`
      - `filter_service.py`
  - `publish_service`
      - `publish_service.py`
  - `rest_api_service`
      - `rest_api_service.py`
  - `screaming_service`
      - `screaming_service.py`
## Results
video with comparison of these architectures: https://disk.yandex.ru/i/oLnTG0nO3hZwjw 
#### CPU peak usage: 
- Event-Based Architecture: >6%
- Pipes-and-filters: <2%
#### MEM average usage:
- Event-Based Architecture: 1.5%
- Pipes-and-filters: 2%
#### Time spent to process 10 requests (seconds):
- Event-Based Architecture: 9.21
- Pipes-and-filters: 12.20
## Installation
1. Clone the repository
2. Enter your credentials
3. Run the code in your IDE

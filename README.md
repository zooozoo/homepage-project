


## Custom Homepage Project [www.news-collecter.com](https://www.news-collecter.com/)
홈페이지로 쓰고자 직접 제작한 웹사이트 입니다.
주기적으로 포탈과 언론사의 메인 기사 제목을 10개정도씩 가져와 한 화면에 보여주는 사이트입니다.


![프로젝트 작동영상 gif](news-collecter-resize-compres.gif)


* 프로젝트명 : News-Collecter
* 기간 : 2018.03.09 – 2018.05.11
* 내용 :
  수많은 언론사가 뉴스를 만들어 냅니다. 뉴스의 소비자들은 각각의 언론사의 뉴스 취사선택에 따라 영향을 받기 마련입니다. 
  예를들면 언론사는 어떤 사항을 뉴스거리로 보도할 것인지, 혹은 같은 사항이라도 어떤 단어를 선택해서 제목을 뽑을 것인지에 따라 
  뉴스 소비자들은 해당 사항에 대해서 긍정 혹은 부정적인 영향을 받게 됩니다. 
  정보의 호수속에서 균형잡힌 시각을 얻기위해서는 여러 언론사들의 헤드라인 선정이나, 사안에 대한 논조 등을 비교해 가면서 볼 수 
  있어야 하는데 기존 포탈에서는 뉴스를 보여주는 것이 목적이 아닌지라 이러한 역할을 하기에는 한계점이 있다고 생각했습니다. 
  그래서 광고나 검색을 위한 포탈이 아닌 한눈에 여러 언론사의 헤드라인을 모아서 볼 수 있는 일종의 뉴스 포탈을 통해 특정 사안에 
  대한 각 언론사별 논조를 비교하거나, 뉴스의 취사선택에서 어떤 차이점을 보이는지 확인하며 나만의 생각을 가질 수 있는데 도움을주는 
  페이지를 만들고자 했습니다.
* 사용기술 :
  * Django, uwsgi, nginx를 사용해 웹서버를 구축했습니다.
  * Django Template, CSS와 Bootstrap을 활용해 웹 페이지를 구현했습니다.
  * request와 beautiful soup을 사용해서 언론과 포탈의 뉴스 타이틀을 가져왔습니다. 각 언론사
  별로HTML구조가 다르기 때문에 언론사별 메소드를 구현하였고 bulk_create 쿼리를
  활용하기 위해 class로 구현했습니다.
  * Celery와 AWS Simple Queue Service를 활용하여 지정한 시간 간격으로 메시지큐의 요청을
  통해 각 언론사 뉴스타이틀을 가져오게끔 구성해 놓았습니다.
  * Supervisor를 활용해 배포된 상태에서 Nginx와 wsgi, Celery를 자동으로 백그라운드에서
  실행시키도록 구성했습니다.
  * Docker와 AWS Elastic beanstalk을 활용해 배포작업을 진행하였습니다.
  * Route53을 활용해 도메인 이름을 부여하고 AWS의 Certificate Manager 서비스를 활용해
  SSL인증서를 발급받고 적용했습니다.
* Github - [https://github.com/zooozoo/homepage-project](https://github.com/zooozoo/homepage-project)
* 프로젝트 도메인 [http://www.news-collecter.com](http://www.news-collecter.com)
* 진행사항 기록 [https://zooozoo.github.io/records/2018-03-23-PROJECT-NEWS-COLLECTER/](https://zooozoo.github.io/records/2018-03-23-PROJECT-NEWS-COLLECTER/)
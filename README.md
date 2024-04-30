# 한국어 방언 (사투리) 음성 합성

한국 5개 지역의 사투리로 말하는 인공지능. Tacotron2 기반.

## 합성 결과 예시

```
헬로월드! 유튜브 빵형의 개발도상국에 어서오세요!
```

- [강원도](https://voca.ro/1aHL8s0MHxz4)
- [제주도](https://voca.ro/1glI7LP1Dd2c)
- [충청도](https://voca.ro/120EqSRyJH25)
- [경상도](https://voca.ro/1hRzziA4c8D9)
- [전라도](https://voca.ro/1mQbP19vCs2l)

## 데이터셋

[AI허브 - 한국어 방언 발화 데이터셋](https://www.aihub.or.kr/aihubdata/data/list.do?pageIndex=1&currMenu=115&topMenu=100&dataSetSn=&srchdataClCode=DATACL001&srchOrder=&SrchdataClCode=DATACL002&searchKeyword=%ED%95%9C%EA%B5%AD%EC%96%B4+%EB%B0%A9%EC%96%B8&srchDataRealmCode=REALM002&srchDataTy=DATA004)


- https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=119


## 사전 학습 모델 다운로드

![](imgs/01.png)

1. AI허브 회원가입 - 데이터셋 상세 페이지 - 활용 AI 모델 및 코드 - AI 모델 다운로드

2. 압축 해제 - 03.AI모델 - 1. Binary File - 음성합성 - `acoustic.ckpt`, `vocoder.ckpt`

3. `logs/model` 폴더 저장

## 테스트 코드

[test.ipynb](test.ipynb)

## 제작지원

- [AI허브](https://www.aihub.or.kr)
- [NIA 한국정보화진흥원](https://www.nia.or.kr/)
- [유튜브 빵형의 개발도상국](https://www.youtube.com/channel/UC9PB9nKYqKEx_N3KM-JVTpg)


### 부가설명

- stt : speack to text
- tts : text to speech
- 사내에서 내가 설정한 목소리로 텍스트를 읽어준다.

- AI 모델 - 1. Binaryfile - 음성합성률
- 프로젝트 폴더 내 logs/model 경로로 이동

1. 원하는 사투리로 읽어주는 서비스
2. 이런 데이터셋을 활용하는것은 어렵기 때문에 데이터셋을 구하기 어려움 => ai hub는 가공이 잘 되어있음
3. 우리가 원하는 파일을 선택한다 => 음성합성 선택

4. python app.py
    - TTS 단점 : 학습시간이 조금 오래걸린다


    

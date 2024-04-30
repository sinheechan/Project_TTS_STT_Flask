# Project_TTS_STT_Flask

Tacotron2 기반 한국어 방언 (사투리) 음성 합성 모델 학습

<br />

< img src= >

<br />

<br /><br /> 

## Object

Tacotron2는 텍스트를 음성으로 변환하는 딥러닝 기반의 음성 합성 모델입니다.

OpenAI Whisper는 텍스트를 입력으로 받아들여 자연스러운 대화형 응답을 생성하는 언어 모델입니다.

우리는 이 과정을 통해 Text에서 Speak 사이를 번갈아 변환을 수행할 수 있습니다.

본 과정에서는 국내 5개 지역의 방언 데이터셋을 기반으로 학습 모델을 구축하여 TTS를 구현하는 과정을 학습합니다.

<br /><br /> 

## 데이터셋

[IT_Korea_Academy] leelang7 - torch-hybrid-tacotron2
[AI허브] - 한국어 방언 발화 데이터셋

<br /><br /> 

## 사전 학습 모델 다운로드 

1. AI허브 회원가입 - 데이터셋 상세 페이지 - 활용 AI 모델 및 코드 - AI 모델 다운로드

2. 압축 해제 - 03.AI모델 - 1. Binary File - 음성합성 - `acoustic.ckpt`, `vocoder.ckpt`

3. `logs/model` 폴더 생성 및 저장

<br /><br /> 

## TTS, STT WorkFlow

[test.ipynb]


    

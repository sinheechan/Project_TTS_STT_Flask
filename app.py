# Setting

import gradio as gr
import torch
import numpy as np
import soundfile as sf

from model.model_inference_v2 import Tacotron2 # 텍스트를 음성으로 변환
from vocoder.model.waveglow import WaveGlow # Tacotron2에서 생성된 멜 스펙트로그램을 오디오로 변환
from vocoder.denoiser_librosa import Denoiser # 오디오 신호에 데노이징(소음 제거) 작업을 수행

from korean_text.korean_cleaner_cls import KoreanCleaner # korean_cleaner_cls.py 내 KoreanCleaner 클래스 로드

from text import text_to_sequence # 텍스트를 시퀀스로 변환
from utils.util import to_var # 데이터를 PyTorch의 변수(Variable)로 변환

device = 'cpu' # cuda / GPU 권장

# Tacotron2

Tacotron2_model = torch.load('logs/model/acoustic.ckpt', map_location=torch.device(device)) # AI hub 모델

model = Tacotron2() # Tacotron2 로드
model.load_state_dict(Tacotron2_model['model']) # 모델 가중치 가져옴
model = model.eval() # 테스트(추론) 모드로 설정

# Vocoder

Vocoder_model = torch.load('logs/model/vocoder.ckpt', map_location=torch.device(device))

vocoder = WaveGlow() # WaveGlow
vocoder.load_state_dict(Vocoder_model['model'])
vocoder = vocoder.remove_weightnorm(vocoder) # WaveGlow 모델에서 가중치 정규화를 제거
vocoder.eval()

denoiser = Denoiser(vocoder, 0.1) # 생성된 오디오의 잡음을 줄이는 역할 / 잡음 강도 0.1
korean_cleaner = KoreanCleaner() # 한국어 텍스트를 전처리 / Tacotron2 모델에 제공하기 전에 텍스트의 품질을 향상

# TTS 모델 전달하기 전 전처리 / 클리너
def inference(text):
    text = korean_cleaner.clean_text(text)

    sequence = text_to_sequence(text, ['multi_cleaner'])
    sequence = to_var(torch.IntTensor(sequence)[None, :]).long()

    sigma = 0.5
    strength = 10
    sample_rate = 22050

    with torch.no_grad():
        _, mel_outputs_postnet, linear_outputs, _, alignments = model.inference(sequence) # sequence
        wav = vocoder.infer(mel_outputs_postnet, sigma=sigma)

        wav *= 32767. / max(0.01, torch.max(torch.abs(wav))) # 인코딩
        wav = wav.squeeze()
        wav = wav.cpu().detach().numpy().astype('float32')

        wav = denoiser(wav, strength=strength)

    wav = np.append(wav, np.array([[0.0] * (sample_rate // 2)]))

    wav_file = wav.astype(np.int16)
    sf.write('temp.wav', wav_file, sample_rate)

    return 'temp.wav' # temp.wave

demo = gr.Interface(fn=inference, inputs="text", outputs="audio")
demo.launch()

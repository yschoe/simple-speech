import speech_recognition as sr
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 음성 인식 함수
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("음성을 입력하세요...")
        try:
            # 음성 녹음
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("음성을 처리 중입니다...", flush=True)
            # 음성 텍스트 변환
            text = recognizer.recognize_google(audio, language='ko-KR')
            return text.lower()
        except sr.WaitTimeoutError:
            print("시간 초과: 음성이 입력되지 않았습니다.", flush=True)
        except sr.UnknownValueError:
            print("오류: 음성을 이해하지 못했습니다.", flush=True)
        except sr.RequestError as e:
            print(f"오류: 음성 인식 서비스에 문제가 있습니다. {e}", flush=True)
    return None

# 주요 단어를 감지하는 함수
def process_command(command):
    commands = ["시작", "종료", "회전", "직진", "후진"]
    if command in commands:
        print(f"명령어 '{command}' 인식됨!", flush=True)
        # 여기에 각 명령에 대한 처리를 추가하세요.
        if command == "종료":
            print("프로그램을 종료합니다.", flush=True)
            return False
    else:
        print("알 수 없는 명령입니다.", flush=True)
    return True

# 메인 프로그램
def main():
    running = True
    print("인식을 시작합니다. 시작, 종료, 회전, 직진, 후진 중한 단어를 말씀해주세요", flush=True)
    while running:
        result = recognize_speech()
        if result:
            print(f"인식된 텍스트: {result}", flush=True)
            for command in ["시작", "종료", "회전", "직진", "후진"]:
                if command in result:
                    running = process_command(command)
                    break

if __name__ == "__main__":
    main()

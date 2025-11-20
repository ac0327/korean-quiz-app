import streamlit as st
import random

# 韓文字母 (Hangeul) 練習數據
HANGEUL_DATA = {
    'ㅏ': 'a', 'ㅑ': 'ya', 'ㅓ': 'eo', 'ㅕ': 'yeo', 'ㅗ': 'o', 
    'ㅛ': 'yo', 'ㅜ': 'u', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅣ': 'i',
    'ㄱ': 'g/k', 'ㄴ': 'n', 'ㄷ': 'd/t', 'ㄹ': 'r/l', 'ㅁ': 'm', 
    'ㅂ': 'b/p', 'ㅅ': 's', 'ㅇ': '(silent)/ng', 'ㅈ': 'j', 'ㅊ': 'ch',
}

# 基礎韓文單字練習數據
WORD_DATA = {
    '안녕하세요': '你好/您好',
    '감사합니다': '謝謝',
    '네': '是/對',
    '아니요': '不/不是',
    '사랑해': '我愛你',
    '이름': '名字',
    '물': '水',
    '커피': '咖啡',
    '학생': '學生'
}

def hangeul_quiz_page():
    """韓文字母測驗頁面邏輯"""
    st.header("📝 韓文字母 (Hangeul) 練習")
    st.caption("請輸入以下字母的主要羅馬拼音/發音")
    
    # 確保頁面狀態中有當前的字母和正確答案
    if 'hangeul_char' not in st.session_state or st.session_state.quiz_type != 'hangeul':
        st.session_state.hangeul_char = random.choice(list(HANGEUL_DATA.keys()))
        st.session_state.correct_hangeul = HANGEUL_DATA[st.session_state.hangeul_char]
        st.session_state.quiz_type = 'hangeul'
        st.session_state.result = ""

    current_char = st.session_state.hangeul_char
    correct_answer = st.session_state.correct_hangeul
    
    # 顯示問題
    st.markdown(f"## 字母：<span style='color: #007bff; font-size: 3em;'>{current_char}</span>", unsafe_allow_html=True)
    
    # 輸入框和提交按鈕
    user_input = st.text_input("輸入你的羅馬拼音/發音 (例如: a 或 g/k)", key="hangeul_input")
    
    if st.button("提交答案 (字母)"):
        # 檢查答案
        user_input_clean = user_input.strip().lower()
        
        # 允許多個正確答案，用 '/' 分隔
        possible_answers = [ans.strip().lower() for ans in correct_answer.split('/')]
        
        if user_input_clean in possible_answers:
            st.session_state.result = f"🎉 **正確！** '{current_char}' 的發音是 **{correct_answer}**。"
            st.session_state.result_style = "success"
        else:
            st.session_state.result = f"❌ **錯誤！** '{current_char}' 的發音是 **{correct_answer}**。請再試試！"
            st.session_state.result_style = "error"
        
        # 隨機選擇下一個問題，並清除輸入框
        st.session_state.hangeul_char = random.choice(list(HANGEUL_DATA.keys()))
        st.session_state.correct_hangeul = HANGEUL_DATA[st.session_state.hangeul_char]
        st.experimental_rerun() # 重新運行，顯示新題目和結果
        
    # 顯示結果
    if st.session_state.get('result'):
        if st.session_state.result_style == "success":
            st.success(st.session_state.result)
        else:
            st.error(st.session_state.result)

def word_quiz_page():
    """基礎單字測驗頁面邏輯"""
    st.header("📖 基礎單字練習")
    st.caption("請輸入以下韓文單字的中文意思")

    # 確保頁面狀態中有當前的單字和正確答案
    if 'korean_word' not in st.session_state or st.session_state.quiz_type != 'word':
        st.session_state.korean_word = random.choice(list(WORD_DATA.keys()))
        st.session_state.correct_meaning = WORD_DATA[st.session_state.korean_word]
        st.session_state.quiz_type = 'word'
        st.session_state.result = ""

    current_word = st.session_state.korean_word
    correct_meaning = st.session_state.correct_meaning
    
    # 顯示問題
    st.markdown(f"## 單字：<span style='color: #ff4b4b; font-size: 2.5em;'>{current_word}</span>", unsafe_allow_html=True)
    
    # 輸入框和提交按鈕
    user_input = st.text_input("輸入你的中文意思", key="word_input")
    
    if st.button("提交答案 (單字)"):
        # 檢查答案
        user_input_clean = user_input.strip()
        
        # 簡易檢查：判斷使用者輸入是否包含在正確答案中，或正確答案是否包含在使用者輸入中
        if user_input_clean in correct_meaning or correct_meaning in user_input_clean:
            st.session_state.result = f"🎉 **正確！** '{current_word}' 的意思是 **{correct_meaning}**。"
            st.session_state.result_style = "success"
        else:
            st.session_state.result = f"❌ **錯誤！** '{current_word}' 的意思是 **{correct_meaning}**。"
            st.session_state.result_style = "error"

        # 隨機選擇下一個問題
        st.session_state.korean_word = random.choice(list(WORD_DATA.keys()))
        st.session_state.correct_meaning = WORD_DATA[st.session_state.korean_word]
        st.experimental_rerun() # 重新運行，顯示新題目和結果

    # 顯示結果
    if st.session_state.get('result'):
        if st.session_state.result_style == "success":
            st.success(st.session_state.result)
        else:
            st.error(st.session_state.result)


def main():
    """主應用程式架構"""
    st.set_page_config(page_title="韓文練習 App", layout="centered")
    
    st.title("🇰🇷 韓文初學者練習 App")
    st.write("請從左側選單選擇你的練習模式！")

    # 使用 Streamlit 的側邊欄 (Sidebar) 製作選單
    st.sidebar.title("練習選單")
    
    # 初始化 session state 來儲存選中的模式
    if 'quiz_mode' not in st.session_state:
        st.session_state.quiz_mode = '字母練習'

    # 選單選項
    mode = st.sidebar.radio(
        "選擇練習模式",
        ('字母練習', '單字練習'),
        index=0  # 預設選擇第一個
    )

    # 根據選單顯示對應的頁面
    if mode == '字母練習':
        hangeul_quiz_page()
    elif mode == '單字練習':
        word_quiz_page()

# 運行主函式
if __name__ == "__main__":
    main()
import streamlit as st
import requests

# Streamlitアプリケーションの設定
st.title("GitHub Issue Bot")
st.write("このアプリはGitHub Issueに自動でコメントを追加するボットです。")

# ユーザー入力のためのフォーム
with st.form(key='github_form'):
    token = st.text_input("GitHub Personal Access Token", type="password")
    owner = st.text_input("リポジトリ所有者（ユーザー名または組織名）")
    repo = st.text_input("リポジトリ名")
    issue_number = st.number_input("Issue番号", min_value=1, step=1)
    comment_body = st.text_area("コメント内容")
    
    submit_button = st.form_submit_button(label='コメントを追加')

if submit_button:
    if not token or not owner or not repo or not issue_number or not comment_body:
        st.error("すべてのフィールドに入力してください。")
    else:
        # GitHub API呼び出し用ヘッダー
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # コメント内容
        comment_data = {
            "body": comment_body
        }
        
        # GitHub APIエンドポイントURL
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
        
        # API呼び出し
        response = requests.post(url, json=comment_data, headers=headers)
        
        if response.status_code == 201:
            st.success("コメントが正常に追加されました。")
        else:
            st.error(f"コメントの追加に失敗しました: {response.status_code}")
            st.json(response.json())
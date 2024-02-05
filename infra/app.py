import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from lib import document_connector
import langchain
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_vertexai import VertexAI

from langchain.text_splitter import CharacterTextSplitter

langchain.verbose = False

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.event("app_mention")
def handle_mention(event, say):
    query = event["text"]
    url = os.environ.get("URL")
    documents = document_connector.url_loader(url)

    use_embedding_model_name = os.environ.get("USE_EMBEDDING_MODEL_NAME")
    embeddings = VertexAIEmbeddings(model_name=use_embedding_model_name)

    index = VectorstoreIndexCreator(
        embedding=embeddings, vectorstore_cls=FAISS).from_loaders([documents])

    use_chat_model_name = os.environ.get("USE_CHAT_MODEL_NAME")

    chat = VertexAI(model_name=use_chat_model_name, temperature=0)
    result = index.query_with_sources(query, llm=chat)
    message = f"ans: {result['answer']} {result['sources']}"
    say(message)


# アプリを起動します
if __name__ == "__main__":

    APP_ENVIRONMENT = os.environ.get("APP_ENVIRONMENT", "prod")

    if APP_ENVIRONMENT == "prod":
        app.start(port=int(os.environ.get("PORT", 3000)))
    else:
        SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

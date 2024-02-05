# LangChainVertexAIDockerSample

LangChainコンテナを作ってその中でVertexAIを起動する

```bash
docker build . -t lang_chain
```

```bash
docker run -d -e USE_CHAT_MODEL_NAME=text-bison-32k -e USE_EMBEDDING_MODEL_NAME=textembedding-gecko@001 -e SLACK_BOT_TOKEN=xoxb-XXXX -e SLACK_APP_TOKEN=xapp-XXXX -e USE_CHAT_MODEL_NAME=text-bison-32k -e USE_EMBEDDING_MODEL_NAME=textembedding-gecko@001 -e URL=url -e APP_ENVIRONMENT=prod lang_chain
```

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.document_loaders import BSHTMLLoader


def document_loaders(root_path: str = './', glob: str = "**/*.py") -> DirectoryLoader:
    return DirectoryLoader(root_path, glob=glob, loader_cls=TextLoader)


def url_loader(url: str):
    return RecursiveUrlLoader(url)


def html_loader(url:str):
    return UnstructuredHTMLLoader(url)


def bs4_loader(url:str):
    return BSHTMLLoader(url)

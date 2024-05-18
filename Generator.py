from langchain_upstage import ChatUpstage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from Retriever import searchLocal
from Ocr import ocr

llm = ChatUpstage()


def generateAnswer(poiList):
    context = searchLocal(poiList)
    print(context)

    prompt_template = PromptTemplate.from_template(
        """
        Please provide most correct answer from the following context.
        Context is POI list.
        Must answer as word.
        ---
        Question: Cluster context by address. Tell me with address with the most context. Must answer as address.
        ---
        Context: {Context}
        """
    )
    chain = prompt_template | llm | StrOutputParser()
    result = chain.invoke({"Context": context})
    print(result)

    return result


def generatePoiList(img):
    img_text = ocr(img)
    prompt_template = PromptTemplate.from_template(
        """
        Please provide answer from the following context.
        Answer contains only list of POIs
        Do not translate language.
        And Format is csv without double quote.
        ---
        Question: 여기서 POI 이름이 될만한 것들을 리스트로 만들어줘
        ---
        Context: {context}
        """
    )
    chain = prompt_template | llm | StrOutputParser()
    pois_ = chain.invoke(
        {
            "context": img_text,
        }
    ).split(",")
    result = [poi.strip() for poi in pois_]
    print(result)
    return result


def generateMapUrl(word):
    naver_map_url = "https://map.naver.com/p/search/"
    return f"{naver_map_url}{word.replace(' ', '%20')}"


def totalChain(bimg):
    return generateMapUrl(generateAnswer(generatePoiList(bimg)))


if __name__ == "__main__":
    result = totalChain(open("test8.png", "rb"))
    print(result)

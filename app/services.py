from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.settings import OPENAI_API_KEY

from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from app.openai_helper.chains import ChainFactory
from app.openai_helper.models import GPT_4, GPTConfig
from app.openai_helper.utility import make_openai_call


def extract_transcript_from_youtube(youtube_link):
    # Generate transcript array
    video_id = youtube_link.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    ### Currently we are using free key that doesn't allow more the 2 concurrent call.
    ### Currenly we are using sequential call that takes 70sec to generate for 10min video 
    output_list=[]
    for i in range(0,len(transcript),30):
        end_index=i+30 if i+30<len(transcript) else len(transcript)
        # structured_data.append({"transcript":transcript[i:end_index]})
        output= ChainFactory().timestamp_chain().run(transcript=transcript[i:end_index])
        output_list.append(output)
        
    ### If we use paid openai key then we will be able to make parallel call and whose process takes 4-5 sec.
    ### Below is the code for parallel call with paid openai key
    # structured_data=[]
    # for i in range(0,len(transcript),30):
    #     end_index=i+30 if i+30<len(transcript) else len(transcript)
        # structured_data.append({"transcript":transcript[i:end_index]})
    # output_list = make_openai_call(structured_data,ChainFactory(config=GPTConfig(model=GPT_4)).timestamp_chain())


    # Format output
    output_text=""
    for output_json in output_list:
        output_json = eval(output_json)
        for key in output_json.keys():
            output_text+=f"{key} : {output_json[key]}\n"

    return output_text
